

def main():
    ways = 0
    for row in open("input.txt", 'r').readlines():
        record, checksum = row.split()
        checksum = [int(n) for n in checksum.split(',')]
        record = '?'.join([record for i in range(5)])
        checksum *= 5
        positions = {0: 1}
        for i, contiguous in enumerate(checksum):
            new_positions = {}
            for k, v in positions.items():
                for n in range(k, len(record) - sum(checksum[i + 1:]) + len(checksum[i + 1:])):
                    if n + contiguous - 1 < len(record) and '.' not in record[n:n + contiguous]:
                        if (i == len(checksum) - 1 and '#' not in record[n + contiguous:]) or (
                                i < len(checksum) - 1 and n + contiguous < len(record) and record[
                                n + contiguous] != '#'):
                            new_positions[n + contiguous + 1] = (new_positions[
                                                                    n + contiguous + 1] +
                                                                 v) if n + contiguous + 1 in new_positions else v
                    if record[n] == '#':
                        break
            positions = new_positions
        ways += sum(positions.values())
    print(ways)


if __name__ == '__main__':
    print(main())
