result = 0
names_digits = {"1": "1", "one": "1",
                "2": "2", "two": "2",
                "3": "3", "three": "3",
                "4": "4", "four": "4",
                "5": "5", "five": "5",
                "6": "6", "six": "6",
                "7": "7", "seven": "7",
                "8": "8", "eight": "8",
                "9": "9", "nine": "9",
                "0": "0"}


def add_number(line: str):
    global result
    digits_found = []
    for i in range(len(line)):
        for n in names_digits.keys():
            if line[i:].startswith(n):
                digits_found.append(names_digits[n])
                break
    result += int(digits_found[0]+digits_found[-1])


def from_file(filename = "test.txt"):
    file = open(filename, 'r')
    for line in file.readlines():
        add_number(line)
    file.close()
    print(result)


from_file("input.txt")
