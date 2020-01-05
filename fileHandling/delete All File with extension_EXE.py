# -------------------------------------------------------------------------------
# Name:        Program to delete a particular type of files from selected directory
#
# Author:      rakesh
#
# Created:     05-05-2017
# Copyright:   MIT
# -------------------------------------------------------------------------------
import os
import sys  # module for terminating
import glob
import tkinter as tk
from tkinter import filedialog


def main():
    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory()  # source folder
    count = 0
    for root, SubFolders, files in os.walk(directory):
        os.chdir(root)
        files = glob.glob('*.nef')
        # print(files)
        for filename in files:
            print(filename, 'Deleted')
            os.unlink(filename)
            count += 1
    print("Total {} files deleted".format(count))


if __name__ == '__main__':
    main()
