import numpy
from collections import Counter

puzzle_input_path = "/root/PycharmProjects/Advent_2019/Day8/puzzle_input.txt"
with open(puzzle_input_path, 'r') as file:
    puzzle_input = file.read()

columns = 25
rows = 6

puzzle_input_length = len(puzzle_input)
# layers =puzzle_input_length/(rows*columns)

layers =[]
i=0
for layer in range(0,int((puzzle_input_length/(rows*columns)))):
    space_image = numpy.zeros(shape=[rows, columns])
    for line in space_image:
        for pixel in range(0, len(line)):
            line[pixel] = puzzle_input[i]
            i+=1
    layers.append(space_image)

layer = 0
zero_count = 1000000

for layer in layers:
    zeroes = 0
    ones = 0
    twos = 0
    for row in layer:
        values = Counter(row)
        zeroes += values[0]
        ones += values[1]
        twos += values[2]
    if zeroes < zero_count:
        zero_count = zeroes
        output = ones * twos

print("Part 1 output: {}".format(output))

output = ''
for i in range(0,rows):
    for j in range(0, columns):
        for layer in layers:
            if layer[i][j] in [0,1]:
                output+=str(int(layer[i][j]))
                if len(output) ==25:
                    print(output)
                    output = ''
                break
print(len(output))
print("Part 2 output: {}".format(output))







