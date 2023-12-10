file = "input.txt"
position_decoder = {"R": 1, "L": 0}


def main():
    f = open(file, 'r')
    sequence = f.readline().rstrip('\n')
    f.readline()
    lines_next = {}
    for line in f.readlines():
        line = line.rstrip('\n')
        key, value = line.split(' = ')
        value = (value.split(", ")[0].lstrip('('), value.split(", ")[1].rstrip(')'))
        lines_next[key] = value
    position = 'AAA'
    counter = 0
    while position != 'ZZZ':
        position = lines_next[position][position_decoder[sequence[counter % len(sequence)]]]
        counter += 1
    print(counter)


if __name__ == '__main__':
    main()
