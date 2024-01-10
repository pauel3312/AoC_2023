from Day_13_part_1 import *


def lines_near_equal(line1, line2):
    if len(line1) != len(line2):
        raise Exception("Lengths do not match")
    error_found = False
    for i in range(len(line1)):
        if line1[i] != line2[i]:
            if error_found:
                return False, False
            error_found = True
    return True, error_found


def get_potential_horizontal_symmetry_with_smudge(pattern):
    potential_symmetry_centres = []
    for i, line in enumerate(pattern[1:]):
        valid, smudge_found = lines_near_equal(pattern[i], line)
        if valid:
            potential_symmetry_centres.append((i, i+1, smudge_found))
    return potential_symmetry_centres


def check_symmetry_centre_with_smudge(pattern, centre):
    if centre[2]:
        return check_symmetry_centre(pattern, centre)
    offset = 1
    smudge_found = False
    while centre[0]-offset >= 0 and centre[1]+offset < len(pattern):
        if smudge_found:
            if pattern[centre[0]-offset] != pattern[centre[1]+offset]:
                return False
        else:
            valid, smudge_found = lines_near_equal(pattern[centre[0]-offset], pattern[centre[1]+offset])
            if not valid:
                return False
        offset += 1
    return smudge_found


def main():
    data = load_data(13, 2023, True)
    patterns = separate_patterns(data)
    checked_patterns = []
    result = 0
    for pattern in patterns:
        for centre in get_potential_horizontal_symmetry_with_smudge(pattern):
            if check_symmetry_centre_with_smudge(pattern, centre):
                result += 100*get_n_lines_before_symmetry(centre)
                checked_patterns.append(pattern)
                break

    for pattern in checked_patterns:
        patterns.remove(pattern)
    checked_patterns = []

    for pattern in patterns:
        transposed_pattern = transpose_pattern(pattern)
        for centre in get_potential_horizontal_symmetry_with_smudge(transposed_pattern):
            if check_symmetry_centre_with_smudge(transposed_pattern, centre):
                result += get_n_lines_before_symmetry(centre)
                checked_patterns.append(pattern)
                break

    for pattern in checked_patterns:
        patterns.remove(pattern)

    for pattern in patterns:
        for line in pattern:
            print(line)
        print()

    return result


if __name__ == '__main__':
    print(main())
