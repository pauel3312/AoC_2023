
file = "test.txt"


def get_input():
    f = open(file, 'r')
    data = [line.rstrip('\n') for line in f.readlines()]
    f.close()
    return data


def expand_space(data):
    data_expanded_columns = []
    empty_columns = set(range(len(data[0])))

    for line in data:
        for check_column in empty_columns.copy():
            if line[check_column] == "#":
                empty_columns.remove(check_column)

    for line in data:
        new_line = ""
        for i, char in enumerate(line):
            if i in empty_columns:
                new_line += "."
            new_line += char
        data_expanded_columns.append(new_line)
        if "#" not in new_line:
            data_expanded_columns.append(new_line)
    return data_expanded_columns


def get_sum_shortest_paths(galaxy_coordinates):
    sum_shortest_paths = 0
    for i, galaxy in enumerate(galaxy_coordinates):
        print(galaxy_coordinates[i+1:])
        for pair in galaxy_coordinates[i+1:]:
            sum_shortest_paths += abs(galaxy[0]-pair[0]) + abs(galaxy[1]-pair[1])
    return sum_shortest_paths


def main():
    real_space = expand_space(get_input())
    galaxy_coordinates = []
    for x, line in enumerate(real_space):
        for y, char in enumerate(line):
            if char == "#":
                galaxy_coordinates.append((x, y))

    print(get_sum_shortest_paths(galaxy_coordinates))


if __name__ == '__main__':
    main()
