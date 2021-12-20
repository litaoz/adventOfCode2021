'''
--- Part Two ---
Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
Considering all lines from the above example would now produce the following diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....
You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?

'''

from typing import List, Tuple

input_filename = 'input5-2_test.txt'


class Board:
    def __init__(self):
        self.board = []
        self.width = 0
        self.height = 0

    def __repr__(self):
        # display the board
        lines = []
        for line in self.board:
            line_string = ''
            for num in line:
                line_string += f'{str(num).rjust(2)} '
            lines.append(line_string[:-1])
        board = '\n' + '\n'.join(lines) + '\n'
        return board

    def dangerous_points(self):
        return sum([sum([1 for itm in row if itm >= 2]) for row in self.board])

    def add_line_segment(self, line_segment: Tuple[int, int, int, int]):
        x1, y1, x2, y2 = line_segment

        height_needed = max(y1, y2) + 1
        if height_needed > self.height:
            new_row = [0 for _ in range(self.width)]
            for _ in range(self.height, height_needed):
                self.board.append(new_row.copy())
            self.height = height_needed

        width_needed = max(x1, x2) + 1
        if width_needed > self.width:
            for row in self.board:
                additional_width = [0 for _ in range(self.width, width_needed)]
                row += additional_width
            self.width = width_needed

        min_x = min(x1, x2)
        min_y = min(y1, y2)
        max_x = max(x1, x2)
        max_y = max(y1, y2)
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                if self.point_on_line_segment(line_segment, (x, y)):
                    self.board[y][x] += 1

    def point_on_line_segment(self, line_segment: Tuple[int, int, int, int], point: Tuple[int, int]):
        x1, y1, x2, y2 = line_segment
        x3, y3 = point

        if y1 > y2:
            y1, y2 = y2, y1
            x1, x2 = x2, x1

        if x1 == x2:
            return (x3 == x2) and (y1 <= y3 <= y2)

        slope = (y2 - y1) / (x2 - x1)
        is_point_on_line = (y3 - y1) == slope * (x3 - x1)
        is_point_in_bounding_box = (min(x1, x2) <= x3 <= max(
            x1, x2)) and (min(y1, y2) <= y3 <= max(y1, y2))
        return is_point_on_line and is_point_in_bounding_box


def parse_input(input_filename) -> List[Tuple[int, int, int, int]]:
    input_data_raw = []
    with open(input_filename) as f:
        input_data_raw = f.read().splitlines()
        #  input_data_raw.append('')  # recover a stripped ending space

    split_line_segments = [row.split('->') for row in input_data_raw]

    line_segments = []
    for row in split_line_segments:
        assert len(row) == 2
        x1, y1 = row[0].split(',')
        x2, y2 = row[1].split(',')
        line_segment = (int(x1), int(y1), int(x2), int(y2))
        line_segments.append(line_segment)

    return line_segments


def main():
    line_segments = parse_input(input_filename)
    board = Board()
    for line in line_segments:
        x1, y1, x2, y2 = line
        board.add_line_segment(line)
    return board.dangerous_points()


if __name__ == "__main__":
    result = main()
    print(result)  # 2800 too low
