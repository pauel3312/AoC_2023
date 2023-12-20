from Advent_Utils.utils import load_data


def get_potential_horizontal_symmetry(pattern):
    potential_symmetry_centres = []
    for i, line in enumerate(pattern[1:]):
        if pattern[i] == line:
            potential_symmetry_centres.append((i, i+1))
    return potential_symmetry_centres


def check_symmetry_centre(pattern, centre):
    offset = 0
    while centre[0]-offset >= 0 and centre[1]+offset < len(pattern):
        if pattern[centre[0]-offset] != pattern[centre[1]+offset]:
            return False
        offset += 1
    return True


def get_n_lines_before_symmetry(centre):
    return centre[0] + 1


def transpose_pattern(pattern):
    transposed_pattern = [""]*len(pattern[0])
    for line in pattern:
        for i in range(len(pattern[0])):
            transposed_pattern[i] += line[i]
    return transposed_pattern


def separate_patterns(data):
    patterns = []
    last_pattern_sep = 0
    for i, line in enumerate(data):
        if line == "":
            patterns.append(data[last_pattern_sep:i])
            last_pattern_sep = i+1
    patterns.append(data[last_pattern_sep:])
    return patterns


def main():
    data = load_data(True)
    patterns = separate_patterns(data)
    checked_patterns = []
    result = 0
    for pattern in patterns:
        for centre in get_potential_horizontal_symmetry(pattern):
            if check_symmetry_centre(pattern, centre):
                result += 100*get_n_lines_before_symmetry(centre)
                checked_patterns.append(pattern)
                break

    for pattern in checked_patterns:
        patterns.remove(pattern)
    del checked_patterns

    for pattern in patterns:
        transposed_pattern = transpose_pattern(pattern)
        for centre in get_potential_horizontal_symmetry(transposed_pattern):
            if check_symmetry_centre(transposed_pattern, centre):
                result += get_n_lines_before_symmetry(centre)
                break

    return result


if __name__ == '__main__':
    print(main())
