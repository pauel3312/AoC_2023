from Day_11_part_1 import *
space = get_input()
EXPANSION = 1000000


def get_columns_to_expand(data):
    columns_to_expand = list(range(len(data[0])))

    for line in data:
        for check_column in columns_to_expand.copy():
            if line[check_column] == "#":
                columns_to_expand.remove(check_column)

    return columns_to_expand


def main():
    columns_to_expand = get_columns_to_expand(space)
    lines_expanded = 0
    galaxy_coordinates = []
    for x, line in enumerate(space):
        columns_expanded = 0
        if "#" not in line:
            lines_expanded += 1
            continue
        else:
            for y, char in enumerate(line):
                if y in columns_to_expand:
                    columns_expanded += 1
                elif char == "#":
                    galaxy_coordinates.append(((EXPANSION-1)*lines_expanded + x,
                                               (EXPANSION-1)*columns_expanded + y))

    print(get_sum_shortest_paths(galaxy_coordinates))


if __name__ == '__main__':
    main()
