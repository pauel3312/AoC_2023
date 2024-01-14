from Advent_Utils.utils import load_data
import Day_16.Day_16_part_1 as Part1

data = []


def get_energized_tiles_with_start(start_beam):
    beam_starts: set[tuple[tuple[int, int], tuple[int, int]]] = set()
    beam_starts.add(start_beam)
    Part1.beam_step(start_beam[0], start_beam[1], beam_starts)
    number_energized_tiles = 0
    for line in Part1.display_beams_on_data(start_beam, beam_starts):
        number_energized_tiles += line.count("#")
    return number_energized_tiles


def do_all_from_direction(direction: tuple[int, int]) -> int:
    max_n_energized = 0
    start_position_mask = (abs(direction[1]), abs(direction[0]))

    if -1 in direction:
        if direction[0] == -1:
            default_start_position = (len(data)-1, 0)
        else:
            default_start_position = (0, len(data)-1)
    else:
        default_start_position = (0, 0)

    for i in range(len(data)):
        start_beam = ((default_start_position[0] + (start_position_mask[0] * i),
                       default_start_position[1] + (start_position_mask[1] * i)),
                      direction)
        max_n_energized_for_current_beam = get_energized_tiles_with_start(start_beam)
        if max_n_energized_for_current_beam > max_n_energized:
            max_n_energized = max_n_energized_for_current_beam

    return max_n_energized


def main():
    global data
    data = load_data(16, 2023, True)
    Part1.data = data
    max_n_energized = 0

    for direction in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        max_from_current_direction = do_all_from_direction(direction)
        if max_from_current_direction > max_n_energized:
            max_n_energized = max_from_current_direction

    return max_n_energized


if __name__ == '__main__':
    print(main())
