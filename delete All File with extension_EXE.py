#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      acer
#
# Created:     05-05-2017
# Copyright:   (c) acer 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import sys          #module for terminating 
import glob
import tkinter as tk
from tkinter import filedialog
def main():
    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory()  #source folder
    count=0
    for root,files in os.walk(directory):
        os.chdir(root)
        files = glob.glob('*.exe')
        for filename in files:
            os.unlink(filename)
            count+=1
    print("Total {} files deleted".format(count))

if __name__ == '__main__':
    main()
