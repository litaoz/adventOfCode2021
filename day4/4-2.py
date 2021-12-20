'''
--- Part Two ---
On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?

'''

from typing import List, Tuple

input_filename = 'input4-2.txt'


class BingoBoard:
    def __init__(self, board_text: List[str]):
        self.board = self.parse_board_text(board_text)
        self.selected = [[0 for _ in line] for line in self.board]

    def __repr__(self):
        # display the board
        lines = []
        for line in self.board:
            line_string = ''
            for num in line:
                line_string += f'{str(num).rjust(2)} '
            lines.append(line_string[:-1])
        board = '\n' + '\n'.join(lines) + '\n'
        return board

    def has_won(self) -> bool:
        # return if the board is won
        for row in self.selected:
            if all(row):
                return True

        numCols = len(self.selected[0])
        for colNum in range(numCols):
            col = [row[colNum] for row in self.selected]
            if all(col):
                return True

        return False

    def value(self):
        # return value of the board
        numRows = len(self.board)
        numCols = len(self.board[0])

        total = 0
        for r in range(numRows):
            for c in range(numCols):
                if self.selected[r][c] == 0:
                    total += self.board[r][c]
        return total

    def draw_number(self, num: int):
        numRows = len(self.board)
        numCols = len(self.board[0])

        for r in range(numRows):
            for c in range(numCols):
                if self.board[r][c] == num:
                    self.selected[r][c] = 1

    # helper function
    def parse_board_text(self, board_text: List[str]) -> List[List[int]]:
        result = []
        for line in board_text:
            line_int = [int(num) for num in line.split()]
            result.append(line_int)
        return result


def parse_input(input_filename) -> Tuple[str, List[BingoBoard]]:
    input_data_raw = []
    with open(input_filename) as f:
        input_data_raw = f.read().splitlines()
        input_data_raw.append('')  # recover a stripped ending space

    assert len(input_data_raw) > 3
    chosen_numbers = [int(item) for item in input_data_raw[0].split(',')]

    # Load boards
    boards = []
    buffer = []
    for row in input_data_raw[2:]:
        if row == '':
            boards.append(BingoBoard(buffer))
            buffer = []
        else:
            buffer.append(row)
    return (chosen_numbers, boards)


def main():
    chosen_numbers, boards = parse_input(input_filename)
    for num in chosen_numbers:
        buffer = []
        for board in boards:
            board.draw_number(num)
            if board.has_won() and len(boards) == 1:
                return board.value() * num
            elif board.has_won():
                pass  # don't keep for next round
            else:
                buffer.append(board)
        boards = buffer


if __name__ == "__main__":
    result = main()
    print(result)
