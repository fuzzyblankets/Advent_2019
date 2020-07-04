"""
https://adventofcode.com/2019/day/7
"""

from itertools import permutations
import Part1_intcode


if __name__ == '__main__':
    int_code =[]
    puzzle_input_path = "//puzzle_input_test.txt"
    with open(puzzle_input_path, 'r') as file:
        puzzle_input = file.read().strip().split(",")
        int_code = list(map(int, puzzle_input))
    amp_inputs = permutations([0,1,2,3,4])
    thruster_out_max = 0
    for combo in amp_inputs:
        amp_a_out = Part1_intcode.main(combo[0], 0, int_code)
        amp_b_out = Part1_intcode.main(combo[1], amp_a_out, int_code)
        amp_c_out = Part1_intcode.main(combo[2], amp_b_out, int_code)
        amp_d_out = Part1_intcode.main(combo[3], amp_c_out, int_code)
        thruster_out = Part1_intcode.main(combo[4], amp_d_out, int_code)

        if thruster_out > thruster_out_max:
            thruster_out_max = thruster_out_max
            combo_out = combo

    print("Max thruster output: {}".format(thruster_out_max))
    print("Amplifier Combo: {}".format(combo_out))

