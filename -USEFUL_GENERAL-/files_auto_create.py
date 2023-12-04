import os


def add_files(day: int):
    os.chdir("..")
    os.mkdir(f"Day_{day}")
    os.chdir(f"Day_{day}")
    for file in ["input.txt",
                 "test.txt",
                 f"Day_{day}_part_1.py",
                 f"Day_{day}_part_2.py"]:
        f = open(file, "w")
        f.close()


for i in range (3, 26):
    add_files(i)
