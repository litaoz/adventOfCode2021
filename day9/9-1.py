'''
--- Day 9: Smoke Basin ---
These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678
Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

'''

from typing import List, Tuple
from itertools import permutations

input_filename = 'input9-1.txt'


def parse_input(input_filename) -> List[List[str]]:
    input_data_raw = []
    with open(input_filename) as f:
        input_data_raw = f.read().splitlines()

    height_map = []
    for row in input_data_raw:
        chars = [int(char) for char in row]
        height_map.append(chars)

    return height_map


def find_low_points(height_map) -> List[Tuple]:
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


def calculate_risk_level(height_map, points):
    risk_levels = []
    for point in points:
        r, c = point
        risk_level = height_map[r][c] + 1
        risk_levels.append(risk_level)
    return sum(risk_levels)


def main():
    height_map = parse_input(input_filename)
    low_points = find_low_points(height_map)
    risk_level = calculate_risk_level(height_map, low_points)
    return risk_level


if __name__ == "__main__":
    result = main()
    print(result)  # 342
