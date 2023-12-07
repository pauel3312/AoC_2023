from Day_5_part_1 import *


def format_table(i):
    table = get_table(i)
    for i, line in enumerate(table):
        line = [int(x) for x in line.split(' ')]
        table[i] = (line[0] - line[1], range(line[1], line[1] + line[2]))
    return table


def apply_line_to_seeds(line, seeds):  # line[1] = (); seeds = []
    changed_seeds = []
    new_seeds = []
    for seed in seeds:

        if line[1].start >= seed.stop or line[1].stop <= seed.start:  # ()[] or []()
            new_seeds.append(seed)
            continue

        if seed.start >= line[1].start:  # ([xx
            if seed.stop <= line[1].stop:  # ([])
                changed_seeds.append(range(seed.start + line[0],
                                           seed.stop + line[0]))
                continue

            else:  # ([)]
                changed_seeds.append(range(seed.start + line[0],
                                           line[1].stop + line[0]))
                new_seeds.append(range(line[1].stop, seed.stop))
                continue

        else:  # [(xx
            new_seeds.append(range(seed.start, line[1].start - 1))
            if seed.stop <= line[1].stop:  # [(])
                changed_seeds.append(range(line[1].start + line[0],
                                           seed.stop + line[0]))
                continue

            else:  # [()]
                new_seeds.append(range(line[1].stop, seed.stop))
                changed_seeds.append(range(line[1].start + line[0],
                                           line[1].stop + line[0]))

    return new_seeds, changed_seeds


def main():
    seeds_data = parse_file()[0].split(':')[1]
    seeds = [(int(seeds_data[1:].split(" ")[i]), int(seeds_data[1:].split(" ")[i+1]))
             for i in range(0, len(seeds_data[1:].split(" ")), 2)]
    seeds = [range(i[0], i[0]+i[1]) for i in seeds]
    for table_index in range(1, len(path)):
        changed_seeds = []
        for line in format_table(table_index):
            seeds, changed_temp = apply_line_to_seeds(line, seeds)
            for s in changed_temp:
                changed_seeds.append(s)
        for s in changed_seeds:
            seeds.append(s)
    mins = []
    for seed in seeds:
        mins.append(seed.start)
    print(min(mins))


if __name__ == "__main__":
    main()
