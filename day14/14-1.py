'''
--- Day 14: Extended Polymerization ---
The incredible pressures at this depth are starting to put a strain on your submarine. The submarine has polymerization equipment that would produce suitable materials to reinforce the submarine, and the nearby volcanically-active caves should even have the necessary input elements in sufficient quantities.

The submarine manual contains instructions for finding the optimal polymer formula; specifically, it offers a polymer template and a list of pair insertion rules (your puzzle input). You just need to work out what polymer would result after repeating the pair insertion process a few times.

For example:

NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
The first line is the polymer template - this is the starting point of the process.

The following section defines the pair insertion rules. A rule like AB -> C means that when elements A and B are immediately adjacent, element C should be inserted between them. These insertions all happen simultaneously.

So, starting with the polymer template NNCB, the first step simultaneously considers all three pairs:

The first pair (NN) matches the rule NN -> C, so element C is inserted between the first N and the second N.
The second pair (NC) matches the rule NC -> B, so element B is inserted between the N and the C.
The third pair (CB) matches the rule CB -> H, so element H is inserted between the C and the B.
Note that these pairs overlap: the second element of one pair is the first element of the next pair. Also, because all pairs are considered simultaneously, inserted elements are not considered to be part of a pair until the next step.

After the first step of this process, the polymer becomes NCNBCHB.

Here are the results of a few steps using the above rules:

Template:     NNCB
After step 1: NCNBCHB
After step 2: NBCCNBBBCBHCB
After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
This polymer grows quickly. After step 5, it has length 97; After step 10, it has length 3073. After step 10, B occurs 1749 times, C occurs 298 times, H occurs 161 times, and N occurs 865 times; taking the quantity of the most common element (B, 1749) and subtracting the quantity of the least common element (H, 161) produces 1749 - 161 = 1588.

Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?
'''
from typing import Tuple
from collections import Counter

input_filename = 'input14-1.txt'


class Polymer:
    def __init__(self, polymer: str, rules: dict):
        self.polymer = polymer
        self.rules = rules

    def print(self):
        print(self.polymer)

    def next_step(self):
        polymer_length = len(self.polymer)

        # Find pairs
        pairs = []
        for i in range(polymer_length - 1):
            pairs.append(self.polymer[i: i + 2])

        # Determine next_polymer
        next_polymer = []
        for pair in pairs:
            if pair in self.rules:
                element = self.rules[pair]
                sequence = f'{pair[0]}{element}'
                next_polymer.append(sequence)
            else:
                next_polymer.append(pair[0])
        next_polymer.append(self.polymer[-1])
        self.polymer = ''.join(next_polymer)

    def count_elements(self):
        elements = [char for char in self.polymer]
        return Counter(elements)

    def most_common_minus_least_common(self):
        counts = self.count_elements()
        most_common = counts.most_common()[0][1]
        least_common = counts.most_common()[-1][1]
        return most_common - least_common


def parse_input(input_filename) -> Tuple[str, dict]:
    input_data_raw = []
    with open(input_filename) as f:
        input_data_raw = f.read().splitlines()

    polymer_template = input_data_raw[0]

    insertion_rules = dict()
    for row in input_data_raw[2:]:
        pair, element = row.split(' -> ')
        insertion_rules[pair] = element

    return polymer_template, insertion_rules


def main():
    polymer_template, insertion_rules = parse_input(input_filename)
    polymer = Polymer(polymer_template, insertion_rules)
    steps = 10
    for _ in range(steps):
        polymer.next_step()
    return polymer.most_common_minus_least_common()


if __name__ == "__main__":
    result = main()
    print(result)  # 3009
