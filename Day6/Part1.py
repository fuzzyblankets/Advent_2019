"""
https://adventofcode.com/2019/day/6
"""
import nested_lookup
from collections import ChainMap


def main(puzzle_input):
    orbit_map = {}
    orbit_map = first_split(puzzle_input, orbit_map)

    print ("step1")

def first_split(puzzle_input, orbit_map):
    for orbits in puzzle_input:
        orbit = orbits.split(")")
        orbitee = orbit[0]
        orbiter = orbit[1]
        x = nested_lookup.nested_lookup(orbitee, orbit_map)
        if not x:
            orbit_map[orbitee] = [{}]
            orbit_map = nested_lookup.nested_update(orbit_map, key= orbitee, value= [{orbiter}])
        else:
            x.append({orbiter})
            for i in x:
                orbit_map = nested_lookup.nested_update(orbit_map, key=orbitee, value=i)
    return orbit_map




# def first_split(puzzle_input, orbit_map):
#     for orbits in puzzle_input:
#         orbit = orbits.split(")")
#         orbitee = orbit[0]
#         orbiter = orbit[1]
#         if not orbitee in orbit_map:
#             orbit_map[orbitee] = [{}]
#         orbit_map[orbitee][orbiter] = [{}]
#     return orbit_map
#
#
#
#
# def second_split(orbit_map):
#     for orbit in orbit_map.keys():
#         for item in orbit_map[orbit].keys():
#             x = nested_lookup.nested_lookup(item, orbit_map)
#             if len(x) > 0:
#                 nested_lookup.nested_update(orbit_map[orbit], key = item, value = x[1:])






if __name__ == '__main__':
    puzzle_input_path = "/Users/Ellie/PycharmProjects/Advent_2019/Day6/puzzle_input_test.txt"
    with open(puzzle_input_path, 'r') as file:
        puzzle_input = file.read().strip().split("\n")

    main(puzzle_input)

