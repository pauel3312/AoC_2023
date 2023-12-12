import Day_10_part_1 as Part1
from sys import setrecursionlimit

setrecursionlimit(10000)

loop_tiles, lines = Part1.main()
loop_tiles = loop_tiles.keys()
outside_empty_tiles: set[tuple] = set()


def get_nearby_empty_tiles_no_squeeze(position):
    adjacent_empty_tiles = set()
    for x_offset in (-1, 0, 1):
        for y_offset in ((-1, 0, 1) if x_offset != 0 else (-1, 1)):
            if position[0] + x_offset in (len(lines), -1) or position[1] + y_offset in (len(lines[0]), -1):
                continue
            if lines[position[0] + x_offset][position[1] + y_offset] == '.':
                adjacent_empty_tiles.add((position[0] + x_offset, position[1] + y_offset))
    return adjacent_empty_tiles


def get_all_nearby_empty_tiles(position):
    adjacent_empty_tiles = set()
    for x_offset in (-1, 0, 1):
        for y_offset in ((-1, 0, 1) if x_offset != 0 else (-1, 1)):
            if (position[0] + x_offset not in range(len(lines)) or
                    position[1] + y_offset not in range(len(lines[0]))):
                continue
            if x_offset == 0:
                for link_offset in (-1, 1):
                    if position[0] + link_offset not in range(len(lines)):
                        continue
                    if ((not is_linked((position[0], position[1] + y_offset),
                                      (position[0] + link_offset, position[1] + y_offset))) and
                            "." not in (lines[position[0]][position[1]+y_offset],
                                        lines[position[0] + link_offset][position[1] + y_offset])):
                        for tile in get_empties_after_squeeze(((int(position[0]), int(position[1] + y_offset)),
                                                               (int(position[0] + link_offset),
                                                                int(position[1] + y_offset))),
                                                              (x_offset, y_offset)):
                            adjacent_empty_tiles.add(tile)

            elif y_offset == 0:
                for link_offset in (-1, 1):
                    if position[1] + link_offset not in range(len(lines[0])):
                        continue
                    if ((not is_linked((position[0] + x_offset, position[1]),
                                       (position[0] + x_offset, position[1] + link_offset))) and
                            "." not in (lines[position[0] + x_offset][position[1]],
                                        lines[position[0] + x_offset][position[1] + link_offset])):
                        for tile in get_empties_after_squeeze(((int(position[0] + x_offset), int(position[1])),
                                                               (int(position[0] + x_offset),
                                                                int(position[1] + link_offset))),
                                                              (x_offset, y_offset)):
                            adjacent_empty_tiles.add(tile)

    return adjacent_empty_tiles


def get_empties_after_squeeze(start_position: tuple[tuple[int, int], tuple[int, int]], direction: tuple[int, int]):
    """
    Recursively finds all the empty tiles that are connected to somewhere one can squeeze between pipes
    :param start_position: starting position as a tuple of the two positions detected as non-linked on the
    outside of the loop
    :param direction: direction in which the detection shall proceed
    :return: set of empty tiles considered adjacent to the position that called this function
    """
    returns = set()
    for position in start_position:
        try:
            if lines[position[0] + direction[0]][position[1] + direction[1]] == ".":
                returns.add((position[0] + direction[0], position[1] + direction[1]))
        except IndexError:
            return set()

    for tile in get_from_new_start(start_position[0], direction, start_position[1]):
        returns.add(tile)
    for tile in get_from_new_start(start_position[1], direction, start_position[0]):
        returns.add(tile)
    forward_pos = tuple((start_position[i][0] + direction[0], start_position[i][1] + direction[1]) for i in range(2))
    if not is_linked(forward_pos[0], forward_pos[1]):
        returns.add(get_empties_after_squeeze(forward_pos, direction))
    return returns


def get_from_new_start(start_pos, direction, start_pos_2):
    if not is_linked(start_pos,
                     (start_pos[0] + direction[0],
                      start_pos[1] + direction[1])):
        next_pos = (start_pos, (start_pos[0] + direction[0],
                                start_pos[1] + direction[1]))
        new_direction = []
        for i in range(len(start_pos)):
            new_direction.append(start_pos[i] - start_pos_2[i])
        new_direction = tuple(new_direction)
        return get_empties_after_squeeze(next_pos, new_direction)
    else:
        return set()


def is_linked(pos1, pos2):
    difference_pos1 = tuple(pos2[x] - pos1[x] for x in range(len(pos1)))
    difference_pos2 = tuple(pos1[x] - pos2[x] for x in range(len(pos1)))
    if (difference_pos1 in Part1.tiles_connections[lines[pos1[0]][pos1[1]]] and
            difference_pos2 in Part1.tiles_connections[lines[pos2[0]][pos2[1]]]):
        return True
    return False


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
        for j in (0, len(line) - 1):
            if line[j] in ".":
                outside_empty_tiles.add((i, j))

    for i, char in enumerate(lines[-1]):
        if char in ".":
            outside_empty_tiles.add((len(lines) - 1, i))

    return outside_empty_tiles


def main():
    get_outside_empty_tiles()
    positions_no_more_adjacent_empties = set()
    while len(positions_no_more_adjacent_empties) != len(outside_empty_tiles):
        for tile in outside_empty_tiles - positions_no_more_adjacent_empties:
            positions_no_more_adjacent_empties.add(tile)
            for new in get_nearby_empty_tiles_no_squeeze(tile):
                outside_empty_tiles.add(new)
            for new in get_all_nearby_empty_tiles(tile):
                outside_empty_tiles.add(new)
    print_new_pattern()


if __name__ == '__main__':
    main()
    is_linked((3, 0), (3, 1))
