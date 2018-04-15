#-------------------------------------------------------------------------------
# Name:        delete_duplicate.py
# Purpose:     Delete duplicate files in destination folder
## Author:     rakesh kumar
## Created:     05-05-2017
# Copyright:   binarynote.com
# Licence:     MIT
#-------------------------------------------------------------------------------
import glob
import os
def main():
    source = r'C:\Users\acer\Desktop\python_pdf'
    target = r'C:\Users\acer\Desktop\python_pdf1'
    os.chdir(source)
    file_source = glob.glob('*.*')
    os.chdir(target)
    files_target=glob.glob('*.*')
    count=0
    for filename in files_target:
        if filename in file_source :
            os.unlink(filename)
            count+=1
    
    print('Total {} files deteled'.format(count))
if __name__ == '__main__':
    main()
