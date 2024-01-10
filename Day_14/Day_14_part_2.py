from Advent_Utils.utils import *
import Day_14_part_1 as Part1


def rotate_data_clockwise(data):
    new_data = ['']*len(data[0])
    for x, line in enumerate(data):
        for y, char in enumerate(line):
            new_data[y] = char + new_data[y]
    return new_data


def cycle(data):
    for i in range(4):
        data = Part1.move_all_rocks_north(data)
        data = rotate_data_clockwise(data)
    return data


def main():
    data = load_data(14, 2023, True)
    old_datasets = [data, ]
    data = cycle(data)
    while data not in old_datasets:
        old_datasets.append(data)
        data = cycle(data)
    cycle_length = len(old_datasets) - old_datasets.index(data)
    end_number = 1000000000
    while end_number >= len(old_datasets):
        end_number -= cycle_length
    return Part1.calculate_load(old_datasets[end_number])


if __name__ == '__main__':
    print(main())
