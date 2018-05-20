# Program to print character paralleogram
# made by           : rakesh kumar
# Licence           : MIT
def printString(string):
    n = len(string)
    for i in range(0,n):
        print(string[i],end=" ")

string  = "TESTINGPROGRAM"
n = len(string)
# print(n)
for i in range(1,n+1):
    for j in range(i,n):
        print("  ",end="")
    printString(string[0:i])
    print()
for i in range(1,n+1):
    printString(string[i:])
    print()