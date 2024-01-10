import os

default_file_pattern = """
from Advent_Utils.utils import load_data


def main():
    data = load_data({}, 2023, False)
    

if __name__ == '__main__':
    main()
"""


def load_data(day: int, year: int, mode: bool = False):
    if mode:
        os.system(f"aocd {day} {year} > temp")
        f = open("temp")
    else:
        f = open("test.txt")
    returns = [line.rstrip("\n") for line in f.readlines()]
    f.close()
    if mode:
        os.remove("temp")
    return returns


def add_files(day: int):
    os.chdir("..")
    try:
        os.mkdir(f"Day_{day}")
    except FileExistsError:
        pass
    os.chdir(f"Day_{day}")
    for file in ["test.txt",
                 f"Day_{day}_part_1.py",
                 f"Day_{day}_part_2.py"]:
        f = open(file, "w")
        if file.endswith('py'):
            f.write(default_file_pattern.format(day))
        f.close()


if __name__ == "__main__":
    for i in range(1, 26):
        add_files(i)
