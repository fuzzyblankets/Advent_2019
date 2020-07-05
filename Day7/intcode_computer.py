"""
https://adventofcode.com/2019/day/5#part2
"""

from enum import Enum
from itertools import permutations

parameter_count_dict = {'01': 3, '02': 3, '03': 1, '04': 1, '05': 2, '06': 2, '07': 3, '08': 3, '99': 0}


class OperationCode(Enum):
    ADD = '01'
    MULTIPLY = '02'
    INPUT = '03'
    OUTPUT = '04'
    JIT = '05'
    JIF = '06'
    LESS_THAN = '07'
    EQUALS = '08'
    TERMINATE = '99'


class Computer():

    def __init__(self, **kwargs):
        self.ptr = 0
        self.code = kwargs.get("code", None)
        self.output = None
        self.opcode = None
        self.params = None
        self.terminate = None
        self.inputs = []

    def processor(self):
        while True:
            self.process_instruction(self.code[self.ptr])
            if self.opcode is OperationCode.TERMINATE:
                self.terminate = -1
                return self.output

            elif self.opcode is OperationCode.ADD:
                self.code[self.params[-1]] = self.params[0] + self.params[1]
                self.ptr += 4

            elif self.opcode is OperationCode.MULTIPLY:
                self.code[self.params[-1]] = self.params[0] * self.params[1]
                self.ptr += 4

            elif self.opcode is OperationCode.INPUT:
                if not self.inputs :
                    value = int(input("Please enter the ID of the system to test:\n"))
                else:
                    value = self.inputs.pop(0)
                self.code[self.params[0]] = value
                self.ptr += 2

            elif self.opcode is OperationCode.OUTPUT:
                self.output = self.code[self.params[0]]
                self.ptr += 2
                return self.output

            elif self.opcode is OperationCode.JIT:
                if self.params[0]:
                    self.ptr = self.params[1]
                else:
                    self.ptr += 3

            elif self.opcode is OperationCode.JIF:
                if not self.params[0]:
                    self.ptr = self.params[1]
                else:
                    self.ptr += 3

            elif self.opcode is OperationCode.LESS_THAN:
                if self.params[0] < self.params[1]:
                    self.code[self.params[-1]] = 1
                else:
                    self.code[self.params[-1]] = 0
                self.ptr += 4

            elif self.opcode is OperationCode.EQUALS:
                if self.params[0] == self.params[1]:
                    self.code[self.params[-1]] = 1
                else:
                    self.code[self.params[-1]] = 0
                self.ptr += 4

            else:
                raise ValueError("Invalid opcode provided.\n Opcode: {}".format(opcode))


    def process_instruction(self, input):
        instruction = str(input).zfill(5)
        self.opcode = OperationCode(instruction[-2:])
        param_count = parameter_count_dict[self.opcode.value]
        modes = [i for i in instruction[(-2 - param_count):-2]]
        modes.reverse()
        self.get_params(modes)

    def get_params(self, modes):
        self.params = []
        i = 1
        for mode in modes:
            if i == len(modes):
                if self.opcode not in [OperationCode.JIF, OperationCode.JIT]:
                    self.params.append(int(self.code[self.ptr + i]))
                    break
            if mode == '0':
                position = int(self.code[self.ptr + i])
                self.params.append(int(self.code[position]))
            elif mode == '1':
                self.params.append(int(self.code[self.ptr + i]))
            else:
                raise ValueError("Incorrect Mode Type")
            i += 1

if __name__ == '__main__':
    int_code = []
    puzzle_input_path = "/root/PycharmProjects/Advent_2019/Day5/puzzle_input.txt"
    with open(puzzle_input_path, 'r') as file:
        puzzle_input = file.read().strip().split(",")
        int_code = list(map(int, puzzle_input))


    amps1 = permutations([0, 1, 2, 3, 4])
    amps2 = permutations([5, 6, 7, 8, 9])
    thruster_out_max1 = []
    thruster_out_max2 = []

    computer = Computer(code=int_code)
    computer.processor()
    print("Program Output 1: {}".format(computer.output))


    for combo in amps1:
        computers = [Computer(code=int_code) for _ in range(5)]
        input_signal = 0
        for computer, phase_setting in zip(computers, combo):
            computer.inputs.append(phase_setting)
        for computer in computers:
            computer.inputs.append(input_signal)
            output_signal = computer.processor()
            input_signal = output_signal
        thruster_out_max1.append(output_signal)

    print("Program Output 1: {}".format(max(thruster_out_max1)))

    for combo in amps2:
        computers = [Computer(code=int_code) for _ in range(5)]
        input_signal = 0
        for computer, phase_setting in zip(computers, combo):
            computer.inputs.append(phase_setting)
        while computers[-1].terminate != -1:
            for computer in computers:
                computer.inputs.append(input_signal)
                output_signal = computer.processor()
                input_signal = output_signal
        thruster_out_max2.append(output_signal)

    print("Program Output 2: {}".format(max(thruster_out_max2)))
