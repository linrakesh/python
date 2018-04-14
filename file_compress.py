#-------------------------------------------------------------------------------
# Name:        Compress a text file replacing the original file
# Purpose:
#
# Author:      acer
#
# Created:     05-05-2017
# Copyright:   (c) acer 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import re
import os
def main():
   file = open("C:\\Users\\acer\\Desktop\\single.php","r")
   file2 = open("compress.txt","w")
   data = file.read();
   file2.write(re.sub('[\s]+',' ',data))
   file.close();
   file2.close()
   os.remove('C:\\Users\\acer\\Desktop\\single.php')
   os.rename('compress.txt','C:\\Users\\acer\\Desktop\\single.php')


if __name__ == '__main__':
    main()
