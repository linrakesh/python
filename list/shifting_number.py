#   program to shift positive number at left hand side and negative number at right hand side.

list1 = [-2, 1, -3, -15, 16, -17, 5, -3, -6]
list2 = []
n = len(list1)

for x in range(n):
    if list1[x] > 0:
        list2.append(list1[x])

for x in range(n-1, -1, -1):
    if(list1[x]) < 0:
        list2.append(list1[x])

print(list2)
