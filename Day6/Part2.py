"""
https://adventofcode.com/2019/day/6#part2
"""
import nested_lookup
from collections import ChainMap


def main(puzzle_input):
    orbit_map = {}
    orbit_map = puzzle_split(puzzle_input, orbit_map)
    orbit_change_count = orbit_change(orbit_map, "YOU", "SAN")
    total_orbit_count = total_orbits(orbit_map)
    return orbit_change_count


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

def total_orbits(orbit_map):
    total_orbits = 0
    for orbit_key in orbit_map.keys():
        for orbit in orbit_map[orbit_key]:
            total_orbits += orbit_count(orbit_map, orbit)
    return total_orbits


def orbit_change(dict, start, end):
    start_path = orbit_path(dict, start)
    end_path = orbit_path(dict, end)

    for i in start_path:
        if i in end_path:
            start_match = start_path.index(i)
            end_match = end_path.index(i)
            return start_match+end_match



def orbit_path(orbit_map, orbit, dig=True):
    path_list = []
    while dig:
        dig, key = depth(orbit_map, orbit)
        if dig:
            orbit = key
            path_list.append(key)
    return path_list


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

    orbit_change_output = main(puzzle_input)

    print("Orbit change count: {}".format(orbit_change_output))

