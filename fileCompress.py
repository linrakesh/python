#-------------------------------------------------------------------------------
# Name:        compress file
# Purpose:     compress any file so that we can save a lots of bits and byte
#
# Author:      rakesh kumar
#
# Created:     18-04-2017
# Copyright:   rakesh kumar
# Licence:     MIT-2.0
#-------------------------------------------------------------------------------
import re

def compress():
   string =  re.sub('[ \t\n]+',' ','The     quick brown                \n\n             \t        fox')
   print string
if __name__ == '__main__':
    compress()
