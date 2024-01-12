import time

from Advent_Utils.utils import load_data

data = []
beam_starts: set[tuple[tuple[int, int], tuple[int, int]]] = set()


def replace_at_index_in_string(str_in: str, index: int, char: str) -> str:
    start_part = str_in[:index]
    end_part = str_in[index+1:]
    return start_part + char + end_part


def check_out_of_bounds(position: tuple[int, int]) -> bool:
    if position[0] >= len(data) or \
       position[0] < 0 or \
       position[1] >= len(data) or \
       position[1] < 0:
        return True
    return False


def beam_step(position, direction) -> None:
    new_position = (position[0] + direction[0], position[1] + direction[1])
    if check_out_of_bounds(new_position):
        return

    match data[new_position[0]][new_position[1]]:
        case ".":
            newer_position = (new_position[0] + direction[0], new_position[1] + direction[1])
            while not check_out_of_bounds(newer_position) and data[newer_position[0]][newer_position[1]] == ".":
                new_position = newer_position
                newer_position = (new_position[0] + direction[0], new_position[1] + direction[1])
            beam_step(new_position, direction)
        case "/":
            new_direction = (-direction[1], -direction[0])
            if (new_position, new_direction) in beam_starts:
                return
            beam_starts.add((new_position, new_direction))
            beam_step(new_position, new_direction)
        case "\\":
            new_direction = (direction[1], direction[0])
            if (new_position, new_direction) in beam_starts:
                return
            beam_starts.add((new_position, new_direction))
            beam_step(new_position, new_direction)
        case "-":
            if direction[0] == 0:
                beam_step(new_position, direction)
                return
            for direction_offset in (-1, 1):
                new_direction = (0, direction_offset)
                if (new_position, new_direction) in beam_starts:
                    return
                beam_starts.add((new_position, new_direction))
                beam_step(new_position, new_direction)
        case "|":
            if direction[1] == 0:
                beam_step(new_position, direction)
                return
            for direction_offset in (-1, 1):
                new_direction = (direction_offset, 0)
                if (new_position, new_direction) in beam_starts:
                    return
                beam_starts.add((new_position, new_direction))
                beam_step(new_position, new_direction)


def display_beams_on_data():
    new_data = ["."*len(data[0])]*len(data)
    for start, direction in beam_starts:
        wall = False
        step = 0
        next_position = start
        while not wall:
            if check_out_of_bounds((next_position[0], start[1] + (direction[1]*step))):
                break
            new_data[next_position[0]] = replace_at_index_in_string(new_data[next_position[0]],
                                                                    start[1] + (direction[1]*step),
                                                                    "#")
            if (((data[next_position[0]][next_position[1]] in "\\/") or
               (data[next_position[0]][next_position[1]] == "-" and direction[0] != 0) or
               (data[next_position[0]][next_position[1]] == "|" and direction[1] != 0)) and
               (start == (0, 0) and direction == (0, 1))):
                wall = True

            step += 1
            next_position = (start[0]+(direction[0]*step),
                             start[1]+(direction[1]*step))

            if check_out_of_bounds(next_position) or \
               (data[next_position[0]][next_position[1]] in "\\/") or \
               (data[next_position[0]][next_position[1]] == "-" and direction[0] != 0) or \
               (data[next_position[0]][next_position[1]] == "|" and direction[1] != 0):
                wall = True

    return new_data


def main():
    global data
    data = load_data(16, 2023, True)
    beam_starts.add(((0, 0), (0, 1)))
    beam_step((0, -1), (0, 1))
    number_energized_tiles = 0
    for energized_display_line in display_beams_on_data():
        number_energized_tiles += energized_display_line.count("#")
    return number_energized_tiles


if __name__ == '__main__':
    print(main())
