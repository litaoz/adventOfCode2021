'''
--- Day 13: Transparent Origami ---
You reach another volcanically active part of the cave. It would be nice if you could do some kind of thermal imaging so you could tell ahead of time which caves are too hot to safely enter.

Fortunately, the submarine seems to be equipped with a thermal camera! When you activate it, you are greeted with:

Congratulations on your purchase! To activate this infrared thermal imaging
camera system, please enter the code found on page 1 of the manual.
Apparently, the Elves have never used this feature. To your surprise, you manage to find the manual; as you go to open it, page 1 falls out. It's a large sheet of transparent paper! The transparent paper is marked with random dots and includes instructions on how to fold it up (your puzzle input). For example:

6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
# is a dot on the paper and . is an empty, unmarked position:
The first section is a list of dots on the transparent paper. 0,0 represents the top-left coordinate. The first value, x, increases to the right. The second value, y, increases downward. So, the coordinate 3,0 is to the right of 0,0, and the coordinate 0,7 is below 0,0. The coordinates in this example form the following pattern, where

...#..#..#.
....#......
...........
# ..........
...#....#.#
...........
...........
...........
...........
...........
.#....#.##.
....#......
......#...#
# ..........
# .#........
Then, there is a list of fold instructions. Each instruction indicates a line on the transparent paper and wants you to fold the paper up (for horizontal y=... lines) or left (for vertical x=... lines). In this example, the first fold instruction is fold along y=7, which designates the line formed by all of the positions where y is 7 (marked here with -):

...#..#..#.
....#......
...........
# ..........
...#....#.#
...........
...........
-----------
...........
...........
.#....#.##.
....#......
......#...#
# ..........
# .#........
Because this is a horizontal line, fold the bottom half up. Some of the dots might end up overlapping after the fold is complete, but dots will never appear exactly on a fold line. The result of doing this fold looks like this:

# .##..#..#.
# ...#......
......#...#
# ...#......
.#.#..#.###
...........
...........
Now, only 17 dots are visible.

Notice, for example, the two dots in the bottom left corner before the transparent paper is folded; after the fold is complete, those dots appear in the top left corner (at 0,0 and 0,1). Because the paper is transparent, the dot just below them in the result (at 0,3) remains visible, as it can be seen through the transparent paper.

Also notice that some dots can end up overlapping; in this case, the dots merge together and become a single dot.

The second fold instruction is fold along x=5, which indicates this line:

# .##.|#..#.
# ...#|.....
.....|#...#
# ...#|.....
.#.#.|#.###
.....|.....
.....|.....
Because this is a vertical line, fold left:

#####
#...#
#...#
#...#
#####
.....
.....
The instructions made a square!

The transparent paper is pretty big, so for now, focus on just completing the first fold. After the first fold in the example above, 17 dots are visible - dots that end up overlapping after the fold is completed count as a single dot.

How many dots are visible after completing just the first fold instruction on your transparent paper?
'''
from typing import Tuple

input_filename = 'input13-1.txt'


class Paper:
    def __init__(self, coords):
        self.coords = coords

    def print(self):
        allr = [r for r, _ in self.coords]
        allc = [c for _, c in self.coords]
        width = max(allc) + 1
        height = max(allr) + 1

        buffer = ''
        for r in range(height):
            row_buffer = []
            for c in range(width):
                if (r, c) in self.coords:
                    row_buffer.append('#')
                else:
                    row_buffer.append('.')
            buffer += ''.join(row_buffer) + '\n'
        buffer += '\n'
        print(buffer)

    def fold(self, instruction):
        next_coords = set()
        axis, value = instruction

        for coord in self.coords:
            r, c = coord

            if axis == 'r':
                v = r
            elif axis == 'c':
                v = c

            # Reflect towards 0, 0
            if v <= value:
                next_coords.add(coord)
                continue

            diff = v - value
            v = v - 2 * diff
            if v >= 0 and axis == 'r':
                next_coords.add((v, c))
            elif v >= 0 and axis == 'c':
                next_coords.add((r, v))

        self.coords = next_coords

    def count_dots(self):
        return len(self.coords)


def parse_input(input_filename) -> Tuple[set[Tuple], list[Tuple]]:
    input_data_raw = []
    with open(input_filename) as f:
        input_data_raw = f.read().splitlines()

    instructions_start = 0
    dot_coords = set()
    for r, row in enumerate(input_data_raw):
        if row == '':
            instructions_start = r + 1
            break
        x, y = row.split(',')
        dot_coords.add((int(y), int(x)))

    fold_instructions = []
    for row in input_data_raw[instructions_start:]:
        instruction_str = row.strip('fold along ')
        axis, value = instruction_str.split('=')
        axis_map = {'x': 'c', 'y': 'r'}
        instruction = (axis_map[axis], int(value))
        fold_instructions.append(instruction)

    return dot_coords, fold_instructions


def main():
    dot_coords, instructions = parse_input(input_filename)
    grid = Paper(dot_coords)

    for instruction in instructions:
        grid.fold(instruction)
        break

    return grid.count_dots()


if __name__ == "__main__":
    result = main()
    print(result)  # 618
