
sum_IDs = 0

test_line = "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"

max_red = 12
max_green = 13
max_blue = 14


def get_game_ID(line):
    return int(line[5:line.index(":")])


def add_line(line):
    global sum_IDs
    data_str = line.split(": ")[1]
    data_packs = data_str.split("; ")
    for pack in data_packs:
        datas = pack.split(", ")
        for data in datas:
            number, color = data.split(" ")
            if int(number) > eval(f"max_{color}"):
                return
    sum_IDs += get_game_ID(line)


def from_file(filename="test.txt"):
    file = open(filename, "r")
    for line in file.readlines():
        add_line(line)
    print(sum_IDs)


if __name__ == "__main__":
    from_file("input.txt")
