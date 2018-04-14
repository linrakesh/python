#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      acer
#
# Created:     31-01-2018
# Copyright:   (c) acer 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def sum_digit(a):
    sum =0;
    while a!=0:
        rem = a%10
        sum = sum + rem
        a = int(a / 10)
    return sum

if __name__ == '__main__':
   print(" Sum of digit :"+ str(sum_digit(123)))
