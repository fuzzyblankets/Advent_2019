"""
https://adventofcode.com/2019/day/2#part2
"""
int_code = [1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 13, 1, 19, 1, 19, 10, 23, 1, 23, 13,
            27, 1, 6, 27, 31, 1, 9, 31, 35, 2, 10, 35, 39, 1, 39, 6, 43, 1, 6, 43, 47, 2, 13, 47,
            51, 1, 51, 6, 55, 2, 6, 55, 59, 2, 59, 6, 63, 2, 63, 13, 67, 1, 5, 67, 71, 2, 9, 71, 75, 1, 5,
            75, 79, 1, 5, 79, 83, 1, 83, 6, 87, 1, 87, 6, 91, 1, 91, 5, 95, 2, 10, 95, 99, 1, 5, 99, 103,
            1, 10, 103, 107, 1, 107, 9, 111, 2, 111, 10, 115, 1, 115, 9, 119, 1, 13, 119, 123, 1, 123,
            9, 127, 1, 5, 127, 131, 2, 13, 131, 135, 1, 9, 135, 139, 1, 2, 139, 143, 1, 13, 143, 0, 99, 2, 0, 14, 0]

parameter_count_dict = {'01':3, '02':3, '03':1, '04':1, '99':0}

def instruction_split(instruct):
    opcode_and_modes = str(instruct[0]).zfill(5)
    opcode = opcode_and_modes[-2:]
    parameters = instruct[1:]
    modes = list(reversed(list(opcode_and_modes[:len(parameters)])))
    param_and_mode = zip(parameters, modes)
    return op, param_and_mode


def op_01(pos1, pos2, pos3):
    result = int_code[pos1] + int_code[pos2]
    int_code[pos3] = result


def op_02(*args):
    result = int_code[pos1] * int_code[pos2]
    int_code[pos3] = result

def op_03(pos1):
    value = int(input("Enter input value for opcode 3: "))
    int_code[pos1] = value

def op_04(pos1):
    return int_code[pos1]

if __name__="__main__":
    instruction_pointer = 0
    while instruction_pointer < len(int_code):
        opcode = str(int_code[instruction_pointer]).zfill(2)
        if opcode in parameter_count_dict:
            parameter_count = parameter_count_dict[parameter_count]
        else:
            raise ValueError("Opcode parameter count not defined in dictionary.")
        opcode, parameters = instruction_split(int_code[instruction_pointer:instruction_pointer+parameter_count])
        if opcode == 01:
            op_one(int_code[i + 1], int_code[i + 2], int_code[i + 3])
        elif opcode == 02:
            op_two(int_code[i + 1], int_code[i + 2], int_code[i + 3])
        elif opcode == 03:
           pass
        elif opcode == 04

        elif int_code[i] == 99:
            break
        else:
            break



