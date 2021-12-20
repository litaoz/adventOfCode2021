'''
--- Part Two ---
It seems like the individual flashes aren't bright enough to navigate. However, you might have a better option: the flashes seem to be synchronizing!

In the example above, the first time all octopuses flash simultaneously is step 195:

After step 193:
5877777777
8877777777
7777777777
7777777777
7777777777
7777777777
7777777777
7777777777
7777777777
7777777777

After step 194:
6988888888
9988888888
8888888888
8888888888
8888888888
8888888888
8888888888
8888888888
8888888888
8888888888

After step 195:
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
If you can calculate the exact moments when the octopuses will all flash simultaneously, you should be able to navigate through the cavern. What is the first step during which all octopuses flash?

'''
from typing import List, Tuple
from collections import deque

input_filename = 'input11-2.txt'


class Octopuses:
    def __init__(self, grid):
        self.grid = grid
        self.flashes = 0
        self.steps = 0

    def print(self):
        for row in self.grid:
            buffer = []
            for col in row:
                if col > 9:
                    buffer.append('0')
                    continue
                buffer.append(str(col))
            print(''.join(buffer))
        print()

    def next_step(self):
        flashed = set()
        to_flash = []

        # Every octopus increment by one
        for r, row in enumerate(self.grid):
            for c, col in enumerate(row):
                self.grid[r][c] += 1
                if self.grid[r][c] > 9:
                    to_flash.append((r, c))

        # Flash
        while len(to_flash) > 0:
            point = to_flash.pop()
            if point in flashed:
                continue
            flashed.add(point)
            self.flashes += 1

            # Neighbors get +1 energy
            neighbors = self.find_neighbors(point)
            for neighbor in neighbors:
                r_neighbor, c_neighbor = neighbor
                self.grid[r_neighbor][c_neighbor] += 1
                if self.grid[r_neighbor][c_neighbor] > 9 and neighbor not in flashed:
                    to_flash.append(neighbor)

        # Restore all flashed octopus to 0
        for point in flashed:
            r, c = point
            self.grid[r][c] = 0

        self.steps += 1

    def first_step_all_synchronized(self):
        limit = 1000

        def is_zero(itm):
            return itm == 0

        for step in range(limit):
            if all([all([is_zero(itm) for itm in row]) for row in self.grid]):
                return step
            self.next_step()

    def find_neighbors(self, point) -> List[Tuple]:
        height = len(self.grid)
        width = len(self.grid[0])
        r, c = point

        neighbor_rel_coords = []
        for r_rel in [-1, 0, 1]:
            for c_rel in [-1, 0, 1]:
                if r_rel == 0 and c_rel == 0:
                    continue  # skip itself
                neighbor_rel_coords.append((r_rel, c_rel))

        neighbors = []
        for rel_coord in neighbor_rel_coords:
            r_rel, c_rel = rel_coord
            r_neighbor = r + r_rel
            c_neighbor = c + c_rel
            if 0 <= r_neighbor < height and 0 <= c_neighbor < width:
                neighbors.append((r_neighbor, c_neighbor))

        return neighbors


def parse_input(input_filename) -> List[List[int]]:
    input_data_raw = []
    with open(input_filename) as f:
        input_data_raw = f.read().splitlines()

    octopus_grid = []
    for row in input_data_raw:
        chars = [int(char) for char in row]
        octopus_grid.append(chars)

    return octopus_grid


def main():
    octopuses_grid = parse_input(input_filename)
    octopuses = Octopuses(octopuses_grid)
    return octopuses.first_step_all_synchronized()


if __name__ == "__main__":
    result = main()
    print(result)  # 351
