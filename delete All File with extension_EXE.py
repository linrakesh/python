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
import glob
import os
def main():
    directory='C:\\Users\\acer\\Desktop\\HigherThinkingC++'
    os.chdir(directory)
    files=glob.glob('*.exe')
    for filename in files:
        os.unlink(filename)

if __name__ == '__main__':
    main()
