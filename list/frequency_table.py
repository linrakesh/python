list1 = [1, 2, 3, 4, 5, 6, 7, 8, 1, 3, 2, 4, 2, 1, 5, 6, 7, 2, 3, 4, 1]

num = []
freq = []

for i in list1:
    if i not in num:
        num.append(i)
        count = list1.count(i)
        freq.append(count)

for i in range(len(num)):
    print(num[i], 'appear', freq[i], 'times')
