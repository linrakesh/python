# purpose       : To search and delete duplicate files 
# name          : rakesh kumar
# licence       : MIT
# How to use    : define source folder and then select target folder

import os
import sys          #module for terminating 
import glob
import tkinter as tk
from tkinter import filedialog

def del_files(source,target):
    global count
    os.chdir(source)
    source_files = glob.glob('*.*')
    for root, subFolders, files in os.walk(target):
        os.chdir(root)
        files = glob.glob('*.*')
        for filename in files:
            if filename in source_files:
                os.unlink(filename)
                count += 1
            
count=0
root = tk.Tk()
root.withdraw()
sourcedir = filedialog.askdirectory(title='Select Source Folder')  #source folder
os.chdir(sourcedir)
source_files = glob.glob('*.*')
targetdir = filedialog.askdirectory(title ='Select Target folder')  # target folder
if not targetdir.strip() :
    print ( "Folder Error...User did not selected any folder" )
    #rootdir = 'C:\\Users\\ace
    sys.exit()
for root, subFolders, files in os.walk(sourcedir):
         del_files(root,targetdir)
         
print ( "Total {} files deleted" .format(count)  )