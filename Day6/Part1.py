"""
https://adventofcode.com/2019/day/6
"""
import nested_lookup
from collections import ChainMap


def main(puzzle_input):
    orbit_map = {}
    orbit_map = puzzle_split(puzzle_input, orbit_map)
    total_orbits = 0
    for orbit_key in orbit_map.keys():
        for orbit in orbit_map[orbit_key]:
            total_orbits += orbit_count(orbit_map, orbit)
    return total_orbits

def puzzle_split(puzzle_input, orbit_map):
    for orbits in puzzle_input:
        orbit = orbits.split(")")
        orbitee = orbit[0]
        orbiter = orbit[1]
        if not orbitee in orbit_map.keys():
            orbit_map[orbitee] = [orbiter]
        else:
            orbit_map[orbitee].append(orbiter)
    return orbit_map

def depth (dict, value):
    for k, v in dict.items():
        if value == v or value in v:
            return True, k
    return False, None

def orbit_count(orbit_map, orbit, dig = True, orbit_count = 0):
    while dig:
        dig, key = depth(orbit_map, orbit)
        if dig:
            orbit = key
            orbit_count += 1
    return orbit_count

# def first_split(puzzle_input, orbit_map):
#     for orbits in puzzle_input:
#         orbit = orbits.split(")")
#         orbitee = orbit[0]
#         orbiter = orbit[1]
#         if not orbitee in orbit_map:
#             orbit_map[orbitee] = [{}]
#         orbit_map[orbitee][orbiter] = [{}]
#     return orbit_map


if __name__ == '__main__':
    puzzle_input_path = "/root/PycharmProjects/Advent_2019/Day6/puzzle_input.txt"
    with open(puzzle_input_path, 'r') as file:
        puzzle_input = file.read().strip().split("\n")

    total_orbit_output = main(puzzle_input)

    print("Total orbit count: {}".format(total_orbit_output))

