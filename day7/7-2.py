'''
--- Day 7: The Treachery of Whales ---
A giant whale has decided your submarine is its next meal, and it's much faster than you are. There's nowhere to run!

Suddenly, a swarm of crabs (each in its own tiny submarine - it's too deep for them otherwise) zooms in to rescue you! They seem to be preparing to blast a hole in the ocean floor; sensors indicate a massive underground cave system just beyond where they're aiming!

The crab submarines all need to be aligned before they'll have enough power to blast a large enough hole for your submarine to get through. However, it doesn't look like they'll be aligned before the whale catches you! Maybe you can help?

There's one major catch - crab submarines can only move horizontally.

You quickly make a list of the horizontal position of each crab (your puzzle input). Crab submarines have limited fuel, so you need to find a way to make all of their horizontal positions match while requiring them to spend as little fuel as possible.

For example, consider the following horizontal positions:

16,1,2,0,4,2,7,1,2,14
This means there's a crab with horizontal position 16, a crab with horizontal position 1, and so on.

Each change of 1 step in horizontal position of a single crab costs 1 fuel. You could choose any horizontal position to align them all on, but the one that costs the least fuel is horizontal position 2:

Move from 16 to 2: 14 fuel
Move from 1 to 2: 1 fuel
Move from 2 to 2: 0 fuel
Move from 0 to 2: 2 fuel
Move from 4 to 2: 2 fuel
Move from 2 to 2: 0 fuel
Move from 7 to 2: 5 fuel
Move from 1 to 2: 1 fuel
Move from 2 to 2: 0 fuel
Move from 14 to 2: 12 fuel
This costs a total of 37 fuel. This is the cheapest possible outcome; more expensive outcomes include aligning at position 1 (41 fuel), position 3 (39 fuel), or position 10 (71 fuel).

Determine the horizontal position that the crabs can align to using the least fuel possible. How much fuel must they spend to align to that position?

'''
import statistics
import math
from typing import List, Tuple

input_filename = 'input7-2.txt'


def parse_input(input_filename) -> List[int]:
    input_data_raw = []
    with open(input_filename) as f:
        input_data_raw = f.read().splitlines()
    crabs = input_data_raw[0].split(',')
    crabs = [int(crab) for crab in crabs]
    return crabs


def travel_cost(crabs, position):
    travel = []
    for crab_pos in crabs:
        distance = abs(crab_pos - position)
        fuel = distance * (distance + 1) / 2
        travel.append(fuel)
    return sum(travel)


def main():
    crabs = parse_input(input_filename)
    mean = statistics.mean(crabs)
    possible_min_positions = []
    possible_min_positions.append(travel_cost(crabs, math.floor(mean)))
    possible_min_positions.append(travel_cost(crabs, math.ceil(mean)))
    return min(possible_min_positions)


if __name__ == "__main__":
    result = main()
    print(int(result))  # 94004208
