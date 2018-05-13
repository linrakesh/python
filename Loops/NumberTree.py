# purpose       : write a program to print the following pattern 
#                           1
#                       1   2   
#                           1   2   3   
#                1  2   3   4 
#                           1  2   3   4   5
#       1   2   3   4   5   6
# author        : rakesh kumar
# licence       : MIT

n = int(input("Enter value of n  : "))
for i in range(1,n+1):
    if(i%2!=0):
        for j in range(n+1,i,-1):
            print(' ', end=" ")
    else:
        for j in range(n+1,1,-1):
            print(' ', end=" ")
    for k in range(1,i+1):
        print(k, end=" ")
    print()