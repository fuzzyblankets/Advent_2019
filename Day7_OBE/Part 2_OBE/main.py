"""
https://adventofcode.com/2019/day/7
"""

import argparse
from itertools import permutations
import payloads
from processor import Computer

class AMPS():
    def __init__(self, start, end, loopback_mode):
        self.start= int(start)
        self.end = int(end)
        self.loopback_mode = loopback_mode

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Int Code Options.')
    parser.add_argument('-l', '--loopback-mode', action='store_true',
                        dest='loopback_mode', help='turn on thruster loopback mode')
    parser.add_argument('-r', '--input-range', nargs='+', required = True,
                        dest='input_range', help='phase range for amplifiers')
    args = parser.parse_args()

    loopback_mode = False
    if args.loopback_mode:
        loopback_mode = args.loopback_mode

    range_start = args.input_range[0]
    range_end = args.input_range[1]

    int_code =[]
    puzzle_input_path = "//puzzle_input_test.txt"
    with open(puzzle_input_path, 'r') as file:
        puzzle_input = file.read().strip().split(",")
        int_code = list(map(str, puzzle_input))

    comp = Computer(data=int_code)
    amps = AMPS(range_start, range_end, loopback_mode)
    amp_inputs = permutations(range(amps.start, amps.end + 1))
    thruster_out_max = 0
    for combos in amp_inputs:
        amp_input = 0
        for phase in combos:
            amp_out = comp.calculate(amp_input, phase)
            amp_input = amp_out
        while loopback_mode:
            amp_out_loop = processor.processor(code, amp_input, phase)
            if amp_out_loop is None:
                break
            amp_input = amp_out_loop
            amp_out = amp_out_loop
        if amp_out > thruster_out_max:
            thruster_out_max = amp_out
            combo_out = combos

    return thruster_out_max, combo_out


def loopback(self, code, amp_input):
    return processor.processor(phase, amp_input, code)


    thruster_out_max, combo_out = amps.output(amps.code,
                                              amps.start,
                                              amps.end,
                                              amps.loopback_mode)


    print("Max thruster output: {}".format(thruster_out_max))
    print("Amplifier Combo: {}".format(combo_out))





