from Advent_Utils.utils import load_data


def hash_str(str_in: str) -> int:
    current_value = 0
    index = 0
    while index != len(str_in):
        current_value += ord(str_in[index])
        current_value *= 17
        current_value %= 256
        index += 1
    return current_value


def main():
    data = load_data(15, 2023, True)[0].split(',')
    sum_hashes = 0
    for elem in data:
        sum_hashes += hash_str(elem)
    return sum_hashes


if __name__ == '__main__':
    print(main())
