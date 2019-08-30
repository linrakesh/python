''' program to arrange list element using selection sort method
    made by             : rakesh kumar
    last edited         :20-aug-2019'''

x = [23, 5, 67, 8, 324, 6, 89, 9, 23, 1, 4, 89]
n = len(x)
for i in range(1, n):
    temp = x[i]
    j = i-1
    while(temp < x[j] and j >= 0):
        x[j+1] = x[j]
        j = j-1

    x[j+1] = temp

print(x)
