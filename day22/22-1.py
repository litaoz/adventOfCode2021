'''
--- Day 22: Reactor Reboot ---
Operating at these extreme ocean depths has overloaded the submarine's reactor; it needs to be rebooted.

The reactor core is made up of a large 3-dimensional grid made up entirely of cubes, one cube per integer 3-dimensional coordinate (x,y,z). Each cube can be either on or off; at the start of the reboot process, they are all off. (Could it be an old model of a reactor you've seen before?)

To reboot the reactor, you just need to set all of the cubes to either on or off by following a list of reboot steps (your puzzle input). Each step specifies a cuboid (the set of all cubes that have coordinates which fall within ranges for x, y, and z) and whether to turn all of the cubes in that cuboid on or off.

For example, given these reboot steps:

on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11
on x=10..10,y=10..10,z=10..10
The first step (on x=10..12,y=10..12,z=10..12) turns on a 3x3x3 cuboid consisting of 27 cubes:

10,10,10
10,10,11
10,10,12
10,11,10
10,11,11
10,11,12
10,12,10
10,12,11
10,12,12
11,10,10
11,10,11
11,10,12
11,11,10
11,11,11
11,11,12
11,12,10
11,12,11
11,12,12
12,10,10
12,10,11
12,10,12
12,11,10
12,11,11
12,11,12
12,12,10
12,12,11
12,12,12
The second step (on x=11..13,y=11..13,z=11..13) turns on a 3x3x3 cuboid that overlaps with the first. As a result, only 19 additional cubes turn on; the rest are already on from the previous step:

11,11,13
11,12,13
11,13,11
11,13,12
11,13,13
12,11,13
12,12,13
12,13,11
12,13,12
12,13,13
13,11,11
13,11,12
13,11,13
13,12,11
13,12,12
13,12,13
13,13,11
13,13,12
13,13,13
The third step (off x=9..11,y=9..11,z=9..11) turns off a 3x3x3 cuboid that overlaps partially with some cubes that are on, ultimately turning off 8 cubes:

10,10,10
10,10,11
10,11,10
10,11,11
11,10,10
11,10,11
11,11,10
11,11,11
The final step (on x=10..10,y=10..10,z=10..10) turns on a single cube, 10,10,10. After this last step, 39 cubes are on.

The initialization procedure only uses cubes that have x, y, and z positions of at least -50 and at most 50. For now, ignore cubes outside this region.

Here is a larger example:

on x=-20..26,y=-36..17,z=-47..7
on x=-20..33,y=-21..23,z=-26..28
on x=-22..28,y=-29..23,z=-38..16
on x=-46..7,y=-6..46,z=-50..-1
on x=-49..1,y=-3..46,z=-24..28
on x=2..47,y=-22..22,z=-23..27
on x=-27..23,y=-28..26,z=-21..29
on x=-39..5,y=-6..47,z=-3..44
on x=-30..21,y=-8..43,z=-13..34
on x=-22..26,y=-27..20,z=-29..19
off x=-48..-32,y=26..41,z=-47..-37
on x=-12..35,y=6..50,z=-50..-2
off x=-48..-32,y=-32..-16,z=-15..-5
on x=-18..26,y=-33..15,z=-7..46
off x=-40..-22,y=-38..-28,z=23..41
on x=-16..35,y=-41..10,z=-47..6
off x=-32..-23,y=11..30,z=-14..3
on x=-49..-5,y=-3..45,z=-29..18
off x=18..30,y=-20..-8,z=-3..13
on x=-41..9,y=-7..43,z=-33..15
on x=-54112..-39298,y=-85059..-49293,z=-27449..7877
on x=967..23432,y=45373..81175,z=27513..53682
The last two steps are fully outside the initialization procedure area; all other steps are fully within it. After executing these steps in the initialization procedure region, 590784 cubes are on.

Execute the reboot steps. Afterward, considering only cubes in the region x=-50..50,y=-50..50,z=-50..50, how many cubes are on?

'''


input_filename = 'input22-2_test4.txt'


def count_on(grid):
    count = 0
    for i in grid.values():
        for j in i.values():
            for k in j.values():
                if k == 1:
                    count += 1
    return count


def do_operation(grid, operation):
    min_x, max_x = -50, 50
    min_y, max_y = -50, 50
    min_z, max_z = -50, 50

    op, x_range, y_range, z_range = operation
    x_range_min, x_range_max = x_range
    y_range_min, y_range_max = y_range
    z_range_min, z_range_max = z_range

    if x_range_max < min_x or max_x < x_range_min:
        return
    if y_range_max < min_y or max_y < y_range_min:
        return
    if z_range_max < min_z or max_z < z_range_min:
        return

    for i in range(x_range_min, x_range_max + 1):
        for j in range(y_range_min, y_range_max + 1):
            for k in range(z_range_min, z_range_max + 1):
                if min_x <= i <= max_x and min_y <= j <= max_y and min_z <= k <= max_z:
                    grid[i][j][k] = op


def parse_input(input_filename):
    input_data_raw = []
    with open(input_filename) as f:
        input_data_raw = f.read().strip().split('\n')

    op_map = {'on': 1, 'off': 0}
    results = []
    for row in input_data_raw:
        op, ranges = row.split(' ')
        x, y, z = ranges.split(',')
        x_range = x.strip('x=').split('..')
        y_range = y.strip('y=').split('..')
        z_range = z.strip('z=').split('..')
        x_range = [int(i) for i in x_range]
        y_range = [int(i) for i in y_range]
        z_range = [int(i) for i in z_range]
        results.append((op_map[op], x_range, y_range, z_range))

    return results


def main():
    operations = parse_input(input_filename)
    grid = {i: {j: {k: 0 for k in range(-50, 51)}
                for j in range(-50, 51)} for i in range(-50, 51)}
    for operation in operations:
        do_operation(grid, operation)
    return count_on(grid)


if __name__ == "__main__":
    result = main()
    print(result)  # 564654
