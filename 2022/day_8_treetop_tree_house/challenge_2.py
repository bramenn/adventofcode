"""
--- Part Two ---

Content with the amount of tree cover available, the Elves just need to know the best spot to build
their tree house: they would like to be able to see a lot of trees.

To measure the viewing distance from a given tree, look up, down, left, and right from that tree;
stop if you reach an edge or at the first tree that is the same height or taller than the tree
under consideration. (If a tree is right on the edge, at least one of its viewing distances will
be zero.)

The Elves don't care about distant trees taller than those found by the rules above; the proposed
tree house has large eaves to keep it dry, so they wouldn't be able to see higher than the tree
house anyway.

In the example above, consider the middle 5 in the second row:

30373
25512
65332
33549
35390

    Looking up, its view is not blocked; it can see 1 tree (of height 3).
    Looking left, its view is blocked immediately; it can see only 1 tree (of height 5, right next
    to it).
    Looking right, its view is not blocked; it can see 2 trees.
    Looking down, its view is blocked eventually; it can see 2 trees (one of height 3, then the
    tree of height 5 that blocks its view).

A tree's scenic score is found by multiplying together its viewing distance in each of the four
directions. For this tree, this is 4 (found by multiplying 1 * 1 * 2 * 2).

However, you can do even better: consider the tree of height 5 in the middle of the fourth row:

30373
25512
65332
33549
35390

    Looking up, its view is blocked at 2 trees (by another tree with a height of 5).
    Looking left, its view is not blocked; it can see 2 trees.
    Looking down, its view is also not blocked; it can see 1 tree.
    Looking right, its view is blocked at 2 trees (by a massive tree of height 9).

This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the tree house.

Consider each tree on your map. What is the highest scenic score possible for any tree?

"""

from __future__ import annotations

from typing import Dict, List

trees_y: Dict[int, List[Tree]] = {}
trees_x: Dict[int, List[Tree]] = {}

right_edge = 0
right_edge = 0
bottom_edge = 0
total_visibles_trees = 0


class Tree:

    pos_y: int
    pos_x: int

    height: int
    highest_scenic_score: int

    r_highest_scenic_score: int
    l_highest_scenic_score: int
    t_highest_scenic_score: int
    b_highest_scenic_score: int

    def __init__(self, pos_y: int, pos_x: int, height: int):
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.height = height
        self.highest_scenic_score = 1
        self.r_highest_scenic_score = 0
        self.l_highest_scenic_score = 0
        self.t_highest_scenic_score = 0
        self.b_highest_scenic_score = 0

    @property
    def is_visible_for_left(self) -> bool:
        result = True
        for tree in trees_y[self.pos_y][: self.pos_x][::-1]:
            if int(tree) >= self.height:
                result = False
                break
            self.l_highest_scenic_score += 1

        self.highest_scenic_score *= self.l_highest_scenic_score
        return result

    @property
    def is_visible_for_rigth(self):
        result = True
        for tree in trees_y[self.pos_y][self.pos_x + 1 :]:
            self.r_highest_scenic_score += 1
            if int(tree) >= self.height:
                result = False
                break

        self.highest_scenic_score *= self.r_highest_scenic_score
        return result

    @property
    def is_visible_for_top(self):
        result = True
        for tree in trees_x[self.pos_x][: self.pos_y][::-1]:
            self.t_highest_scenic_score += 1
            if int(tree) >= self.height:
                result = False
                break

        self.highest_scenic_score *= self.t_highest_scenic_score
        return result

    @property
    def is_visible_for_bottom(self):
        result = True
        for tree in trees_x[self.pos_x][self.pos_y + 1 :]:
            self.b_highest_scenic_score += 1
            if int(tree) >= self.height:
                result = False
                break
        self.highest_scenic_score *= self.b_highest_scenic_score
        return result

    @property
    def is_visible(self) -> bool:
        global total_visibles_trees
        if (
            self.pos_y == 0
            or self.pos_y == right_edge
            or self.pos_x == 0
            or self.pos_x == bottom_edge
            ############################
            or self.is_visible_for_rigth
            or self.is_visible_for_left
            or self.is_visible_for_top
            or self.is_visible_for_bottom
        ):
            total_visibles_trees += 1
            return True

        return False


f = open("map.txt", "r")

counter_y = 0
trees = []

for row_trees in f:
    row_trees = row_trees.replace("\n", "")
    if not right_edge:
        right_edge = len(row_trees) - 1

    counter_x = 0
    trees_y[counter_y] = list(row_trees)

    for tree in row_trees:
        _tree = Tree(pos_x=counter_x, pos_y=counter_y, height=int(tree))
        trees.append(_tree)
        if not trees_x.get(counter_x):
            trees_x[counter_x] = []
        trees_x[counter_x].append(_tree.height)

        counter_x += 1

    counter_y += 1

bottom_edge = counter_y - 1

highest_scenic_score_found = 0

for tree in trees:
    tree.is_visible_for_left
    tree.is_visible_for_rigth
    tree.is_visible_for_top
    tree.is_visible_for_bottom
    if tree.highest_scenic_score > highest_scenic_score_found:
        highest_scenic_score_found = tree.highest_scenic_score


print("highest_scenic_score_found ->", highest_scenic_score_found)  # 287040

f.close()

# 1823624 >>
