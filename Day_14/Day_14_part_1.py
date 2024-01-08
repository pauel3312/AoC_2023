from Advent_Utils.utils import load_data


def get_rocks_north_to_south(data):
    rocks = []
    for x, line in enumerate(data):
        for y, char in enumerate(line):
            if char == "O":
                rocks.append((x, y))
    return rocks


def move_rock_north(data, rock):
    new_data = data.copy()
    start_line = data[rock[0]]
    new_data[rock[0]] = start_line[:rock[1]] + "." + start_line[rock[1]+1:]
    end_x = rock[0]
    while new_data[end_x-1][rock[1]] not in "#O" and end_x > 0:
        end_x -= 1
    new_data[end_x] = data[end_x][:rock[1]] + "O" + data[end_x][rock[1]+1:]
    return new_data


def move_all_rocks_north(data):
    rocks = get_rocks_north_to_south(data)
    while len(rocks) > 0:
        data = move_rock_north(data, rocks.pop(0))
    return data


def main():
    data = load_data(True)
    data = move_all_rocks_north(data)
    total_load = 0
    for rock in get_rocks_north_to_south(data):
        total_load += len(data) - rock[0]
    return total_load


if __name__ == '__main__':
    print(main())
