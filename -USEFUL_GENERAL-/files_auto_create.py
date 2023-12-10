import os

default_file_pattern = """

def main():
    None
    

if __name__ == '__main__':
    main()
"""


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
    for i in range(11, 26):
        add_files(i)
