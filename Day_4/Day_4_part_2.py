from Day_4_part_1 import *

lines = open(file, "r").readlines()
card_copies = [1] * len(lines)
result = 0

for i, line in enumerate(lines):
    corrects = get_card_points(line)
    for j in range(corrects):
        card_copies[i+j+1] += card_copies[i]

for n in card_copies:
    result += n

print(result)
