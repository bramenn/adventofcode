"""
--- Part Two ---

The Elf finishes helping with the tent and sneaks back over to you. "Anyway,
the second column says how the round needs to end: X means you need to lose,
Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to
choose so the round ends as indicated. The example above now goes like this:

    In the first round, your opponent will choose Rock (A), and you need the round to
    end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
    In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X)
    with a score of 1 + 0 = 1.
    In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.

Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if
everything goes exactly according to your strategy guide?


NOTES:

# A -> Rock -> 1
# B -> Paper -> 2
# C -> Scissors -> 3

# X -> lost -> 0
# Y -> draw -> 3
# Z -> win -> 6
"""

f = open("moves.txt", "r")

data = {
    "A": {"name": "Rock", "lost_with": "B", "value": 1},
    "B": {"name": "Paper", "lost_with": "C", "value": 2},
    "C": {"name": "Scissors", "lost_with": "A", "value": 3},
}

strategy = {
    "X": {"name": "lost", "value": 0},
    "Y": {"name": "draw", "value": 3},
    "Z": {"name": "win", "value": 6},
}

player_counter = 0


def hand_result(hand: str, order: str) -> int:

    _hand_1 = data[hand]
    _order = strategy[order]

    if _order["value"] == 6:
        my_hand = data[_hand_1["lost_with"]]
    elif _order["value"] == 3:
        my_hand = _hand_1
    else:
        my_hand = data[_hand_1["lost_with"]]["lost_with"]
        my_hand = data[my_hand]

    return my_hand["value"] + _order["value"]


for line in f:
    line = line.replace("\n", "")

    player_1_hand, order = line.split(" ")
    player_counter += hand_result(player_1_hand, order)


print("player_counter -> ", player_counter)  # 10560

f.close()
