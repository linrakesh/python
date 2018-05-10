x =[3,56,2,56,78,56,34,23,4,78,8,123,45]
for i in range(0,12):
    pos = i 
    low = x[pos]
    for j in range(i+1,13):
        if(low>x[j]):
            pos = j
            low = x[j]
    x[i],x[pos] = x[pos],x[i]

print("Sorted Array :")            
for i in x:
    print(i,end =" ")