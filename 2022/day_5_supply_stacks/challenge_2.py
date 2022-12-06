"""
--- Part Two ---

As you watch the crane operator expertly rearrange the crates, you notice the process isn't
following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away.
The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats,
an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]
[N] [C]
[Z] [M] [P]
 1   2   3

However, the action of moving three crates from stack 1 to stack 3 means that those three moved
crates stay in the same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3

Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3

Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3

In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know where
they should stand to be ready to unload the final supplies. After the rearrangement procedure
completes, what crate ends up on top of each stack?


NOTES:

    [W]         [J]     [J]
    [V]     [F] [F] [S] [S]
    [S] [M] [R] [W] [M] [C]
    [M] [G] [W] [S] [F] [G]     [C]
[W] [P] [S] [M] [H] [N] [F]     [L]
[R] [H] [T] [D] [L] [D] [D] [B] [W]
[T] [C] [L] [H] [Q] [J] [B] [T] [N]
[G] [G] [C] [J] [P] [P] [Z] [R] [H]
 1   2   3   4   5   6   7   8   9
"""

f = open("moves.txt", "r")

stacks = {
    1: "GTRW",
    2: "GCHPMSVW",
    3: "CLTSGM",
    4: "JHDMWRF",
    5: "PQLHSWFJ",
    6: "PJDNFMS",
    7: "ZBDFGCSJ",
    8: "RTB",
    9: "HNWLC",
}

# stacks = {
#     1: "ZN",
#     2: "MCD",
#     3: "P",
# }


def move_stacks_to(number_blocks: int, original_stack: int, target_stack: int):

    blocks_removed = stacks[original_stack][-number_blocks:]
    stacks[original_stack] = stacks[original_stack][:-number_blocks]
    stacks[target_stack] += blocks_removed


for move in f:
    move = move.replace("\n", "")

    _, number_blocks, _, original_stack, _, target_stack = move.split(" ")

    number_blocks = int(number_blocks)
    original_stack = int(original_stack)
    target_stack = int(target_stack)

    move_stacks_to(number_blocks, original_stack, target_stack)

final_stacks = ""

for stack in stacks:
    final_stacks += stacks[stack][-1]


print("TOTAL final_stacks ->", final_stacks)  # LVMRWSSPZ

f.close()
