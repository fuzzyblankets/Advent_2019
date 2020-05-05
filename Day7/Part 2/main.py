"""
https://adventofcode.com/2019/day/7
"""

if __name__ == '__main__':
    int_code =[]
    puzzle_input_path = "/root/PycharmProjects/Advent_2019/Day7/puzzle_input_test.txt"
    with open(puzzle_input_path, 'r') as file:
        puzzle_input = file.read().strip().split(",")
        int_code = list(map(int, puzzle_input))

    thruster_out_max, combo_out = amplifiers(int_code)

    print("Max thruster output: {}".format(thruster_out_max))
    print("Amplifier Combo: {}".format(combo_out))





