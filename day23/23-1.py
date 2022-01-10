'''
--- Day 23: Amphipod ---
A group of amphipods notice your fancy submarine and flag you down. "With such an impressive shell," one amphipod says, "surely you can help us with a question that has stumped our best scientists."

They go on to explain that a group of timid, stubborn amphipods live in a nearby burrow. Four types of amphipods live there: Amber (A), Bronze (B), Copper (C), and Desert (D). They live in a burrow that consists of a hallway and four side rooms. The side rooms are initially full of amphipods, and the hallway is initially empty.

They give you a diagram of the situation (your puzzle input), including locations of each amphipod (A, B, C, or D, each of which is occupying an otherwise open space), walls (#), and open space (.).

For example:

#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
The amphipods would like a method to organize every amphipod into side rooms so that each side room contains one type of amphipod and the types are sorted A-D going left to right, like this:

#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #########
Amphipods can move up, down, left, or right so long as they are moving into an unoccupied open space. Each type of amphipod requires a different amount of energy to move one step: Amber amphipods require 1 energy per step, Bronze amphipods require 10 energy, Copper amphipods require 100, and Desert ones require 1000. The amphipods would like you to find a way to organize the amphipods that requires the least total energy.

However, because they are timid and stubborn, the amphipods have some extra rules:

Amphipods will never stop on the space immediately outside any room. They can move into that space so long as they immediately continue moving. (Specifically, this refers to the four open spaces in the hallway that are directly above an amphipod starting position.)
Amphipods will never move from the hallway into a room unless that room is their destination room and that room contains no amphipods which do not also have that room as their own destination. If an amphipod's starting room is not its destination room, it can stay in that room until it leaves the room. (For example, an Amber amphipod will not move from the hallway into the right three rooms, and will only move into the leftmost room if that room is empty or if it only contains other Amber amphipods.)
Once an amphipod stops moving in the hallway, it will stay in that spot until it can move into a room. (That is, once any amphipod starts moving, any other amphipods currently in the hallway are locked in place and will not move again until they can move fully into a room.)
In the above example, the amphipods can be organized using a minimum of 12521 energy. One way to do this is shown below.

Starting configuration:

#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
One Bronze amphipod moves into the hallway, taking 4 steps and using 40 energy:

#############
#...B.......#
###B#C#.#D###
  #A#D#C#A#
  #########
The only Copper amphipod not in its side room moves there, taking 4 steps and using 400 energy:

#############
#...B.......#
###B#.#C#D###
  #A#D#C#A#
  #########
A Desert amphipod moves out of the way, taking 3 steps and using 3000 energy, and then the Bronze amphipod takes its place, taking 3 steps and using 30 energy:

#############
#.....D.....#
###B#.#C#D###
  #A#B#C#A#
  #########
The leftmost Bronze amphipod moves to its room using 40 energy:

#############
#.....D.....#
###.#B#C#D###
  #A#B#C#A#
  #########
Both amphipods in the rightmost room move into the hallway, using 2003 energy in total:

#############
#.....D.D.A.#
###.#B#C#.###
  #A#B#C#.#
  #########
Both Desert amphipods move into the rightmost room using 7000 energy:

#############
#.........A.#
###.#B#C#D###
  #A#B#C#D#
  #########
Finally, the last Amber amphipod moves into its room, using 8 energy:

#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #########
What is the least energy required to organize the amphipods?

'''
from queue import PriorityQueue

input_filename = 'input23-1.txt'

p_moves = [set() for _ in range(15)]  # set(to, spaces, blocked)
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
    # Add the deeper room
    additional_moves = set()
    for spot in p_move:
        to, spaces, blocked = spot
        blocked_copy = set(blocked)
        blocked_copy.add(to)
        additional_moves.add((to+4, spaces+1, tuple(blocked_copy)))
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
        if idx >= 11 and goal_state[idx] == crab:
            continue
        if 7 <= idx < 11 and goal_state[idx] == crab and state[idx+4] == goal_state[idx+4]:
            continue

        for move in location:
            to, spaces, blocked = move
            if state[to] != '.':
                continue

            if 7 <= to < 11 and (goal_state[to] != crab or state[to+4] != goal_state[to+4]):
                continue
            if 11 < to and goal_state[to] != crab:
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
    print()


def solve(initial_state):
    goal_state = '.......ABCDABCD'
    seen = set()
    to_visit = PriorityQueue()
    to_visit.put((0, initial_state, [initial_state]))
    while not to_visit.empty():
        energy, state, path = to_visit.get()
        if state == goal_state:
            for p in path:
                print_state(p)
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
    results += [input_data_raw[2][3], input_data_raw[2]
                [5], input_data_raw[2][7], input_data_raw[2][9]]
    results += [input_data_raw[3][3], input_data_raw[3]
                [5], input_data_raw[3][7], input_data_raw[3][9]]

    return ''.join(results)


def main():
    initial_state = parse_input(input_filename)
    return solve(initial_state)


if __name__ == "__main__":
    # import cProfile
    # cProfile.run('main()')
    result = main()
    print(result)  # 15111
