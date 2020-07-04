from aenum import MultiValueEnum
from enum import Enum

class Instruction():
    parameter_count_dict = {'01': 3, '02': 3, '03': 1, '04': 1, '05': 2, '06': 2, '07': 3, '08': 3, '99': 0}
    def __init__(self, instruction):
        modes = self.get_modes(str(instruction)[:-1])
        self.modes = MODE(modes)
        self.code = OPERATION_CODE(str(instruction)[len(modes):])
        self.privs = WRITER(modes)
        mode_list = list(map(int, opcode[:3][::-1]))
        self.mode = list(MODE(i) for i in mode_list)
        self.parameter_count = self.parameter_count_dict[opcode[-2:]]

def get_modes(instruction):
    mode1 = None
    mode2 = None
    mode3 = None

    modes = [mode[2], mode[1], mode[0] for mode in str(data):

class Computer ():
    def __init__(self, **kwargs):
        self.data = data
        self.idx = 0
        self.done = 0
        self.output = None

    def add(self, param):
        return  param[0] + param[1]

    def multiply(self, param):
        int_code[param[2]] = param[0] * param[1]

    def in_put(self, param, value):
        int_code[param[0]] = value

    def out_put(self, param):
        return int_code[param[0]]

    def jit(self, param):
        if param[0]:
            return param[1]

    def jif(self, param):
        if not param[0]:
            return param[1]

    def less_than(self, param):
        if param[0] < param [1]:
            int_code[param[2]] = 1
        else:
            int_code[param[2]] = 0

    def equals(self, param):
        if param[0] == param [1]:
            int_code[param[2]] = 1
        else:
            int_code[param[2]] = 0

    def calculate(self, input_signal, phase=None):
        while self.idx < len(self.data):
            modes = Instruction(self.data[self.idx])

            mode1, mode2, mode3 = self.data
            c
            parameters = int_code[instruction_pointer + 1:instruction_pointer + instruction.parameter_count + 1]

            if instruction.privs.name == "write":
                parameters_values = parameter_discovery(zip(parameters[:-1], instruction.mode), int_code)
                write_out = parameters[-1]
            else:
                parameters_values = parameter_discovery(zip(parameters, instruction.mode), int_code)

            if instruction.ops is OPERATION_CODE.TERMINATE:
                print("Identified End Marker. Halting Code.")
                return None

            elif instruction.ops is OPERATION_CODE.ADD:
                int_code[write_out] = parameters_values[0] + parameters_values[1]

            elif instruction.ops is OPERATION_CODE.MULTIPLY:
                int_code[write_out] = parameters_values[0] * parameters_values[1]

            elif instruction.ops is OPERATION_CODE.INPUT:
                if phase is not None:
                    int_code[write_out] = phase
                    phase = None
                else:
                    int_code[write_out] = input_signal

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

class Computer:


    def __str__(self):
        return "{}, {}, {}".format(self.ops, self.mode, self.parameter_count)




def parameter_discovery(params, int_code):
    parameters=[]
    for param in params:
        if param[1] is MODE.POSITION:  # positional
            parameters.append(int_code[param[0]])
        elif param[1] is MODE.IMMEDIATE:  # absolute
            parameters.append(param[0])
        else:
            raise ValueError("Incorrect parameter mode: {}".format(param[1]))
    return parameters



        instruction_pointer += (instruction.parameter_count+1)
