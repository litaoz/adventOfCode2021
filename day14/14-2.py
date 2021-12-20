'''
--- Part Two ---
The resulting polymer isn't nearly strong enough to reinforce the submarine. You'll need to run more steps of the pair insertion process; a total of 40 steps should do it.

In the above example, the most common element is B (occurring 2192039569602 times) and the least common element is H (occurring 3849876073 times); subtracting these produces 2188189693529.

Apply 40 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?
'''
from typing import Tuple

input_filename = 'input14-2.txt'


class Polymer:
    def __init__(self, polymer: str, rules: dict):
        self.polymer = polymer
        self.rules = rules
        self.pair_count = {}
        polymer_length = len(self.polymer)

        # Find pairs
        pairs = []
        for i in range(polymer_length - 1):
            pairs.append(self.polymer[i: i + 2])

        for pair in pairs:
            if pair in self.pair_count:
                self.pair_count[pair] += 1
            else:
                self.pair_count[pair] = 1

    def next_step(self):
        next_pair_count = {}
        for pair, count in self.pair_count.items():
            if pair in self.rules:
                elm = self.rules[pair]
                new_pairs = [f'{pair[0]}{elm}', f'{elm}{pair[1]}']
                for new_pair in new_pairs:
                    if new_pair in next_pair_count:
                        next_pair_count[new_pair] += count
                        continue
                    next_pair_count[new_pair] = count
                continue
            next_pair_count[pair] = count
        self.pair_count = next_pair_count

    def count_elements(self):
        elements = dict()
        for pair in self.pair_count:
            count = self.pair_count[pair]
            for char in pair:
                if char in elements:
                    elements[char] += count
                else:
                    elements[char] = count

        # All pairs are double counted except ends
        ends = [self.polymer[0], self.polymer[-1]]
        for char in ends:
            if char in elements:
                elements[char] += 1
            else:
                elements[char] = 1
                assert False  # should never happen

        for elem in elements:
            elements[elem] //= 2

        return elements

    def most_common_minus_least_common(self):
        elm_counts = self.count_elements()
        counts = [v for k, v in elm_counts.items()]
        most_common = max(counts)
        least_common = min(counts)
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
    steps = 40
    for _ in range(steps):
        polymer.next_step()
    return polymer.most_common_minus_least_common()


if __name__ == "__main__":
    result = main()
    print(result)  # 3459822539451
