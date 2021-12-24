'''
--- Day 18: Snailfish ---
You descend into the ocean trench and encounter some snailfish. They say they saw the sleigh keys! They'll even tell you which direction the keys went if you help one of the smaller snailfish with his math homework.

Snailfish numbers aren't like regular numbers. Instead, every snailfish number is a pair - an ordered list of two elements. Each element of the pair can be either a regular number or another pair.

Pairs are written as [x,y], where x and y are the elements within the pair. Here are some example snailfish numbers, one snailfish number per line:

[1,2]
[[1,2],3]
[9,[8,7]]
[[1,9],[8,5]]
[[[[1,2],[3,4]],[[5,6],[7,8]]],9]
[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]
This snailfish homework is about addition. To add two snailfish numbers, form a pair from the left and right parameters of the addition operator. For example, [1,2] + [[3,4],5] becomes [[1,2],[[3,4],5]].

There's only one problem: snailfish numbers must always be reduced, and the process of adding two snailfish numbers can result in snailfish numbers that need to be reduced.

To reduce a snailfish number, you must repeatedly do the first action in this list that applies to the snailfish number:

If any pair is nested inside four pairs, the leftmost such pair explodes.
If any regular number is 10 or greater, the leftmost such regular number splits.
Once no action in the above list applies, the snailfish number is reduced.

During reduction, at most one action applies, after which the process returns to the top of the list of actions. For example, if split produces a pair that meets the explode criteria, that pair explodes before other splits occur.

To explode a pair, the pair's left value is added to the first regular number to the left of the exploding pair (if any), and the pair's right value is added to the first regular number to the right of the exploding pair (if any). Exploding pairs will always consist of two regular numbers. Then, the entire exploding pair is replaced with the regular number 0.

Here are some examples of a single explode action:

[[[[[9,8],1],2],3],4] becomes [[[[0,9],2],3],4] (the 9 has no regular number to its left, so it is not added to any regular number).
[7,[6,[5,[4,[3,2]]]]] becomes [7,[6,[5,[7,0]]]] (the 2 has no regular number to its right, and so it is not added to any regular number).
[[6,[5,[4,[3,2]]]],1] becomes [[6,[5,[7,0]]],3].
[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]] becomes [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]] (the pair [3,2] is unaffected because the pair [7,3] is further to the left; [3,2] would explode on the next action).
[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]] becomes [[3,[2,[8,0]]],[9,[5,[7,0]]]].
To split a regular number, replace it with a pair; the left element of the pair should be the regular number divided by two and rounded down, while the right element of the pair should be the regular number divided by two and rounded up. For example, 10 becomes [5,5], 11 becomes [5,6], 12 becomes [6,6], and so on.

Here is the process of finding the reduced result of [[[[4,3],4],4],[7,[[8,4],9]]] + [1,1]:

after addition: [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
after explode:  [[[[0,7],4],[7,[[8,4],9]]],[1,1]]
after explode:  [[[[0,7],4],[15,[0,13]]],[1,1]]
after split:    [[[[0,7],4],[[7,8],[0,13]]],[1,1]]
after split:    [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]
after explode:  [[[[0,7],4],[[7,8],[6,0]]],[8,1]]
Once no reduce actions apply, the snailfish number that remains is the actual result of the addition operation: [[[[0,7],4],[[7,8],[6,0]]],[8,1]].

The homework assignment involves adding up a list of snailfish numbers (your puzzle input). The snailfish numbers are each listed on a separate line. Add the first snailfish number and the second, then add that result and the third, then add that result and the fourth, and so on until all numbers in the list have been used once.

For example, the final sum of this list is [[[[1,1],[2,2]],[3,3]],[4,4]]:

[1,1]
[2,2]
[3,3]
[4,4]
The final sum of this list is [[[[3,0],[5,3]],[4,4]],[5,5]]:

[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
The final sum of this list is [[[[5,0],[7,4]],[5,5]],[6,6]]:

[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]
Here's a slightly larger example:

[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]
The final sum [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]] is found after adding up the above snailfish numbers:

  [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
+ [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
= [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]

  [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
+ [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
= [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]

  [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]
+ [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
= [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]

  [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]
+ [7,[5,[[3,8],[1,4]]]]
= [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]

  [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]
+ [[2,[2,2]],[8,[8,1]]]
= [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]

  [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]
+ [2,9]
= [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]

  [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]
+ [1,[[[9,3],9],[[9,0],[0,7]]]]
= [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]

  [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]
+ [[[5,[7,4]],7],1]
= [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]

  [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]
+ [[[[4,2],2],6],[8,7]]
= [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]
To check whether it's the right answer, the snailfish teacher only checks the magnitude of the final sum. The magnitude of a pair is 3 times the magnitude of its left element plus 2 times the magnitude of its right element. The magnitude of a regular number is just that number.

For example, the magnitude of [9,1] is 3*9 + 2*1 = 29; the magnitude of [1,9] is 3*1 + 2*9 = 21. Magnitude calculations are recursive: the magnitude of [[9,1],[1,9]] is 3*29 + 2*21 = 129.

Here are a few more magnitude examples:

[[1,2],[[3,4],5]] becomes 143.
[[[[0,7],4],[[7,8],[6,0]]],[8,1]] becomes 1384.
[[[[1,1],[2,2]],[3,3]],[4,4]] becomes 445.
[[[[3,0],[5,3]],[4,4]],[5,5]] becomes 791.
[[[[5,0],[7,4]],[5,5]],[6,6]] becomes 1137.
[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]] becomes 3488.
So, given this example homework assignment:

[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
The final sum is:

[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]
The magnitude of this final sum is 4140.

Add up all of the snailfish numbers from the homework assignment in the order they appear. What is the magnitude of the final sum?
'''

import math

input_filename = 'input18-1.txt'


class SnailNumber:
    def __init__(self):
        self.root = None

    def add(self, node):
        if self.root is None:
            self.root = node
            self.reduce()
            print('Added')
            print(self.print())
            print()
            return

        new_root = Node()
        new_root.left = self.root
        new_root.left.parent = new_root
        new_root.right = node
        new_root.right.parent = new_root
        self.root = new_root

        self.reduce()

        print('Added')
        print(self.print())
        print()

    def reduce(self):
        max_steps = 1000
        for _ in range(max_steps):
            exploded = self.explode()
            if exploded:
                # print('Explode')
                # print(self.print())
                # print()
                continue
            splitted = self.split()
            # if splitted:
            #     print('Split')
            #     print(self.print())
            #     print()

            if not(splitted):
                return
        assert False, 'max steps hit'

    def find_exploding_node(self, node, depth):
        assert node is not None

        if node.value is not None:
            return None

        if node.left.value is not None and depth > 4:
            return node
        if node.right.value is not None and depth > 4:
            return node

        left_explosion = self.find_exploding_node(node.left, depth + 1)
        if left_explosion is not None:
            return left_explosion

        right_explosion = self.find_exploding_node(node.right, depth + 1)
        if right_explosion is not None:
            return right_explosion

        return None

    def explode(self) -> bool:
        # Find where explosion occurs
        exploding_node = self.find_exploding_node(self.root, 1)

        # No explosion found
        if exploding_node is None:
            return False

        # Explode
        left_parent = self.left_side_parent(
            exploding_node, exploding_node.parent)
        if left_parent is not None:
            left_val = self.rightmost_child(left_parent.left)
            left_val.value += exploding_node.left.value

        right_parent = self.right_side_parent(
            exploding_node, exploding_node.parent)
        if right_parent is not None:
            right_val = self.leftmost_child(right_parent.right)
            right_val.value += exploding_node.right.value

        exploding_node.value = 0
        del exploding_node.left
        exploding_node.left = None
        del exploding_node.right
        exploding_node.right = None
        return True

    def find_splitting_node(self, node):
        assert node is not None

        if node.value is not None:
            if node.value >= 10:
                return node
            return None

        left_split = self.find_splitting_node(node.left)
        if left_split is not None:
            return left_split

        right_split = self.find_splitting_node(node.right)
        if right_split is not None:
            return right_split

        return None

    def split(self) -> bool:
        # Find where split occurs
        splitting_node = self.find_splitting_node(self.root)

        # No split found
        if splitting_node is None:
            return False

        # Split
        new_left_node = Node()
        new_left_node.parent = splitting_node
        new_left_node.value = math.floor(splitting_node.value / 2)

        new_right_node = Node()
        new_right_node.parent = splitting_node
        new_right_node.value = math.ceil(splitting_node.value / 2)

        splitting_node.value = None
        splitting_node.left = new_left_node
        splitting_node.right = new_right_node

        return True

    def print(self, node=None):
        if node is None:
            node = self.root

        if node.value is None:
            return f'[{self.print(node.left)},{self.print(node.right)}]'
        return node.value

    def find_magnitude(self, node=None):
        if node is None:
            node = self.root

        if node.value is not None:
            return node.value

        left = self.find_magnitude(node.left)
        right = self.find_magnitude(node.right)
        return 3 * left + 2 * right

    def left_side_parent(self, node, parent):
        if parent is None:
            return None
        if parent.left == node:
            return self.left_side_parent(parent, parent.parent)
        return parent

    def right_side_parent(self, node, parent):
        if parent is None:
            return None
        if parent.right == node:
            return self.right_side_parent(parent, parent.parent)
        return parent

    def leftmost_child(self, node):
        if node.value is None:
            return self.leftmost_child(node.left)
        return node

    def rightmost_child(self, node):
        if node.value is None:
            return self.rightmost_child(node.right)
        return node


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.value = None


def parse_string(string, parent=None):
    new_node = Node()

    if len(string) == 1:
        new_node.value = int(string)
        new_node.parent = parent
        return new_node

    depth = 0
    comma_idx = -1
    for i, char in enumerate(string):
        if char == '[':
            depth += 1
        if char == ']':
            depth -= 1
        if depth == 1 and char == ',':
            comma_idx = i
            break

    new_node.left = parse_string(string[1:comma_idx], new_node)
    new_node.right = parse_string(string[comma_idx + 1:-1], new_node)
    new_node.parent = parent
    return new_node


def parse_input(input_filename):
    input_data_raw = []
    with open(input_filename) as f:
        input_data_raw = f.read().splitlines()

    inputs = [parse_string(row) for row in input_data_raw]
    return inputs


def main():
    numbers = parse_input(input_filename)
    output = SnailNumber()
    for num in numbers:
        output.add(num)
    return output.find_magnitude()


if __name__ == "__main__":
    result = main()
    print(result)  # 3869
