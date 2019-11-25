# program to find out frequency of each element in a list using dictionary
#   made by           : rakesh kumar

list1 = [1, 2, 3, 4, 5, 6, 7, 34, 2, 2, 2, 4, 6, 7, 7, 8, 9]
freq = {}
for x in list1:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

print(freq)

# altername method to find out
list1 = [1, 2, 3, 4, 5, 6, 7, 34, 2, 2, 2, 4, 6, 7, 7, 8, 9]
freq = {}
for x in list1:
    if x not in freq:
        freq[x] = list1.count(x)

print(freq)
