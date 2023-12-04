
numbers = []
characters = []
labels_sum = 0

test_line = "467..114.."

file = "input.txt"


def get_numbers_line(line: str, line_nbr):
    num_len = 0
    for i, char in enumerate(line):
        if num_len > 0:
            num_len -= 1
            continue
        if char.isdigit():
            num = char
            num_len = 1
            while i+num_len < len(line) and line[i+num_len].isdigit():
                num += line[i+num_len]
                num_len += 1
            numbers.append((int(num), i, i+num_len, line_nbr))


def get_numbers_file(filename: str = file):
    f = open(filename, "r")
    for i, line in enumerate(f.readlines()):
        get_numbers_line(line, i)


def get_char_positions(filename: str = file):
    f = open(filename, "r")
    for i, line in enumerate(f.readlines()):
        for j, char in enumerate(line):
            if char not in ".12345667890\n":
                characters.append((j, i))


def get_nums(filename=file):
    global labels_sum
    for number in numbers:
        horizontal = tuple(range(number[1]-1, number[2]+1))
        vertical = tuple(range(number[3]-1, number[3]+2))
        for char in characters:
            if char[0] in horizontal and char[1] in vertical:
                labels_sum += number[0]


get_numbers_file()
get_char_positions()
get_nums()
print(labels_sum)
