''' program to find out unique element in a list
    made by             : rakesh kumar
    last compiled on    : 10-08-2018
'''

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 1, 3, 2, 4, 2, 1, 5, 6, 7, 2, 3, 4, 1]
num = []
for i in list1:
    if i not in num:
        num.append(i)

print(num)
