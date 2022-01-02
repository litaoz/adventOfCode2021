'''
--- Part Two ---
Sometimes, it's a good idea to appreciate just how big the ocean is. Using the Manhattan distance, how far apart do the scanners get?

In the above example, scanners 2 (1105,-1205,1229) and 3 (-92,-2380,-20) are the largest Manhattan distance apart. In total, they are 1197 + 1175 + 1249 = 3621 units apart.

What is the largest Manhattan distance between any two scanners?
'''

from itertools import permutations

input_filename = 'input19-1_test3.txt'


class Ocean:
    def __init__(self):
        self.scanners = []
        self.beacons = []

    def add(self, scanner_points_corrected):
        '''
        scanner_points = [('scanner x', (coord)), ('beacon', (coord)) ... ]
        '''
        scanner = self.get_scanner_from_scanner(scanner_points_corrected)
        beacons = self.get_beacons_from_scanner(scanner_points_corrected)

        self.scanners.append(scanner)
        self.beacons += beacons

    def largest_scanner_manhattan_distance(self):
        distances = []
        for scanner1 in self.scanners:
            for scanner2 in self.scanners:
                dist = self.manhattan_distance(scanner1, scanner2)
                distances.append(dist)
        return max(distances)

    def count_beacons(self):
        return len(self.beacons)

    def add_scanner_result(self, scanner_points) -> bool:
        known_beacon_neighbors = self.get_beacon_neighbors(self.beacons)
        new_beacons = self.get_beacons_from_scanner(scanner_points)
        new_beacon_neighbors = self.get_beacon_neighbors(new_beacons)

        def find_beacon_with_enough_common_neighbors(known_beacon_neighbors, new_beacon_neighbors):
            '''
            Returns None if no beacon with enough neighbors
            '''
            min_common_neighbors = 11
            for known_beacon in known_beacon_neighbors:
                for new_beacon in new_beacon_neighbors:
                    common_neighbors = known_beacon.keys() & new_beacon.keys()
                    if len(common_neighbors) >= min_common_neighbors:
                        return (known_beacon, new_beacon, common_neighbors)
            return None

        def new_neighbors(common_beacons, orientation):
            known_beacon_entry, new_beacon_entry, common_neighbors = common_beacons
            translation, rotation, reflection = orientation

            def reflect(point, reflection):
                return tuple([point_dim * reflection_dim for point_dim, reflection_dim in zip(point, reflection)])

            def rotate(point, rotation):
                for i, coord in enumerate(permutations(point)):
                    if i == rotation:
                        return tuple(coord)
                return -1

            def translate(point, translation):
                return tuple([dim[0] + dim[1] for dim in zip(point, translation)])

            def orient(point, orientation):
                translation, rotation, reflection = orientation
                new_point, known_point = translation
                point_init_trans = translate(point, new_point)
                point_rot = rotate(point_init_trans, rotation)
                point_ref = reflect(point_rot, reflection)
                point_final_trans = translate(point_ref, known_point)
                return point_final_trans

            # scanner_points = [('scanner x', (coord)), ('beacon', (coord)) ... ]
            unknown_neighbors = [new_beacon_entry[point][1]
                                 for point in new_beacon_entry if point not in common_neighbors]
            unknown_neighbors.insert(0, tuple([0 for _ in reflection]))
            unknown_neighbors = [orient(n, orientation)
                                 for n in unknown_neighbors]

            result = [('scanner', unknown_neighbors[0])]
            for n in unknown_neighbors[1:]:
                result.append(('beacon', n))
            return result

        def find_orientation(common_beacons):
            known_beacon_entry, new_beacon_entry, common_neighbors = common_beacons

            def back_translate(point, base):
                return tuple([dim[0] - dim[1] for dim in zip(point, base)])

            def num_rotation(point1, point2):
                point2_abs = tuple([abs(dim) for dim in point2])
                for i, coord in enumerate(permutations(point1)):
                    coord_abs = tuple([abs(dim) for dim in coord])
                    if coord_abs == point2_abs:
                        return i
                assert False, "No rotation found"

            def find_reflection(point1, point2, rotation):
                coord = tuple()
                for i, coord_rot in enumerate(permutations(point1)):
                    if i == rotation:
                        coord = coord_rot
                        break

                reflection = list()
                for coord_dim, point2_dim in zip(coord, point2):
                    if point2_dim == 0:
                        reflection.append(1)
                        continue
                    reflection.append(coord_dim // point2_dim)
                return tuple(reflection)

            translation = []
            rotations = []
            reflections = []
            for neighbor in common_neighbors:
                known_beacon = known_beacon_entry[neighbor][0]
                new_beacon = new_beacon_entry[neighbor][0]
                translation = tuple([-dim for dim in new_beacon])
                known_neighbor = known_beacon_entry[neighbor][1]
                new_neighbor = new_beacon_entry[neighbor][1]

                known_rel = back_translate(known_neighbor, known_beacon)
                new_rel = back_translate(new_neighbor, new_beacon)
                rotation = num_rotation(new_rel, known_rel)
                rotations.append(rotation)

                reflection = find_reflection(new_rel, known_rel, rotation)
                reflections.append(reflection)

            translation = tuple([translation, known_beacon])
            rotation = max(set(rotations), key=rotations.count)
            reflection = max(set(reflections), key=reflections.count)

            return (translation, rotation, reflection)

        # Find a point that shares enough neighbors with known
        common_beacons = find_beacon_with_enough_common_neighbors(
            known_beacon_neighbors, new_beacon_neighbors)

        if common_beacons is None:
            return False

        # Find orientation to add the unknown neighbors to the known
        orientation = find_orientation(common_beacons)

        # Correct orient of unknown neighbors
        unknown_neighbors = new_neighbors(common_beacons, orientation)

        # Add the unknown neighbors
        self.add(unknown_neighbors)

        return True

    def get_beacon_neighbors(self, beacons):
        # Private method to find neighbors
        beacon_neighbors = []
        for point in beacons:
            neighbors = dict()
            for neighbor in beacons:
                if point == neighbor:
                    continue
                euclidian_dist = self.euclidian_distance(point, neighbor)
                manhattan_dist = self.manhattan_distance(point, neighbor)
                key = (manhattan_dist, euclidian_dist)
                neighbors[key] = (point, neighbor)
            beacon_neighbors.append(neighbors)
        return beacon_neighbors

    def get_scanner_from_scanner(self, scanner_points):
        '''
        Private
        point = ('scanner x', (coord))
        '''
        return scanner_points[0][1]

    def get_beacons_from_scanner(self, scanner_points):
        '''
        Private
        Check if point is a beacon point
        point = ('beacon', (coord))
        '''
        return [point[1] for point in scanner_points if point[0] == 'beacon']

    def manhattan_distance(self, point1, point2):
        dims = zip(point1, point2)
        return sum([abs(dim[1] - dim[0]) for dim in dims])

    def euclidian_distance(self, point1, point2):
        dims = zip(point1, point2)
        return (sum([(dim[1] - dim[0])**2 for dim in dims]))**0.5


def parse_input(input_filename) -> list[list[tuple]]:
    input_data_raw = []
    with open(input_filename) as f:
        input_data_raw = f.read().strip().split('\n\n')

    def parse_group(group):
        group_split = group.split('\n')
        coords = [(group_split[0].strip('---').strip(), (0, 0, 0))]
        rows = group_split[1:]
        for row in rows:
            coord_str = row.split(',')
            coord = tuple([int(dim) for dim in coord_str])
            coords.append(('beacon', coord))
        return coords

    inputs = [parse_group(group) for group in input_data_raw]
    return inputs


def main():
    scanner_results = parse_input(input_filename)
    ocean = Ocean()
    scanner = scanner_results.pop(0)
    ocean.add(scanner)

    this_scanners = []
    next_scanners = scanner_results
    while len(next_scanners) > 0 and len(next_scanners) != len(this_scanners):
        this_scanners = next_scanners
        next_scanners = []
        for scanner in this_scanners:
            if ocean.add_scanner_result(scanner):
                continue
            next_scanners.append(scanner)
    assert len(next_scanners) == 0, "Not all scanners were added"

    # return ocean.count_beacons()
    return ocean.largest_scanner_manhattan_distance()


if __name__ == "__main__":
    result = main()
    print(result)  # 12166
