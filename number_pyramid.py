#-------------------------------------------------------------------------------
# Name:        number pyramid
# Purpose:     nesting of for loop
#
# Author:      rakesh kumar
#
# Created:     18-04-2017
# Copyright:   rakesh kumar
# Licence:     MIT-2.0
#-------------------------------------------------------------------------------
import sys
def pyramid():
    n = int(input('Enter any number '))
    for i in range(1,n+1):
        for j in range(1,i+1):
            sys.stdout.write(str(j)+" ")
        print ""

if __name__ == '__main__':
   pyramid()
