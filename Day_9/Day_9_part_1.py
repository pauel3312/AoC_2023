file = 'input.txt'


def get_sequences():
    f = open(file, 'r')
    sequences = f.readlines()
    f.close()
    return [list((int(x) for x in sequence.split(' '))) for sequence in sequences]


def get_differences(sequence):
    differences = []
    for i in range(len(sequence) - 1):
        differences.append(sequence[i+1] - sequence[i])
    return differences


def get_next(sequence):
    successive_sequences = [sequence, ]
    result = sequence[-1]
    differences = get_differences(sequence)
    while len(differences) != differences.count(0):
        result += differences[-1]
        successive_sequences.append(differences)
        differences = get_differences(differences)
    return result


def main():
    sequences = get_sequences()
    sum_next_numbers = 0
    for sequence in sequences:
        sum_next_numbers += get_next(sequence)
    print(sum_next_numbers)


if __name__ == '__main__':
    main()
