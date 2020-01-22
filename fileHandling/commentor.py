#   program to add comment at the begining of each python file having extension .py
#   made by         : rakesh kumar
#   licence         : MIT

import os
import sys  # module for terminating
import glob
import tkinter as tk
from tkinter import filedialog

str = "# program to comment on every file \n"
str = str + "# made by       : rakesh kumar \n"
str = str+" # class -       : xi A \n"
str = str+" # session       :2019-20 \n\n"


def add_comment(filename):
    with open(filename, "r") as f:
        data = f.read()

    with open("abc.txt", "w") as f:
        f.write(str)
        f.write(data)

    os.unlink(filename)
    os.rename("abc.txt", filename)


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory()  # source folder
    count = 0
    for root, SubFolders, files in os.walk(directory):
        os.chdir(root)
        files = glob.glob('*.py')
        # print(files)
        for filename in files:
            print(filename, 'Comment Added')
            add_comment(filename)
            count += 1
