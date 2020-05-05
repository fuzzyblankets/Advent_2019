"""
https://adventofcode.com/2019/day/2#part2
"""
# int_code = [1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 13, 1, 19, 1, 19, 10, 23, 1, 23, 13,
#             27, 1, 6, 27, 31, 1, 9, 31, 35, 2, 10, 35, 39, 1, 39, 6, 43, 1, 6, 43, 47, 2, 13, 47,
#             51, 1, 51, 6, 55, 2, 6, 55, 59, 2, 59, 6, 63, 2, 63, 13, 67, 1, 5, 67, 71, 2, 9, 71, 75, 1, 5,
#             75, 79, 1, 5, 79, 83, 1, 83, 6, 87, 1, 87, 6, 91, 1, 91, 5, 95, 2, 10, 95, 99, 1, 5, 99, 103,
#             1, 10, 103, 107, 1, 107, 9, 111, 2, 111, 10, 115, 1, 115, 9, 119, 1, 13, 119, 123, 1, 123,
#             9, 127, 1, 5, 127, 131, 2, 13, 131, 135, 1, 9, 135, 139, 1, 2, 139, 143, 1, 13, 143, 0, 99, 2, 0, 14, 0]

parameter_count_dict = {'01':3, '02':3, '03':1, '04':1, '99':0}

def instruction_split(instruct):
    opcode_and_modes = str(instruct[0]).zfill(5)
    opcode = opcode_and_modes[-2:]
    parameters = instruct[1:]
    modes = list(reversed(list(opcode_and_modes[:len(parameters)])))
    parameters = parameter_discovery(zip(parameters, modes))
    return opcode, parameters


def parameter_discovery(inputs):
    #TODO figure out how parameter mode applies to writing values out
    parameters=[]
    for i in inputs:
        if i[1] == '0':  # positional
            position  = i[0]
            parameters.append(int_code[position])
        elif i[1] == '1':  # absolute
            absolute = i[0]
            parameters.append(absolute)
        else:
            raise ValueError("Incorrect parameter mode: {}".format(i[1]))
    return parameters


def op_01(param1, param2, param3):
    result = param1 + param2
    int_code[param3] = result


def op_02(param1, param2, param3):
    result = int_code[param1] * int_code[param2]
    int_code[param3] = result

def op_03(param1, value):
    int_code[param1] = value

def op_04(param1):
    print (int_code[param1])


def main(int_code):
    instruction_pointer = 0
    while instruction_pointer < len(int_code):
        opcode = str(int_code[instruction_pointer]).zfill(2)
        if opcode in parameter_count_dict:
            parameter_count = parameter_count_dict[opcode]
        else:
            raise ValueError("Opcode parameter count not defined in dictionary.")
        instruction_length = parameter_count+1 #parameters plus opcode
        opcode, parameters = instruction_split(int_code[instruction_pointer:instruction_pointer+instruction_length])

        if opcode == '01':
            op_01(parameters[0],parameters[1],parameters[2])
        elif opcode == '02':
            op_02(parameters[0],parameters[1],parameters[2])
        elif opcode == '03':
            value = int(input("Please enter the ID of the system to test:\n"))
            op_03(parameters[0], value)
        elif opcode == '04':
            op_04(parameters[0])
        elif opcode == '99':
            print ("Identified End Marker. Halting Code.")
            break
        else:
            raise ValueError("Invalid opcode provided.\n Opcode: {}".format(opcode))

        instruction_pointer += instruction_length

if __name__ == '__main__':
    int_code =[]
    puzzle_input_path = "/Users/Ellie/PycharmProjects/Advent_2019/Day5/puzzle_input.txt"

    with open(puzzle_input_path, 'r') as file:
        for line in file:
            puzzle_input = line.strip().split(",")
            for entry in puzzle_input:
                int_code.append(int(entry))

    print(int_code[225])

    main(int_code)




