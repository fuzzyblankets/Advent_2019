"""
https://adventofcode.com/2019/day/7
"""

from aenum import MultiValueEnum
from enum import Enum
from itertools import permutations

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


# def add(param):
#     return  param[0] + param[1]
#
# def multiply(param):
#     int_code[param[2]] = param[0] * param[1]
#
# def in_put(param, value):
#     int_code[param[0]] = value
#
# def out_put(param):
#     return int_code[param[0]]
#
# def jit(param):
#     if param[0]:
#         return param[1]
#
# def jif(param):
#     if not param[0]:
#         return param[1]
#
# def less_than(param):
#     if param[0] < param [1]:
#         int_code[param[2]] = 1
#     else:
#         int_code[param[2]] = 0
#
# def equals(param):
#     if param[0] == param [1]:
#         int_code[param[2]] = 1
#     else:
#         int_code[param[2]] = 0

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

def amplifiers (starting):
    amp_inputs_1 = permutations(range(0,5))
    amp_inputs_2 = permutations(range(5,10))
    thruster_out_max = 0
    for combo_1 in amp_inputs_1:
        amp_input = 0
        for phase in combo_1:
            amp_out = ic_processor(phase, amp_input, starting)
            amp_input = amp_out
        for combo_2 in amp_inputs_2:
            for phase in combo_2:
                amp_out = ic_processor(phase, amp_input, starting)
                amp_input = amp_out

            if amp_out > thruster_out_max:
                thruster_out_max = amp_out
                combo_out = combo

    return thruster_out_max, combo_out

def ic_processor(input_1, input_2, int_code):
    instruction_pointer = 0
    input_count = 1
    while instruction_pointer < len(int_code):
        instruction = Instruction(str(int_code[instruction_pointer]).zfill(5))
        parameters = int_code[instruction_pointer+1:instruction_pointer+instruction.parameter_count+1]

        if instruction.privs.name == "write":
            parameters_values = parameter_discovery(zip(parameters[:-1], instruction.mode))
            write_out = parameters[-1]
        else:
            parameters_values = parameter_discovery(zip(parameters, instruction.mode))

        if instruction.ops is OPERATION_CODE.TERMINATE:
            print("Identified End Marker. Halting Code.")
            break

        elif instruction.ops is OPERATION_CODE.ADD:
            int_code[write_out] =parameters_values[0]+parameters_values[1]

        elif instruction.ops is OPERATION_CODE.MULTIPLY:
            int_code[write_out] = parameters_values[0] * parameters_values[1]

        elif instruction.ops is OPERATION_CODE.INPUT:
            if input_count == 1:
                value = input_1
                int_code[write_out] = value
            else:
                value = input_2
                int_code[write_out] = value
            input_count+=1

        elif instruction.ops is OPERATION_CODE.OUTPUT:
            return parameters_values[0]

        elif instruction.ops is OPERATION_CODE.JIT:
            if parameters_values[0]:
                instruction_pointer = parameters_values[1]
                continue

        elif instruction.ops is OPERATION_CODE.JIF:
            if not parameters_values[0]:
                instruction_pointer = parameters_values[1]
                continue

        elif instruction.ops is OPERATION_CODE.LESS_THAN:
            if parameters_values[0] < parameters_values[1]:
                int_code[write_out] = 1
            else:
                int_code[write_out] = 0

        elif instruction.ops is OPERATION_CODE.EQUALS:
            if parameters_values[0] == parameters_values[1]:
                int_code[write_out] = 1
            else:
                int_code[write_out] = 0

        else:
            raise ValueError("Invalid opcode provided.\n Opcode: {}".format(opcode))

        instruction_pointer += (instruction.parameter_count+1)


if __name__ == '__main__':
    int_code =[]
    puzzle_input_path = "/root/PycharmProjects/Advent_2019/Day7/puzzle_input.txt"
    with open(puzzle_input_path, 'r') as file:
        puzzle_input = file.read().strip().split(",")
        starting_int_code = list(map(int, puzzle_input))
        int_code = list(map(int, puzzle_input))

    thruster_out_max, combo_out = amplifiers(int_code)

    print("Max thruster output: {}".format(thruster_out_max))
    print("Amplifier Combo: {}".format(combo_out))





