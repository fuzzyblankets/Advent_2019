"""
https://adventofcode.com/2019/day/4
"""
import itertools


def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def check_increasing(password):
    return "".join(sorted(password)) == password


def check_repeat(password):
    for a, b in pairwise(password):
        if a == b:
            return True
    return False


good_count = 0
input_puzzle = range(265275,781584)

for password in input_puzzle:
    password = str(password)
    if check_increasing(password):
        if check_repeat(password):
            good_count+=1

