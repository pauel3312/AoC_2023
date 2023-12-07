file = "input.txt"
path = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]


def parse_file():
    returns = []
    f = open(file, "r")
    for current_map in (f.read().split("\n\n")):
        returns.append(current_map)
    f.close()
    return returns


def get_table(i):
    return parse_file()[i].split("\n")[1:]


def get_source_range(elem):
    values = [int(x) for x in elem.split(" ")]
    return range(values[1], values[1] + values[2])


def get_source_dest_diff(elem):
    values = [int(x) for x in elem.split(" ")]
    return values[0] - values[1]


def get_next(table, seed):
    for elem in table:
        if seed in get_source_range(elem):
            seed = seed + get_source_dest_diff(elem)
            break
    return seed


def main():
    seeds = [int(i) for i in parse_file()[0].split(":")[1][1:].split(" ")]
    locations = []

    for seed in seeds:
        for i in range(len(path)-1):
            seed = get_next(get_table(i+1), seed)
        locations.append(seed)

    print(min(locations))


if __name__ == "__main__":
    main()
