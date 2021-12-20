'''
--- Day 15: Chiton ---
You've almost reached the exit of the cave, but the walls are getting closer together. Your submarine can barely still fit, though; the main problem is that the walls of the cave are covered in chitons, and it would be best not to bump any of them.

The cavern is large, but has a very low ceiling, restricting your motion to two dimensions. The shape of the cavern resembles a square; a quick scan of chiton density produces a map of risk level throughout the cave (your puzzle input). For example:

1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
You start in the top left position, your destination is the bottom right position, and you cannot move diagonally. The number at each position is its risk level; to determine the total risk of an entire path, add up the risk levels of each position you enter (that is, don't count the risk level of your starting position unless you enter it; leaving it adds no risk to your total).

Your goal is to find a path with the lowest total risk. In this example, a path with the lowest total risk is highlighted here:

1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
The total risk of this path is 40 (the starting position is never entered, so its risk is not counted).

What is the lowest total risk of any path from the top left to the bottom right?
'''
from typing import Tuple
from queue import PriorityQueue

input_filename = 'input15-1.txt'


class Cave:
    def __init__(self, grid: list[list[int]]):
        self.grid = grid
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def find_best_path(self) -> list[Tuple]:
        values = dict()
        start = (0, 0)
        end = (self.height - 1, self.width - 1)
        risk = 0

        to_visit = PriorityQueue()
        to_visit.put((risk, start, [start]))
        while not to_visit.empty():
            current_risk, node, path = to_visit.get()

            if node in values and values[node] <= current_risk:
                # Found a higher risk path to the same place
                continue
            if node == end:
                return current_risk

            values[node] = current_risk

            # Add neighbors to to_visit
            neighbors = self.find_neighbors(node)
            for neighbor in neighbors:
                n_r, n_c = neighbor
                n_path = path + [neighbor]
                n_risk = current_risk + self.grid[n_r][n_c]
                to_visit.put((n_risk, neighbor, n_path))

    def find_neighbors(self, point) -> list[Tuple]:
        height = len(self.grid)
        width = len(self.grid[0])
        r, c = point

        neighbor_rel_coords = []
        for r_rel in [-1, 0, 1]:
            for c_rel in [-1, 0, 1]:

                # skip itself
                if r_rel == 0 and c_rel == 0:
                    continue

                # skip diagonals
                if r_rel != 0 and c_rel != 0:
                    continue

                neighbor_rel_coords.append((r_rel, c_rel))

        neighbors = []
        for rel_coord in neighbor_rel_coords:
            r_rel, c_rel = rel_coord
            r_neighbor = r + r_rel
            c_neighbor = c + c_rel
            if 0 <= r_neighbor < height and 0 <= c_neighbor < width:
                neighbors.append((r_neighbor, c_neighbor))

        return neighbors


def parse_input(input_filename) -> Tuple[str, dict]:
    input_data_raw = []
    with open(input_filename) as f:
        input_data_raw = f.read().splitlines()

    grid = []
    for row in input_data_raw:
        grid.append([int(char) for char in row])

    return grid


def main():
    grid = parse_input(input_filename)
    cave = Cave(grid)
    return cave.find_best_path()


if __name__ == "__main__":
    # import cProfile
    # cProfile.run('main()')
    result = main()
    print(result)  #
