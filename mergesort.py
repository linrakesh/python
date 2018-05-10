x = [10,20,30,40,50]
y = [14,20,25,30]
z = []
i=j=k=0
while(i<5 and j<4):
    if(x[i]<y[j]):
        z.append(x[i])
        i = i+1
    else:
       z.append(y[j])
       j = j+1
while(i<4):
    z.append(x[i])
    i = i+1
while(j<5):
    z.append(y[j])
    j = j+1
print(z)

      