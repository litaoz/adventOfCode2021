'''
--- Part Two ---
Through a little deduction, you should now be able to determine the remaining digits. Consider again the first example above:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf
After some careful analysis, the mapping between signal wires and segments only make sense in the following configuration:

 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc
So, the unique signal patterns would correspond to the following digits:

acedgfb: 8
cdfbe: 5
gcdfa: 2
fbcad: 3
dab: 7
cefabd: 9
cdfgeb: 6
eafb: 4
cagedb: 0
ab: 1
Then, the four digits of the output value can be decoded:

cdfeb: 5
fcadb: 3
cdfeb: 5
cdbaf: 3
Therefore, the output value for this entry is 5353.

Following this same process for each entry in the second, larger example above, the output value of each entry can be determined:

fdgacbe cefdb cefbgd gcbe: 8394
fcgedb cgb dgebacf gc: 9781
cg cg fdcagb cbg: 1197
efabcd cedba gadfec cb: 9361
gecf egdcabf bgf bfgea: 4873
gebdcfa ecba ca fadegcb: 8418
cefg dcbef fcge gbcadfe: 4548
ed bcgafe cdgba cbgef: 1625
gbdfcae bgc cg cgb: 8717
fgae cfgab fg bagce: 4315
Adding all of the output values in this larger example produces 61229.

For each entry, determine all of the wire/segment connections and decode the four-digit output values. What do you get if you add up all of the output values?

'''

from typing import List, Tuple
from itertools import permutations

input_filename = 'input8-2.txt'

number_def = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}


def parse_input(input_filename) -> List[Tuple[List[str], List[str]]]:
    input_data_raw = []
    with open(input_filename) as f:
        input_data_raw = f.read().splitlines()

    displays = []
    for row in input_data_raw:
        observations_raw, output_raw = row.split('|')
        observations = observations_raw.split()
        output = output_raw.split()
        displays.append((observations, output))

    return displays


def valid_mapping(observations: List[str], mapping: Tuple[str]):
    mapped_observations = set(map_display(observations, mapping))
    for num in number_def:
        if num not in mapped_observations:
            return False
    return True


def map_display(display: List[str], mapping: Tuple[str]) -> List[str]:
    mapping_str = ''.join(mapping)
    transTable = str.maketrans('abcdefg', mapping_str)
    result = []
    for num_str in display:
        translated_num_str = num_str.translate(transTable)
        sorted_num_str = ''.join(sorted(translated_num_str))
        result.append(sorted_num_str)
    return result


def interpret_output(mapped_output: List[str]) -> List[int]:
    result = [number_def[digit_str] for digit_str in mapped_output]
    return result


def solve_display(display) -> List[int]:
    observations, output = display
    for mapping in permutations(['a', 'b', 'c', 'd', 'e', 'f', 'g']):
        if valid_mapping(observations, mapping):
            mapped_output = map_display(output, mapping)
            return interpret_output(mapped_output)


def main():
    displays = parse_input(input_filename)
    displayed_numbers = [solve_display(display) for display in displays]

    results = []
    for solution in displayed_numbers:
        solution_digits_str = [str(digit) for digit in solution]
        number_str = ''.join(solution_digits_str)
        results.append(int(number_str))
    return sum(results)


if __name__ == "__main__":
    result = main()
    print(result)  # 342
