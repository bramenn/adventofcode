"""
--- Part Two ---
Your device's communication system is correctly detecting packets, but still isn't working.
It looks like it also needs to look for messages.

A start-of-message marker is just like a start-of-packet marker, except it consists of 14
distinct characters rather than 4.

Here are the first positions of start-of-message markers for all of the above examples:

mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26
How many characters need to be processed before the first start-of-message marker is detected?
"""

f = open("signal.txt", "r")

first_line = f.readline()

counter = 0

while True:

    text = first_line[counter : counter + 14]
    is_repet = set(text)

    if len(is_repet) == 14:
        break

    counter += 1


print("first marker index", counter + 14)  # 3476

f.close()
