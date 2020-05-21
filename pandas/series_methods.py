import pandas as pd
marks=[]
for i in range(5):
    n = int(input("Marks :"))
    marks.append(n)

s = pd.Series(marks)
#print(s)
print(s.sort_values(ascending=True)) # False for Descending
lar = s.max()
low = s.min()
summ = s.sum()
noe = len(s)
print('Maximum values :', lar)
print('Minimum values :', low)
print('Sum of values :', summ)
print('Average value ', summ/noe)