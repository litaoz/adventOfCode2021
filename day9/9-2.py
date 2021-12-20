'''
--- Part Two ---
Next, you need to find the largest basins so you know what areas are most important to avoid.

A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

The top-left basin, size 3:

2199943210
3987894921
9856789892
8767896789
9899965678
The top-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
The middle basin, size 14:

2199943210
3987894921
9856789892
8767896789
9899965678
The bottom-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?

'''

from typing import List, Tuple
from collections import deque

input_filename = 'input9-2.txt'


def parse_input(input_filename) -> List[List[str]]:
    input_data_raw = []
    with open(input_filename) as f:
        input_data_raw = f.read().splitlines()

    height_map = []
    for row in input_data_raw:
        chars = [int(char) for char in row]
        height_map.append(chars)

    return height_map


def find_low_points(height_map) -> List[Tuple[int, int]]:
    height = len(height_map)
    width = len(height_map[0])

    low_points = []
    for r, row in enumerate(height_map):
        for c, col in enumerate(row):
            neighbors = []
            if r > 0:  # up
                neighbors.append(height_map[r-1][c])
            if r < height - 1:  # down
                neighbors.append(height_map[r+1][c])
            if c > 0:  # left
                neighbors.append(height_map[r][c-1])
            if c < width - 1:  # right
                neighbors.append(height_map[r][c+1])

            comparisons = [col < neighbor for neighbor in neighbors]
            if all(comparisons):
                low_points.append((r, c))

    return low_points


def find_neighbors(height_map, r, c):
    height = len(height_map)
    width = len(height_map[0])
    neighbors = []
    if r > 0:  # up
        neighbors.append((r-1, c))
    if r < height - 1:  # down
        neighbors.append((r+1, c))
    if c > 0:  # left
        neighbors.append((r, c-1))
    if c < width - 1:  # right
        neighbors.append((r, c+1))
    return neighbors


def find_basin_size(height_map, low_point):
    visited = set()
    q = deque()
    count = 0

    q.append(low_point)
    while len(q) > 0:
        point = q.popleft()
        r, c = point
        if point in visited or height_map[r][c] == 9:
            continue
        visited.add(point)
        count += 1
        neighbors = find_neighbors(height_map, r, c)
        for neighbor in neighbors:
            q.append(neighbor)
    return count


def find_basin_sizes(height_map) -> List[int]:
    low_points = find_low_points(height_map)
    basin_sizes = [find_basin_size(height_map, low_point)
                   for low_point in low_points]
    return basin_sizes


def main():
    height_map = parse_input(input_filename)
    basin_sizes = sorted(find_basin_sizes(height_map), reverse=True)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


if __name__ == "__main__":
    result = main()
    print(result)  # 1235430
