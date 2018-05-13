# purpose       : write a program to print the following pattern 
#                           1
#                       1   2   1
#                   1   2   3   2   1
#               1   2   3   4   3   2   1
#           1   2   3   4   5   4   3   2   1
#       1   2   3   4   5   6   5   4   3   2   1
#
# author        : rakesh kumar
# licence       : MIT



for i in range(1,10):
    for j in range(10-i):
      print(' ', end=" ")
    for k in range(1,i+1):
        print(chr(k+64), end=" ")
    for l in range(i-1,0,-1):
        print(chr(l+64),end=" ")
    print()