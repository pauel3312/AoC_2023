import Day_10_part_1 as Part1

loop_tiles, lines = Part1.main()
loop_tiles = loop_tiles.keys()
outside_empty_tiles: set[tuple] = set()
# TODO: get the tiles that you can get to from the outside wy squeezing between pipes


def get_nearby_empty_tiles(position):
    adjacent_empty_tiles = set()
    for x_offset in (-1, 0, 1):
        for y_offset in ((-1, 0, 1) if x_offset != 0 else (-1, 1)):
            if position[0] + x_offset in (len(lines), -1) or position[1] + y_offset in (len(lines[0]), -1):
                continue
            if lines[position[0] + x_offset][position[1] + y_offset] == '.':
                adjacent_empty_tiles.add((position[0] + x_offset, position[1] + y_offset))
    return adjacent_empty_tiles


def print_new_pattern():
    new_lines = []
    for i, line in enumerate(lines):
        new_line = ""
        for j, tile in enumerate(line):
            if (i, j) in outside_empty_tiles:
                new_line += 'O'
            else:
                new_line += tile
        new_lines.append(new_line)
    for line in new_lines:
        print(line)
    return new_lines


def get_outside_empty_tiles():
    global outside_empty_tiles
    for i, char in enumerate(lines[0]):
        if char in ".":
            outside_empty_tiles.add((0, i))

    for i, line in enumerate(lines[1:-1]):
        i += 1
        for j in (0, len(line)-1):
            if line[j] in ".":
                outside_empty_tiles.add((i, j))

    for i, char in enumerate(lines[-1]):
        if char in ".":
            outside_empty_tiles.add((len(lines)-1, i))

    return outside_empty_tiles


def main():
    get_outside_empty_tiles()
    positions_no_more_adjacent_empties = set()
    while len(positions_no_more_adjacent_empties) != len(outside_empty_tiles):
        for tile in outside_empty_tiles-positions_no_more_adjacent_empties:
            positions_no_more_adjacent_empties.add(tile)
            for new in get_nearby_empty_tiles(tile):
                outside_empty_tiles.add(new)
    print_new_pattern()


if __name__ == '__main__':
    main()
