L = ['the', 'in', 'out', 'the', 'in', 'ram', 'umesh', 'the']
d = {}

""" l = len(L)
for i in range(0, l):
    key = L.count(L[i])
    if key not in d:
        value = []
        for j in range(i, l):
            if(L.count(L[j]) == key and L[j] not in value):
                value.append(L[j])
        d[key] = value
 """

for i in L:
    c = L.count(i)
    if c not in d:
        d[c] = [i]
    elif i not in d[c]:
        d[c].append(i)
print(d)
