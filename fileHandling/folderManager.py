import os
import os.path
from os import path
import shutil

source = r'C:\Users\rakesh\Documents'

filetype = {'docs': ['doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'txt', 'rtf', 'odf', 'odt'],
            'pdf':  ['pdf'],
            'img':  ['jpg', 'jpeg', 'png', 'gif', 'bmp'],
            'exe':  ['zip', 'rar', 'exe'],
            'prg':  ['py', 'cpp', 'php'],
            'music': ['mp3', 'mp4', 'mkv', 'wmv', '3gp', 'avi', 'mov', 'aac', 'flv', 'ogg', 'ogb', 'yuv', 'mpg']
            }


def filemove(file, filetype, key):
    if(file.split('.')[1]) in filetype[key]:
        if (os.path.exists(source+'/'+key) == False):
            os.mkdir(source+'/'+key)
        elif(path.isfile(source+'/'+key)):
            os.mkdir(source+'/'+key)
        try:
            shutil.move(root + "/"+file, source+'/'+key)
        except:
            pass


for root, folder, files in os.walk(source):
    for file in files:
        for key in filetype.keys():
            if(file.split('.')[1]) in filetype[key]:
                filemove(file, filetype, key)
