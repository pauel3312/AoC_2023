from Day_9_part_1 import get_differences, get_sequences


def get_prev(sequence):
    successive_sequences = [sequence, ]
    differences = get_differences(sequence)
    while len(differences) != differences.count(0):
        successive_sequences.append(differences)
        differences = get_differences(differences)
    result = 0
    for i in range(len(successive_sequences)):
        result = successive_sequences[-(i+1)][0] - result
    return result


def main():
    sequences = get_sequences()
    sum_prev_numbers = 0
    for sequence in sequences:
        sum_prev_numbers += get_prev(sequence)
    print(sum_prev_numbers)


if __name__ == '__main__':
    main()
