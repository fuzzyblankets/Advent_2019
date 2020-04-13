"""
https://adventofcode.com/2019/day/5#part2
"""

from aenum import MultiValueEnum
from enum import Enum

class OPERATION_CODE(Enum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JIT = 5
    JIF = 6
    LESS_THAN = 7
    EQUALS = 8
    TERMINATE = 99

class WRITER(MultiValueEnum):
    write = 1, 2, 3, 7, 8
    retrieve = 4, 5, 6, 99

class MODE(Enum):
    POSITION = 0
    IMMEDIATE = 1

class Instruction:
    parameter_count_dict = {'01': 3, '02': 3, '03': 1, '04': 1, '05': 2, '06': 2, '07': 3, '08': 3, '99': 0}
    def __init__(self, opcode):
        self.ops = OPERATION_CODE(int(opcode[-2:]))
        self.privs = WRITER(int(opcode[-2:]))
        mode_list = list(map(int, opcode[:3][::-1]))
        self.mode = list(MODE(i) for i in mode_list)
        self.parameter_count = self.parameter_count_dict[opcode[-2:]]

    def __str__(self):
        return "{}, {}, {}".format(self.ops, self.mode, self.parameter_count)


class OPERATION():
    def add(param):
        int_code[param[2]] = param[0] + param[1]

    def multiply(param):
        int_code[param[2]] = param[0] * param[1]

    def in_put(param, value):
        int_code[param[0]] = value

    def out_put(param):
        return int_code[param[0]]

    def jit(param):
        if param[0]:
            return param[1]

    def jif(param):
        if not param[0]:
            return param[1]

    def less_than(param):
        if param[0] < param [1]:
            int_code[param[2]] = 1
        else:
            int_code[param[2]] = 0

    def equals(param):
        if param[0] == param [1]:
            int_code[param[2]] = 1
        else:
            int_code[param[2]] = 0





def parameter_discovery(params):
    parameters=[]
    for param in params:
        if param[1] is MODE.POSITION:  # positional
            parameters.append(int_code[param[0]])
        elif param[1] is MODE.IMMEDIATE:  # absolute
            parameters.append(param[0])
        else:
            raise ValueError("Incorrect parameter mode: {}".format(param[1]))
    return parameters


def main(int_code):
    instruction_pointer = 0
    while instruction_pointer < len(int_code):
        instruction = Instruction(str(int_code[instruction_pointer]).zfill(5))
        parameters = int_code[instruction_pointer+1:instruction_pointer+instruction.parameter_count+1]

        if instruction.privs.name == "write":
            parameters_values = parameter_discovery(zip(parameters[:-1], instruction.mode))
            last_value = parameters[-1]
            parameters_values.append(last_value)
        else:
            parameters_values = parameter_discovery(zip(parameters, instruction.mode))

        if instruction.ops is OPERATION_CODE.TERMINATE:
            print("Identified End Marker. Halting Code.")
            break

        elif instruction.ops is OPERATION_CODE.ADD:
            OPERATION.add(parameters_values)

        elif instruction.ops is OPERATION_CODE.MULTIPLY:
            OPERATION.multiply(parameters_values)

        elif instruction.ops is OPERATION_CODE.INPUT:
            value = int(input("Please enter the ID of the system to test:\n"))
            OPERATION.in_put(parameters_values, value)

        elif instruction.ops is OPERATION_CODE.OUTPUT:
            print("Program Output: {}".format(parameters_values))

        elif instruction.ops is OPERATION_CODE.JIT:
            if parameters_values[0]:
                instruction_pointer = OPERATION.jit(parameters_values)
                continue

        elif instruction.ops is OPERATION_CODE.JIF:
            if not parameters_values[0]:
                instruction_pointer = OPERATION.jif(parameters_values)
                continue

        elif instruction.ops is OPERATION_CODE.LESS_THAN:
            OPERATION.less_than(parameters_values)

        elif instruction.ops is OPERATION_CODE.EQUALS:
            OPERATION.equals(parameters_values)

        else:
            raise ValueError("Invalid opcode provided.\n Opcode: {}".format(opcode))

        instruction_pointer += (instruction.parameter_count+1)


if __name__ == '__main__':
    int_code =[]
    puzzle_input_path = "/Users/Ellie/PycharmProjects/Advent_2019/Day5/puzzle_input.txt"
    with open(puzzle_input_path, 'r') as file:
        puzzle_input = file.read().strip().split(",")
        int_code = list(map(int, puzzle_input))

    main(int_code)




