file = "part_2_test_2.txt"
lines = []

tiles_connections = {"|": ((-1, 0), (1, 0)),
                     "-": ((0, -1), (0, 1)),
                     "L": ((-1, 0), (0, 1)),
                     "J": ((-1, 0), (0, -1)),
                     "7": ((1, 0), (0, -1)),
                     "F": ((1, 0), (0, 1)),
                     ".": tuple(),
                     "S": ((1, 0), (0, 1), (-1, 0), (0, -1)),
                     "O": tuple(),
                     "I": tuple()}


def get_start():
    for x, line in enumerate(lines):
        if 'S' not in line:
            continue
        return x, line.index('S')
    else:
        raise Exception('No start position found')


def get_connected_positions(position):
    connected_postions = []
    for offset in tiles_connections[lines[position[0]][position[1]]]:
        connected_postions.append((position[0] + offset[0],
                                   position[1] + offset[1]))
    return connected_postions


def main():
    global lines
    f = open(file, 'r')
    lines = [line.strip('\n') for line in f.readlines()]
    f.close()
    start_position = get_start()
    distances_record = {}
    equidistant_positions = []
    for potential_path in get_connected_positions(start_position):
        if start_position in get_connected_positions(potential_path):
            equidistant_positions.append(potential_path)
    for path in equidistant_positions:
        distances_record[path] = 1
    distance_counter = 2
    while len(equidistant_positions) > 0:
        new_eq_positions = []
        for position in equidistant_positions:
            for potential_next in get_connected_positions(position):
                if (potential_next not in distances_record.keys() and
                        position in get_connected_positions(potential_next) and
                        potential_next != start_position):
                    new_eq_positions.append(potential_next)

        for position in new_eq_positions:
            distances_record[position] = distance_counter

        distance_counter += 1
        equidistant_positions = new_eq_positions

    return distances_record, lines


if __name__ == '__main__':
    print(max(main()[0].values()))
