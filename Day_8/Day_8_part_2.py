from math import gcd

file = "input.txt"
position_decoder = {"R": 1, "L": 0}


def lcm(a: list[int]):
    result = 1
    for i in a:
        result = result * i // gcd(result, i)
    return result


def main():
    f = open(file, 'r')
    sequence = f.readline().rstrip('\n')
    f.readline()
    lines_next = {}
    positions = []
    for line in f.readlines():
        line = line.rstrip('\n')
        key, value = line.split(' = ')
        value = (value.split(", ")[0].lstrip('('), value.split(", ")[1].rstrip(')'))
        lines_next[key] = value
        if key.endswith('A'):
            positions.append(key)

    positions_patterns = []
    mul_components = []
    add_components = []

    for position in positions:
        counter = 0
        sequence_index = 0
        while not position.endswith('Z'):
            position = lines_next[position][position_decoder[sequence[sequence_index % len(sequence)]]]
            counter += 1
            sequence_index += 1

        add_component = counter
        position = lines_next[position][position_decoder[sequence[sequence_index % len(sequence)]]]
        sequence_index += 1
        counter = 0

        while not position.endswith('Z'):
            position = lines_next[position][position_decoder[sequence[sequence_index % len(sequence)]]]
            counter += 1
            sequence_index += 1

        mul_component = counter
        positions_patterns.append((mul_component, add_component))
        add_components.append(add_component)
        mul_components.append(mul_component)

    print(lcm(add_components))
    print(lcm(mul_components))


if __name__ == '__main__':
    main()
