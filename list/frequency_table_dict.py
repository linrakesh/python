''' program to find out frequency of each element in a list using dictionary
    made by             : rakesh kumar
    last compiled on    : 10-08-2018
'''

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 1, 3, 2, 4, 2, 1, 5, 6, 7, 2, 3, 4, 1]
freq = {}
for i in list1:
    if i not in freq:
        count = list1.count(i)
        freq[i] = count

for i in freq:
    print(i, 'appear', freq[i], 'times')
