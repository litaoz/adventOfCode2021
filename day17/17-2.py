'''
--- Part Two ---
Maybe a fancy trick shot isn't the best idea; after all, you only have one probe, so you had better not miss.

To get the best idea of what your options are for launching the probe, you need to find every initial velocity that causes the probe to eventually be within the target area after any step.

In the above example, there are 112 different initial velocity values that meet these criteria:

23,-10  25,-9   27,-5   29,-6   22,-6   21,-7   9,0     27,-7   24,-5
25,-7   26,-6   25,-5   6,8     11,-2   20,-5   29,-10  6,3     28,-7
8,0     30,-6   29,-8   20,-10  6,7     6,4     6,1     14,-4   21,-6
26,-10  7,-1    7,7     8,-1    21,-9   6,2     20,-7   30,-10  14,-3
20,-8   13,-2   7,3     28,-8   29,-9   15,-3   22,-5   26,-8   25,-8
25,-6   15,-4   9,-2    15,-2   12,-2   28,-9   12,-3   24,-6   23,-7
25,-10  7,8     11,-3   26,-7   7,1     23,-9   6,0     22,-10  27,-6
8,1     22,-8   13,-4   7,6     28,-6   11,-4   12,-4   26,-9   7,4
24,-10  23,-8   30,-8   7,0     9,-1    10,-1   26,-5   22,-9   6,5
7,5     23,-6   28,-10  10,-2   11,-1   20,-9   14,-2   29,-7   13,-3
23,-5   24,-8   27,-9   30,-7   28,-5   21,-10  7,9     6,6     21,-5
27,-10  7,2     30,-9   21,-8   22,-7   24,-9   20,-6   6,9     29,-5
8,-2    27,-8   30,-5   24,-7
How many distinct initial velocity values cause the probe to be within the target area after any step?
'''

from typing import Tuple
import math

input_filename = 'input17-2.txt'


def parse_input(input_filename) -> Tuple[str, dict]:
    input_data_raw = []
    with open(input_filename) as f:
        input_data_raw = f.read().splitlines()

    removed_prefix = input_data_raw[0].strip('target area: ')

    # Parse x
    x_range_str, y_range_str = removed_prefix.split(', ')
    x_range_str = x_range_str.strip('x=')
    x_range_list = x_range_str.split('..')
    x_range = tuple([int(x) for x in x_range_list])

    # Parse y
    y_range_str = y_range_str.strip('y=')
    y_range_list = y_range_str.split('..')
    y_range = tuple([int(x) for x in y_range_list])
    return (x_range, y_range)


def solve_max_y_vel(target_area):
    x_range, y_range = target_area
    y_min, y_max = y_range
    return -(y_min) - 1


def solve_max_x_vel(target_area):
    x_range, y_range = target_area
    x_min, x_max = x_range
    return x_max


def next_step(x, y, x_vel, y_vel):
    x += x_vel
    assert x_vel >= 0
    if x_vel != 0:
        x_vel -= 1

    y += y_vel
    y_vel -= 1

    return (x, y, x_vel, y_vel)


def hits_target_area(target_area, vel_init):
    max_step = 1000
    x_range, y_range = target_area
    x_min, x_max = x_range
    y_min, y_max = y_range

    x, y = 0, 0
    x_vel, y_vel = vel_init
    for _ in range(max_step):
        x, y, x_vel, y_vel = next_step(x, y, x_vel, y_vel)
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return True
        if x > x_max or y < y_min:
            return False
    assert False


def find_possible_vels(target_area):
    max_x_vel = solve_max_x_vel(target_area)
    max_y_vel = solve_max_y_vel(target_area) + 1  # +1 for range inclusion

    vels = []
    for x_vel in range(max_x_vel + 1):
        for y_vel in range(-max_y_vel, max_y_vel):
            if hits_target_area(target_area, (x_vel, y_vel)):
                vels.append((x_vel, y_vel))

    return vels


def main():
    target_area = parse_input(input_filename)
    vels = find_possible_vels(target_area)
    return len(vels)


if __name__ == "__main__":
    result = main()
    print(result)  # 2118
