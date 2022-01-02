'''
--- Day 20: Trench Map ---
With the scanners fully deployed, you turn their attention to mapping the floor of the ocean trench.

When you get back the image from the scanners, it seems to just be random noise. Perhaps you can combine an image enhancement algorithm and the input image (your puzzle input) to clean it up a little.

For example:

..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

# ..#.
# ....
##..#
..#..
..###
The first section is the image enhancement algorithm. It is normally given on a single line, but it has been wrapped to multiple lines in this example for legibility. The second section is the input image, a two-dimensional grid of light pixels (#) and dark pixels (.).

The image enhancement algorithm describes how to enhance an image by simultaneously converting all pixels in the input image into an output image. Each pixel of the output image is determined by looking at a 3x3 square of pixels centered on the corresponding input image pixel. So, to determine the value of the pixel at (5,10) in the output image, nine pixels from the input image need to be considered: (4,9), (4,10), (4,11), (5,9), (5,10), (5,11), (6,9), (6,10), and (6,11). These nine input pixels are combined into a single binary number that is used as an index in the image enhancement algorithm string.

For example, to determine the output pixel that corresponds to the very middle pixel of the input image, the nine pixels marked by [...] would need to be considered:

# . . # .
# [. . .].
#[# . .]#
.[. # .].
. . # # #
#.., then .#.; combining these forms ...#...#.. By turning dark pixels (.) into 0 and light pixels (#) into 1, the binary number 000100010 can be formed, which is 34 in decimal.
Starting from the top-left and reading across each row, these pixels are ..., then

The image enhancement algorithm string is exactly 512 characters long, enough to match every possible 9-bit binary number. The first few characters of the string (numbered starting from zero) are as follows:

0         10        20        30  34    40        50        60        70
|         |         |         |   |     |         |         |         |
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
#. So, the output pixel in the center of the output image should be #, a light pixel.
In the middle of this first group of characters, the character at index 34 can be found:

This process can then be repeated to calculate every pixel of the output image.

Through advances in imaging technology, the images being operated on here are infinite in size. Every pixel of the infinite output image needs to be calculated exactly based on the relevant pixels of the input image. The small input image you have is only a small region of the actual infinite input image; the rest of the input image consists of dark pixels (.). For the purposes of the example, to save on space, only a portion of the infinite-sized input and output images will be shown.

The starting input image, therefore, looks something like this, with more dark pixels (.) extending forever in every direction not shown here:

...............
...............
...............
...............
...............
.....#..#......
.....#.........
.....##..#.....
.......#.......
.......###.....
...............
...............
...............
...............
...............
By applying the image enhancement algorithm to every pixel simultaneously, the following output image can be obtained:

...............
...............
...............
...............
.....##.##.....
....#..#.#.....
....##.#..#....
....####..#....
.....#..##.....
......##..#....
.......#.#.....
...............
...............
...............
...............
Through further advances in imaging technology, the above output image can also be used as an input image! This allows it to be enhanced a second time:

...............
...............
...............
..........#....
....#..#.#.....
...#.#...###...
...#...##.#....
...#.....#.#...
....#.#####....
.....#.#####...
......##.##....
.......###.....
...............
...............
...............
Truly incredible - now the small details are really starting to come through. After enhancing the original input image twice, 35 pixels are lit.

Start with the original input image and apply the image enhancement algorithm twice, being careful to account for the infinite size of the images. How many pixels are lit in the resulting image?


'''


input_filename = 'input20-1.txt'


class Grid:
    def __init__(self, grid_info, algo):
        self.padding_char = 0
        self.grid = grid_info
        self.algo = algo
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
    grid.step()
    grid.step()

    # return ocean.count_beacons()
    return grid.count_lights()


if __name__ == "__main__":
    result = main()
    print(result)  # 5065
