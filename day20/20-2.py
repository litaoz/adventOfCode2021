'''
--- Part Two ---
You still can't quite make out the details in the image. Maybe you just didn't enhance it enough.

If you enhance the starting input image in the above example a total of 50 times, 3351 pixels are lit in the final output image.

Start again with the original input image and apply the image enhancement algorithm 50 times. How many pixels are lit in the resulting image?

'''


input_filename = 'input20-2.txt'


class Grid:
    def __init__(self, grid_info, algo):
        self.padding_char = 0
        self.grid = grid_info
        self.algo = algo

        self.padding_size = 0
        # self.print()

    def step(self):

        def expand():
            padding = 2
            height = len(self.grid) + 2 * padding
            width = len(self.grid[0]) + 2 * padding

            padding_row = [self.padding_char for _ in range(width)]
            result = []
            for _ in range(padding):
                result.append(padding_row)

            for row in self.grid:
                new_row = [self.padding_char for _ in range(padding)]
                new_row += row
                new_row += [self.padding_char for _ in range(padding)]
                result.append(new_row)

            for _ in range(padding):
                result.append(padding_row)

            self.padding_size = padding
            self.grid = result

        def neighbors(r, c):
            height = len(self.grid)
            width = len(self.grid[0])
            neighbor_range = [-1, 0, 1]

            neighbor = []
            for r_rel in neighbor_range:
                r_neighbor = r_rel + r
                for c_rel in neighbor_range:
                    c_neighbor = c_rel + c
                    if 0 <= r_neighbor < height and 0 <= c_neighbor < width:
                        neighbor.append(self.grid[r_neighbor][c_neighbor])
                    else:
                        neighbor.append(self.padding_char)
            neighbor = [str(bit) for bit in neighbor]
            neighbor = ''.join(neighbor)
            neighbor = int(neighbor, base=2)
            return neighbor

        def flip_padding():
            if self.algo[0] == 0:
                return

            if self.padding_char == 0:
                self.padding_char = 1
            else:
                self.padding_char = 0

        expand()
        neighbors = [[neighbors(r, c) for c, col in enumerate(row)]
                     for r, row in enumerate(self.grid)]

        self.grid = [[self.algo[col] for col in row] for row in neighbors]
        flip_padding()
        # self.padding_size -= 2
        # self.print()

    def count_lights(self):
        return sum([sum(row) for row in self.grid])

    def print(self):
        char_map = ['.', '#']
        for row in self.grid:
            print(''.join([char_map[col] for col in row]))
        print()


def parse_input(input_filename) -> list[list[tuple]]:
    input_data_raw = []
    with open(input_filename) as f:
        input_data_raw = f.read().strip().split('\n\n')

    def parse_algo(group):
        char_map = {'.': 0, '#': 1}
        algo = [char_map[char] for char in group]
        return algo

    def parse_grid(group):
        char_map = {'.': 0, '#': 1}
        grid_info = []
        for line in group.split('\n'):
            row = [char_map[char] for char in line]
            grid_info.append(row)
        return grid_info

    algo = parse_algo(input_data_raw[0])
    grid_info = parse_grid(input_data_raw[1])
    return (grid_info, algo)


def main():
    grid_info, algo = parse_input(input_filename)
    grid = Grid(grid_info, algo)

    steps = 50
    for _ in range(steps):
        grid.step()

    # return ocean.count_beacons()
    return grid.count_lights()


if __name__ == "__main__":
    result = main()
    # import cProfile
    # cProfile.run('main()')

    print(result)  # 14790
