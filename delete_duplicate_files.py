# purpose       : To search and delete duplicate files
# name          : rakesh kumar
# licence       : MIT
import os
import sys          #module for terminating 
import glob
import tkinter as tk
from tkinter import filedialog

count=0
root = tk.Tk()
root.withdraw()
sourcedir = filedialog.askdirectory()
os.chdir(sourcedir)
source_files = glob.glob('*.*')
targetdir = filedialog.askdirectory()
if not targetdir.strip() :
    print ( "Folder Error...User did not selected any folder" )
    #rootdir = 'C:\\Users\\ace
    sys.exit()
for root, subFolders, files in os.walk(targetdir):
         os.chdir(root)
         files = glob.glob('*.*')
         for filename in files:
            if filename in source_files:
                os.unlink(filename)
                count+=1
print ( "Total {} files deleted" .format(count)  )