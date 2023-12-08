
file = 'input.txt'

time = 0
distance = 0


def get_data():
    global time, distance
    f = open(file, 'r')
    times_str, distances_str = f.readlines()
    f.close()
    time_str = ''
    distance_str = ''
    for t in times_str.rstrip('\n').split(' '):
        if t.isdigit():
            time_str += t
    for d in distances_str.split(' '):
        if d.isdigit():
            distance_str += d
    time = int(time_str)
    distance = int(distance_str)


def get_n_solutions(t, d):
    n_solutions = 0
    for spd in range(t + 1):
        if (t - spd)*spd > d:
            n_solutions += 1
    return n_solutions


def main():
    get_data()
    print(get_n_solutions(time, distance))


if __name__ == '__main__':
    main()
