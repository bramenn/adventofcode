"""
--- Part Two ---

It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like
to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 or 2-3,4-5) don't overlap, while the remaining
four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

    5-7,7-9 overlaps in a single section, 7.
    2-8,3-7 overlaps all of the sections 3 through 7.
    6-6,4-6 overlaps in a single section, 6.
    2-6,4-8 overlaps in sections 4, 5, and 6.

So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?
"""

f = open("tasks.txt", "r")


def tasks_are_contained(task_1: str, task_2: str) -> bool:
    task_1_index_1, task_1_index_2 = task_1.split("-")
    task_2_index_1, task_2_index_2 = task_2.split("-")

    task_1_index_1 = int(task_1_index_1)
    task_1_index_2 = int(task_1_index_2)
    task_2_index_1 = int(task_2_index_1)
    task_2_index_2 = int(task_2_index_2)

    if (
        task_1_index_1 <= task_2_index_1 <= task_1_index_2
        or task_1_index_1 <= task_2_index_2 <= task_1_index_2
    ):
        return True

    elif (
        task_2_index_1 <= task_1_index_1 <= task_2_index_2
        or task_2_index_1 <= task_1_index_2 <= task_2_index_2
    ):
        return True

    return False


contained_tasks = 0

for tasks in f:
    tasks = tasks.replace("\n", "")
    first_block_tasks, second_block_tasks = tasks.split(",")

    if tasks_are_contained(first_block_tasks, second_block_tasks):
        contained_tasks += 1


print("TOTAL contained_tasks ->", contained_tasks)  # 933

f.close()
