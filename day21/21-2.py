'''
--- Part Two ---
Now that you're warmed up, it's time to play the real game.

A second compartment opens, this time labeled Dirac dice. Out of it falls a single three-sided die.

As you experiment with the die, you feel a little strange. An informational brochure in the compartment explains that this is a quantum die: when you roll it, the universe splits into multiple copies, one copy for each possible outcome of the die. In this case, rolling the die always splits the universe into three copies: one where the outcome of the roll was 1, one where it was 2, and one where it was 3.

The game is played the same as before, although to prevent things from getting too far out of hand, the game now ends when either player's score reaches at least 21.

Using the same starting positions as in the example above, player 1 wins in 444356092776315 universes, while player 2 merely wins in 341960390180808 universes.

Using your given starting positions, determine every possible outcome. Find the player that wins in more universes; in how many universes does that player win?
'''
from functools import cache

input_filename = 'input21-1_test.txt'


@cache
def universe_wins(p1_loc, p2_loc, p1_score, p2_score):
    if p1_score >= 21:
        return [1, 0]
    if p2_score >= 21:
        return [0, 1]

    result = (0, 0)
    for d1 in [1, 2, 3]:
        for d2 in [1, 2, 3]:
            for d3 in [1, 2, 3]:
                new_loc = (p1_loc + d1 + d2 + d3) % 10
                new_score = p1_score + new_loc + 1
                x1, y1 = universe_wins(p2_loc, new_loc, p2_score, new_score)
                result = (result[0]+y1, result[1]+x1)

    return result


def main():
    player1_location = 4 - 1
    player2_location = 6 - 1
    wins = universe_wins(player1_location, player2_location, 0, 0)
    return wins


if __name__ == "__main__":
    result = main()
    print(result)  # 647608359455719
