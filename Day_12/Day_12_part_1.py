from Advent_Utils.utils import load_data


def sep_data(line: str):
    data, hints = line.split(" ")
    hints = eval(f"[{hints}]")
    return data, hints


def get_num_valid_entries(data, hints):
    if len(hints) == 0:
        if "#" not in data:
            return 1
        return 0

    if len(data) == 0:
        return 0

    match data[0]:
        case ".":
            return get_num_valid_entries(data[1:], hints)
        case "?":
            return (get_num_valid_entries(f".{data[1:]}", hints) +
                    get_num_valid_entries(f"#{data[1:]}", hints))
        case "#":
            if len(data) < hints[0]:
                return 0
            if "." not in data[:hints[0]]:
                if len(data) == hints[0]:
                    return get_num_valid_entries(list(), hints[1:])
                else:
                    if data[hints[0]] == "#":
                        return 0
                    return get_num_valid_entries(data[hints[0]+1:], hints[1:])
            else:
                return 0


def main():
    lines = load_data(True)
    result = 0

    for line in lines:
        data, hints = sep_data(line)
        result += get_num_valid_entries(data, hints)
    return result


if __name__ == '__main__':
    print(main())
