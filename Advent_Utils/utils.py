import os

default_file_pattern = """

def main():
    None
    

if __name__ == '__main__':
    main()
"""


def load_data(mode: bool = False):
    if mode:
        f = open("input.txt")
    else:
        f = open("test.txt")
    returns = [line.rstrip("\n") for line in f.readlines()]
    f.close()
    return returns


def add_files(day: int):
    os.chdir("..")
    os.mkdir(f"Day_{day}")
    os.chdir(f"Day_{day}")
    for file in ["input.txt",
                 "test.txt",
                 f"Day_{day}_part_1.py",
                 f"Day_{day}_part_2.py"]:
        f = open(file, "w")
        if file.endswith('py'):
            f.write(default_file_pattern)
        f.close()


if __name__ == "__main__":
    for i in range(1, 26):
        add_files(i)
