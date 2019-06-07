
from datetime import datetime
import glob2

file1 = "file1.txt"
file2 = "file2.txt"
file3 = "file3.txt"

date = datetime.now()
date = date.strftime("%Y-%m-%d-%H-%m-%S-%f")
files = glob2.glob("*.txt")


def merger(files):
    with open(date + ".txt", "w") as file:
        for filename in files:
            with open(filename, "r") as read_file:
                file.write(read_file.read() + "\n")

merger(files)