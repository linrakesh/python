''' program to swap first half element with last half element
    made by         : rakesh kumar
    last edited on  : 30-august 2019 '''

x = [1, 24, 5, 7, 8, 9, 10, 56, 78, 89, 56, 67]
n = len(x)
for i in range(n//2):
    x[i], x[n-1-i] = x[n-1-i], x[i]

print(x)
