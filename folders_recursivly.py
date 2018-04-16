#-------------------------------------------------------------------------------
# Name:        Program to compress all the text files in any folder
# Purpose:     reduce file size and avoid file changes in our themes
#
# Author:      rakesh kumar
#
# Created:     06-05-2017
# Copyright:   rakesh kumar
# Licence:     Private use on one computer
#-------------------------------------------------------------------------------
import os
import glob
import sys
import re
import tkinter as tk
from glob import glob
from tkinter import filedialog

def remove_comment(source):
    with open(source,'r') as ifile:
        newstring = re.sub(r'/\*.*?\*/',' ',ifile.read(),flags=re.S)
    with open(source,'w') as ifile:
        ifile.write(newstring)
    print('/* */ have been removed from the inputfile')
    with open(source,'r') as ifile:
      newstring1=re.sub(r'//.*',' ',ifile.read())
    with open(source,'w') as ifile:
      ifile.write(newstring1)
    print('// have been removed from the inputfile')

def compressFile(source):
   file = open(source,"r")
   file2 = open("temp.dat","w")
   data = file.read();
   file2.write(re.sub('[\s]+',' ',data))
   file.close()
   file2.close()
   os.remove(source)
   os.rename('temp.dat',source)

def deleteFiles():
    root = tk.Tk()
    root.withdraw()
    rootdir = filedialog.askdirectory()
    if not rootdir.strip() :
        print ( "Folder Error...User did not selected any folder" )
        return
    #rootdir = 'C:\\Users\\acer\\Desktop\\HigherThinkingC++'
    count =0
    for root, subFolders, files in os.walk(rootdir):
         os.chdir(root)
         files =  glob('*.html')+ glob('*.htm') + glob('*.css') + glob('*.php')+glob('*.txt')+glob('*.cpp')
         for filename in files:
            #os.unlink(filename)
            ext = os.path.splitext(filename)[1][1:]
            if(ext =='cpp' or ext=='txt'or ext=='php'or ext=='htm'or ext=='html'or ext=='css'or ext=='js'):
                count= count+1
            #remove_comment(filename)
            compressFile(filename)
            #print filename

    print ( "Total files compressed " + str(count) + "....Check your folder now" )

if __name__ == '__main__':
    deleteFiles()
