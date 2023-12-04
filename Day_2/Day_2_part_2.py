sum_powers = 0


def add_line(line):
    global sum_powers

    min_red_present = 0
    min_green_present = 0
    min_blue_present = 0

    data_str = line.split(": ")[1]
    data_packs = data_str.split("; ")

    for pack in data_packs:
        datas = pack.split(", ")
        for data in datas:
            number, color = data.split(" ")
            number = int(number)
            color = color.strip("\n")
            if number > eval(f"min_{color}_present"):
                match color:
                    case "red":
                        min_red_present = number
                    case "green":
                        min_green_present = number
                    case "blue":
                        min_blue_present = number

    sum_powers += min_red_present * min_blue_present * min_green_present


def from_file(filename="test.txt"):
    file = open(filename, "r")
    for line in file.readlines():
        add_line(line)
    print(sum_powers)


if __name__ == "__main__":
    from_file("input.txt")
