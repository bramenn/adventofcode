"""
By the time you calculate the answer to the Elves' question, they've already realized that
the Elf carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories
carried by the top three Elves carrying the most Calories. That way, even if one of those
Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third
Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories
carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

"""

f = open("list_elves_calories.txt", "r")

list_elves_calories = []
count_clories = 0

for line in f:
    if line == "\n":
        list_elves_calories.append(count_clories)
        count_clories = 0
        continue
    count_clories += int(line.strip())



first_highest_calorie_elf = max(list_elves_calories)
print("first_highest_calorie_elf -> ", first_highest_calorie_elf) # // 68467

list_elves_calories.pop(list_elves_calories.index(first_highest_calorie_elf))

second_highest_calorie_elf = max(list_elves_calories)
print("second_highest_calorie_elf -> ", second_highest_calorie_elf) # // 68143

list_elves_calories.pop(list_elves_calories.index(second_highest_calorie_elf))

third_highest_calorie_elf = max(list_elves_calories)
print("third_highest_calorie_elf -> ", third_highest_calorie_elf) # // 66810

total_max_calories = first_highest_calorie_elf + third_highest_calorie_elf + third_highest_calorie_elf
print("total_max_calories -> ", total_max_calories) # // 203420