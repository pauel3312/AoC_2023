
gears = []

file = "input.txt"
f = open(file, "r")
lines = f.readlines()


def get_gears():
    get_adjacent_nums(lines, 1, 3)
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "*" and len(get_adjacent_nums(lines, i, j)) == 2:
                gears.append((i, j))


def get_adjacent_nums(lines, i, j):
    numbers_in_adjacent_lines = []
    numbers_found = []
    for line_i in range(i-1, i+2):
        numbers_in_adjacent_lines += get_numbers_line(lines[line_i], line_i)
    for number in numbers_in_adjacent_lines:
        horizontal = tuple(range(number[1]-1, number[2]+1))
        vertical = tuple(range(number[3]-1, number[3]+2))
        if i in vertical and j in horizontal:
            numbers_found.append(number[0])
    return numbers_found


def get_numbers_line(line: str, line_nbr):
    num_len = 0
    numbers = []
    for i, char in enumerate(line):
        if num_len > 0:
            num_len -= 1
            continue
        if char.isdigit():
            num = char
            num_len = 1
            while i + num_len < len(line) and line[i + num_len].isdigit():
                num += line[i + num_len]
                num_len += 1
            numbers.append((int(num), i, i + num_len, line_nbr))
    return numbers


get_gears()
answer = 0
for gear in gears:
    ratio = 1
    for n in get_adjacent_nums(lines, gear[0], gear[1]):
        ratio *= n
    answer += ratio
print(answer)
