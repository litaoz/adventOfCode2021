'''
--- Part Two ---
Finish folding the transparent paper according to the instructions. The manual says the code is always eight capital letters.

What code do you use to activate the infrared thermal imaging camera system?
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
        self.print()
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

    grid.print()


if __name__ == "__main__":
    result = main()
    print(result)  # ALREKFKU
