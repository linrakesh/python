def common(l1, l2):
    c = list()
    for x in l1:
        if x in l2:
            c.append(x)
    return c


l1 = [1, 2, 3, 4, 6, 8, 9]
l2 = [2, 4, 6, 7, 9, 10]

print(common(l1, l2))
