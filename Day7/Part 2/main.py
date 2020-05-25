"""
https://adventofcode.com/2019/day/7
"""

import argparse
from payloads import PAYLOAD

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Int Code Options.')
    parser.add_argument('-l', '--loopback-mode', action='store_true', type=str,
                        dest='loopback_mode', help='turn on thruster loopback mode')
    args = parser.parse_args()

    loopback_mode = False
    if args.loopback_mode:
        loopback_mode = args.loopback_mode

    int_code =[]
    puzzle_input_path = "/root/PycharmProjects/Advent_2019/Day7/Part 2/puzzle_input_test.txt"
    with open(puzzle_input_path, 'r') as file:
        puzzle_input = file.read().strip().split(",")
        int_code = list(map(int, puzzle_input))


    thruster_out_max, combo_out = PAYLOAD.amplifiers(int_code, inp_range_start=0,inp_range_end=4)
    if loopback_mode:
        thruster_out_max

    print("Max thruster output: {}".format(thruster_out_max))
    print("Amplifier Combo: {}".format(combo_out))





