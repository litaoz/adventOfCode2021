'''
--- Day 2: Dive! ---
Now, you need to figure out how to pilot this thing.

It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:

forward X increases the horizontal position by X units.
down X increases the depth by X units.
up X decreases the depth by X units.
Note that since you're on a submarine, down and up affect your depth, and so they have the opposite result of what you might expect.

The submarine seems to already have a planned course (your puzzle input). You should probably figure out where it's going. For example:

forward 5
down 5
forward 8
up 3
down 8
forward 2
Your horizontal position and depth both start at 0. The steps above would then modify them as follows:

forward 5 adds 5 to your horizontal position, a total of 5.
down 5 adds 5 to your depth, resulting in a value of 5.
forward 8 adds 8 to your horizontal position, a total of 13.
up 3 decreases your depth by 3, resulting in a value of 2.
down 8 adds 8 to your depth, resulting in a value of 10.
forward 2 adds 2 to your horizontal position, a total of 15.
After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)

Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?
'''

input_file = 'input2-1.txt'

input_data_raw = []
with open(input_file) as f:
    input_data_raw = f.readlines()


def parse_input(input_data):
    result = []
    for line in input_data:
        action, value = line.split()
        value = int(value)
        if action == 'forward':
            result.append((value, 0))
        elif action == 'up':
            result.append((0, -value))
        elif action == 'down':
            result.append((0, value))
    return result


def sum_of_tuples(input_list):
    x, y = 0, 0
    for action in input_list:
        dx, dy = action
        x += dx
        y += dy
    return (x, y)


actions = parse_input(input_data_raw)
x, y = sum_of_tuples(actions)
print(x, y, x*y)  # 1248
