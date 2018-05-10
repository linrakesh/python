x =[3,56,2,56,78,56,34,23,4,78,8,123,45]
for i in range(1,13):
    for j in range(0,13-i):
        if(x[j]>x[j+1]):
            x[j],x[j+1] = x[j+1],x[j]

print("Sorted Array :")            
for i in x:
    print(i,end =" ")