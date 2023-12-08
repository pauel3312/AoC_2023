
file = "input.txt"
times = []
distances = []


def get_data():
    f = open(file, 'r')
    times_str, distances_str = f.readlines()
    f.close()
    for t in times_str.rstrip('\n').split(' '):
        if t.isdigit():
            times.append(t)
    for d in distances_str.split(' '):
        if d.isdigit():
            distances.append(d)


def get_n_solutions(index):
    n_solutions = 0
    time = int(times[index])
    distance = int(distances[index])
    for spd in range(time+1):
        if (time-spd)*spd > distance:
            n_solutions += 1
    return n_solutions


def main():
    get_data()
    result = 1
    for i in range(len(times)):
        result *= get_n_solutions(i)
    print(result)


if __name__ == '__main__':
    main()

