#-------------------------------------------------------------------------------
# Name:             small images
# Purpose:          Program to create small images
# Author:           rakesh kumar
# Created:          09-02-2018
# Copyright:        rakesh kumar
# Licence website : http://www.cbsetoday.com
#-------------------------------------------------------------------------------
import os
import glob
import sys
import re
import tkinter as tk
from glob import glob
from tkinter import filedialog
from PIL import Image
from resizeimage import resizeimage

def small(source,target,original):
    dest = target + '\\' +original
    with open(original, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [900, 450], validate=False)
            cover.save(dest, image.format)

def deleteFiles():
    root = tk.Tk()
    root.withdraw()
    rootdir = filedialog.askdirectory()
    if not rootdir.strip() :
        print ( "Folder Error...User did not selected any folder" )
        return
    #rootdir = 'C:\\Users\\acer\\Desktop\\HigherThinkingC++'
    targetdir = filedialog.askdirectory()
    count =0
    for root, subFolders, files in os.walk(rootdir):
         os.chdir(root)
         files =  glob('*.jpg')+ glob('*.jpeg') + glob('*.png')
         for filename in files:
            #os.unlink(filename)
            filename1,ext = os.path.splitext(filename)
            print(filename1)
            if(ext =='jpg' or ext=='jpeg'or ext=='png'):
                count= count+1
            #remove_comment(filename)
            small(filename1,targetdir,filename)
            #print filename

    print ( "\n\n\nJob Complete " + str(count) + "....Check your Destination folder now\n\n" )

if __name__ == '__main__':
    deleteFiles()
