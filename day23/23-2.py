'''
--- Part Two ---
As you prepare to give the amphipods your solution, you notice that the diagram they handed you was actually folded up. As you unfold it, you discover an extra part of the diagram.

Between the first and second lines of text that contain amphipod starting positions, insert the following lines:

  #D#C#B#A#
  #D#B#A#C#
So, the above example now becomes:

#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########
The amphipods still want to be organized into rooms similar to before:

#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########
In this updated example, the least energy required to organize these amphipods is 44169:

#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#..........D#
###B#C#B#.###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#A.........D#
###B#C#B#.###
  #D#C#B#.#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#A........BD#
###B#C#.#.###
  #D#C#B#.#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#A......B.BD#
###B#C#.#.###
  #D#C#.#.#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#AA.....B.BD#
###B#C#.#.###
  #D#C#.#.#
  #D#B#.#C#
  #A#D#C#A#
  #########

#############
#AA.....B.BD#
###B#.#.#.###
  #D#C#.#.#
  #D#B#C#C#
  #A#D#C#A#
  #########

#############
#AA.....B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#B#C#C#
  #A#D#C#A#
  #########

#############
#AA...B.B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#.#C#C#
  #A#D#C#A#
  #########

#############
#AA.D.B.B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#.#C#C#
  #A#.#C#A#
  #########

#############
#AA.D...B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#.#C#C#
  #A#B#C#A#
  #########

#############
#AA.D.....BD#
###B#.#.#.###
  #D#.#C#.#
  #D#B#C#C#
  #A#B#C#A#
  #########

#############
#AA.D......D#
###B#.#.#.###
  #D#B#C#.#
  #D#B#C#C#
  #A#B#C#A#
  #########

#############
#AA.D......D#
###B#.#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#A#
  #########

#############
#AA.D.....AD#
###B#.#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#.#
  #########

#############
#AA.......AD#
###B#.#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#D#
  #########

#############
#AA.......AD#
###.#B#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#D#
  #########

#############
#AA.......AD#
###.#B#C#.###
  #.#B#C#.#
  #D#B#C#D#
  #A#B#C#D#
  #########

#############
#AA.D.....AD#
###.#B#C#.###
  #.#B#C#.#
  #.#B#C#D#
  #A#B#C#D#
  #########

#############
#A..D.....AD#
###.#B#C#.###
  #.#B#C#.#
  #A#B#C#D#
  #A#B#C#D#
  #########

#############
#...D.....AD#
###.#B#C#.###
  #A#B#C#.#
  #A#B#C#D#
  #A#B#C#D#
  #########

#############
#.........AD#
###.#B#C#.###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########

#############
#..........D#
###A#B#C#.###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########

#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########
Using the initial configuration from the full diagram, what is the least energy required to organize the amphipods?

'''
from queue import PriorityQueue

input_filename = 'input23-2.txt'

p_moves = [set() for _ in range(23)]  # set(to, spaces, blocked)
p_moves[0] = {(7, 3, tuple([1])), (8, 5, tuple([1, 2])),
              (9, 7, tuple([1, 2, 3])), (10, 9, tuple([1, 2, 3, 4]))}
p_moves[1] = {(7, 2, tuple()), (8, 4, tuple([2])),
              (9, 6, tuple([2, 3])), (10, 8, tuple([2, 3, 4]))}
p_moves[2] = {(7, 2, tuple()), (8, 2, tuple()),
              (9, 4, tuple([3])), (10, 6, tuple([3, 4]))}
p_moves[3] = {(7, 4, tuple([2])), (8, 2, tuple()),
              (9, 2, tuple()), (10, 4, tuple([4]))}
p_moves[4] = {(7, 6, tuple([2, 3])), (8, 4, tuple([3])),
              (9, 2, tuple([])), (10, 2, tuple([]))}
p_moves[5] = {(7, 8, tuple([2, 3, 4])), (8, 6, tuple([3, 4])),
              (9, 4, tuple([4])), (10, 2, tuple([]))}
p_moves[6] = {(7, 9, tuple([2, 3, 4, 5])), (8, 7, tuple([3, 4, 5])),
              (9, 5, tuple([4, 5])), (10, 3, tuple([5]))}

for idx, p_move in enumerate(p_moves[:7]):
    # Add the deeper rooms
    additional_moves = set()
    for spot in p_move:
        for i in range(3):
            to, spaces, blocked = spot
            blocked_copy = set(blocked)
            blocked_copy.update(range(to, to+4*(i+1), 4))
            additional_moves.add(
                (to+4*(i+1), spaces+1*(i+1), tuple(blocked_copy)))
    p_move.update(additional_moves)

    # Reflect the other moves for rooms to hallway
    for spot in p_move:
        to, spaces, blocked = spot
        p_moves[to].add((idx, spaces, blocked))


def available_moves(energy, state, path, goal_state):
    energy_table = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
    next_states = []
    for idx, location in enumerate(p_moves):
        crab = state[idx]
        if crab == '.':
            continue

        if 7 <= idx < 11 and goal_state[idx] == crab \
                and state[idx+4] == goal_state[idx+4]\
                and state[idx+8] == goal_state[idx+8]\
                and state[idx+12] == goal_state[idx+12]:
            continue
        if 11 <= idx < 15 and goal_state[idx] == crab \
                and state[idx+4] == goal_state[idx+4]\
                and state[idx+8] == goal_state[idx+8]:
            continue
        if 15 <= idx < 17 and goal_state[idx] == crab \
                and state[idx+4] == goal_state[idx+4]:
            continue
        if 17 <= idx < 23 and goal_state[idx] == crab:
            continue

        for move in location:
            to, spaces, blocked = move
            if state[to] != '.':
                continue

            if 7 <= to < 23 and goal_state[to] != crab:
                continue
            if 7 <= to < 11 and (state[to+4] != goal_state[to+4]
                                 or state[to+8] != goal_state[to+8]
                                 or state[to+12] != goal_state[to+12]):
                continue
            if 11 <= to < 15 and (state[to+4] != goal_state[to+4]
                                  or state[to+8] != goal_state[to+8]):
                continue
            if 15 <= to < 17 and (state[to+4] != goal_state[to+4]):
                continue

            blocked_spaces = [state[block] != '.' for block in blocked]
            if any(blocked_spaces):
                continue
            new_energy = energy + energy_table[crab] * spaces
            new_state = list(state)
            new_state[idx], new_state[to] = new_state[to], new_state[idx]
            new_state = ''.join(new_state)
            new_path = path.copy()
            new_path.append(new_state)
            next_states.append((new_energy, new_state, new_path))
    return next_states
    # list[(energy, state, path)]


def print_state(state):
    s = state
    print(f'{s[0]}{s[1]}.{s[2]}.{s[3]}.{s[4]}.{s[5]}{s[6]}')
    print(f'  {s[7]} {s[8]} {s[9]} {s[10]}')
    print(f'  {s[11]} {s[12]} {s[13]} {s[14]}')
    print(f'  {s[15]} {s[16]} {s[17]} {s[18]}')
    print(f'  {s[19]} {s[20]} {s[21]} {s[22]}')
    print()


def solve(initial_state):
    goal_state = '.......ABCDABCDABCDABCD'
    seen = set()
    to_visit = PriorityQueue()
    to_visit.put((0, initial_state, [initial_state]))
    while not to_visit.empty():
        energy, state, path = to_visit.get()
        if state == goal_state:
            # for p in path:
            #     print_state(p)
            return energy
        if state in seen:
            continue
        seen.add(state)
        # print(energy, end='\r')
        # print(energy)
        # print_state(state)
        moves = available_moves(energy, state, path, goal_state)
        for move in moves:
            to_visit.put(move)


def parse_input(input_filename):
    input_data_raw = []
    with open(input_filename) as f:
        input_data_raw = f.read().strip().split('\n')

    results = [input_data_raw[1][1], input_data_raw[1][2], input_data_raw[1][4],
               input_data_raw[1][6], input_data_raw[1][8],
               input_data_raw[1][10], input_data_raw[1][11]]

    for i in range(4):
        results += [input_data_raw[2+i][3], input_data_raw[2+i]
                    [5], input_data_raw[2+i][7], input_data_raw[2+i][9]]

    return ''.join(results)


def main():
    initial_state = parse_input(input_filename)
    return solve(initial_state)


if __name__ == "__main__":
    # import cProfile
    # cProfile.run('main()')
    result = main()
    print(result)  # 15111
