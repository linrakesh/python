x =[1,2,3,4,5,6,7,8]
y = [1,2,3,4,5]
z = []
i=j=k=0
while(i<8 and j <5):
    if(x[i]<y[j]):
        z.append(x[i])
        i = i+1
    else:
        z.append(y[j])
        j = j+1
while(i<8):
    z.append(x[i])
    i = i+1
while(j<5):
    z.append(y[j])
    j= j+1

#display concatenated list 
print("\n Merged array : ")
for i in z:
    print(i,end=" ")