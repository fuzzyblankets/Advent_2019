import numpy

def field_of_vision(ast, field):
    ast_count = {'1':[], '2':[], '3':[], '4':[]}
    for asteroid in field:
        if asteroid == ast:
            continue
        rise = (ast[1]-asteroid[1])
        run = (ast[0]-asteroid[0])
        if rise >=0 and run >=0:
            quadrant = '1'
        elif rise <0 and run >=0:
            quadrant = '2'
        elif rise < 0 and run < 0:
            quadrant = '3'
        else:
            quadrant = '4'
        if run ==0:
            if run > 0:
                slope = "left"
            else:
                slope = "right"
        else:
            if rise == 0 and run == 0:
                slope = "self"
            else:
                slope = rise/run
        if slope not in ast_count[quadrant]:
            ast_count[quadrant].append(slope)

        total = len(ast_count['1'])+len(ast_count['2'])+len(ast_count['3'])+len(ast_count['4'])
    return total

int_code = []
puzzle_input_path = "/root/PycharmProjects/Advent_2019/Day10/puzzle_input.txt"
with open(puzzle_input_path, 'r') as file:
    puzzle_input = file.read().split("\n")
    i=0
    for row in puzzle_input:
        int_code.append(list(row))
        i+=1
    # int_code = list(map(int, puzzle_input))
asteroid_belt = numpy.array(int_code)
asteroid_locations = numpy.where(asteroid_belt == "#")
asteroid_locations_list = list(zip(asteroid_locations[0], asteroid_locations[1]))

max_count = 0
for asteroid in asteroid_locations_list:
    count = field_of_vision(asteroid, asteroid_locations_list)

    if count > max_count:
        max_count = count
        max_position = asteroid

print(max_count, max_position)