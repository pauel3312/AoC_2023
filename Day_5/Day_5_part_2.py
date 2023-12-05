from Day_5_part_1 import *
import itertools as it


def format_table(i):
    table = get_table(i)
    for i, line in enumerate(table):
        line = [int(x) for x in line.split(' ')]
        table[i] = (line[0] - line[1], range(line[1], line[1] + line[2]))
    return table


def apply_line_to_input(line: tuple, input_range: range):

    if input_range.start > line[1].stop or line[1].start > input_range.stop:
        return (input_range,)

    if input_range.start in line[1]:

        if input_range.stop in line[1]:
            return (range(input_range.start + line[0], input_range.stop + line[0]),)

        range_1 = range(input_range.start + line[0], line[1].stop + line[0])
        range_2 = range(line[1].stop, input_range.stop)
        return range_1, range_2

    if line[1] in input_range:
        range_1 = range(input_range.start, line[1].start)
        range_2 = range(line[1].start + line[0], line[1].stop + line[0])
        range_3 = range(line[1].stop, input_range.stop)
        return range_1, range_2, range_3

    range_1 = range(input_range.start, line[1].start)
    range_2 = range(line[1].start + line[0], input_range.stop + line[0])
    return range_1, range_2


def main():
    seeds_data = parse_file()[0].split(':')[1]
    seeds = [(int(seeds_data[1:].split(" ")[i]), int(seeds_data[1:].split(" ")[i+1]))
             for i in range(0, len(seeds_data[1:].split(" ")), 2)]
    seeds = [range(i[0], i[0]+i[1]) for i in seeds]
    soils = []
    for seed in seeds:
        for line in format_table(1):
            for soil in apply_line_to_input(line, seed):
                soils.append(soil)
    print(format_table(2))
    print(seeds)
    print(soils)


if __name__ == "__main__":
    main()
