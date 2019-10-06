''' program to arrange list element using bubble sort metod
    made by             : rakesh kumar
    last edited         :20-aug-2019'''

x = [23, 5, 67, 8, 324, 6, 89, 9, 23, 1, 4, 89]
n = len(x)
for i in range(n-1):
    for j in range(n-i-1):
        if x[j] > x[j+1]:
            x[j], x[j+1] = x[j+1], x[j]

print(x)
