#-------------------------------------------------------------------------------
# Name:        factorial
# Purpose:     To display large numbers
#
# Author:      rakesh kumar
#
# Created:     18-04-2017
# Copyright:   (c) rakesh kumar
# Licence:     MIT-2.0
#-------------------------------------------------------------------------------
#! python3
fact=1
n = 100000
for i in range(1,n+1):
    fact = fact*i
print ("Factoril of" + str(n) +" is :" + str(fact))
