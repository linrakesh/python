x =[1,2,3,5,7,8,9,10,12,14,15,18,20,22]
data = 89
found =0
first=0
last =13
while (first<=last and found ==0):
    mid = int((first+last)/2)
    # print(mid)
    if(x[mid]==data):
       found =1
    if(x[mid]<data):
        first=mid+1
    if(x[mid]>data):
        last = mid-1
if(found ==0):
    print("Data not found")
else:
    print("Data found")

