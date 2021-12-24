'''
--- Part Two ---
You notice a second question on the back of the homework assignment:

What is the largest magnitude you can get from adding only two of the snailfish numbers?

Note that snailfish addition is not commutative - that is, x + y and y + x can produce different results.

Again considering the last example homework assignment above:

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
The largest magnitude of the sum of any two snailfish numbers in this list is 3993. This is the magnitude of [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]] + [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]], which reduces to [[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]].

What is the largest magnitude of any sum of two different snailfish numbers from the homework assignment?
'''

from itertools import permutations
import math

input_filename = 'input18-2.txt'


class SnailNumber:
    def __init__(self):
        self.root = None

    def add(self, node):
        if self.root is None:
            self.root = node
            self.reduce()
            # print('Added')
            # print(self.print())
            # print()
            return

        new_root = Node()
        new_root.left = self.root
        new_root.left.parent = new_root
        new_root.right = node
        new_root.right.parent = new_root
        self.root = new_root

        self.reduce()

        # print('Added')
        # print(self.print())
        # print()

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

    def copy(self):
        return self.root.copy()

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

    def copy(self, parent=None):
        new_node = Node()

        if self.left is not None:
            new_node.left = self.left.copy(new_node)
        if self.right is not None:
            new_node.right = self.right.copy(new_node)
        new_node.parent = parent
        new_node.value = self.value

        return new_node


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
    perm = permutations(numbers, 2)
    magnitudes = []
    for p in perm:
        num1, num2 = p
        output = SnailNumber()
        output.add(num1.copy())
        output.add(num2.copy())
        magnitudes.append(output.find_magnitude())

    return max(magnitudes)


if __name__ == "__main__":
    result = main()
    print(result)  # 4671
