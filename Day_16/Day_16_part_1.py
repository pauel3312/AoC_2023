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
            beam_step(new_position, direction)
        case "/":
            new_direction = (-direction[1], -direction[0])
            beam_starts.add((new_position, new_direction))
            beam_step(new_position, new_direction)
        case "\\":
            new_direction = (direction[1], direction[0])
            beam_starts.add((new_position, new_direction))
            beam_step(new_position, new_direction)
        case "-":
            if direction[0] == 0:
                beam_step(new_position, direction)
                return
            for direction_offset in (-1, 1):
                new_start_position = (new_position[0], new_position[1] + direction_offset)
                if check_out_of_bounds(new_start_position):
                    continue
                new_direction = (0, direction_offset)
                beam_starts.add((new_position, new_direction))
                beam_step(new_start_position, new_direction)
        case "|":
            if direction[1] == 0:
                beam_step(new_position, direction)
                return
            for direction_offset in (-1, 1):
                new_start_position = (new_position[0] + direction_offset, new_position[1])
                if check_out_of_bounds(new_start_position):
                    continue
                new_direction = (direction_offset, 0)
                beam_starts.add((new_position, new_direction))
                beam_step(new_start_position, new_direction)


def main():
    global data
    data = load_data(16, 2023, False)
    beam_starts.add(((0, 0), (0, 1)))
    beam_step((0, 0), (0, 1))
    new_data = data.copy()
    return beam_starts


if __name__ == '__main__':
    print(main())
