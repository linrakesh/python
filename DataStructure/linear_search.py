
#wrong way to find data
x =[1,2,3,5,7,89,3,62,34,13,5,7,9]
data = 89
''' found =0
for i in x:
    if i ==data:
       found =1
if(found ==0):
    print("Data not found")
else:
    print("Data found") '''

# good way to search data in python
if data in x:
    print('found')
else:
    print('not found')
