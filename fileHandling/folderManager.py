#   Python program to arrange files according to their file types
#   made by             : rakesh kumar
#   last compiled on    : 30/11/2019

import os.path
from os import path
import sys
import shutil
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox


filetype = {'docs': ['doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'txt', 'rtf', 'odf', 'odt'],
            'pdf':  ['pdf'],
            'img':  ['jpg', 'jpeg', 'png', 'gif', 'bmp'],
            'exe':  ['zip', 'rar', 'exe'],
            'prg':  ['py', 'cpp', 'php'],
            'music': ['mp3', 'mp4', 'mkv', 'wmv', '3gp', 'avi', 'mov', 'aac', 'flv', 'mpg']
            }


def filemove(file, filetype, key):
    if(file.split('.')[1]) in filetype[key]:
        if (os.path.exists(sourcedir+'/'+key) == False):
            os.mkdir(sourcedir+'/'+key)
        elif(path.isfile(sourcedir+'/'+key)):
            os.mkdir(sourcedir+'/'+key)
        try:
            shutil.move(sourcedir + "/"+file, sourcedir+'/'+key)
        except:
            pass


root = tk.Tk()
root.withdraw()
sourcedir = filedialog.askdirectory()  # source folder
if not sourcedir.strip():
    print("Folder Error...User did not selected any folder")
    #rootdir = 'C:\\Users\\ace
    sys.exit()

for root, folder, files in os.walk(sourcedir):
    for file in files:
        for key in filetype.keys():
            if(file.split('.')[1]) in filetype[key]:
                filemove(file, filetype, key)

tkinter.messagebox.showinfo('Folder Manager', 'Please check your Folde now')
