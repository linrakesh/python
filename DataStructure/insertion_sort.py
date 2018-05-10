x =[3,56,2,56,78,56,34,23,4,78,8,123,45]
for i in range(1,13):
    j= i-1 
    temp = x[i]
    while(temp<x[j] and j>=0):
        x[j+1]=x[j]
        j = j-1
    x[j+1] = temp
    
print("Sorted Array :")            
for i in x:
    print(i,end =" ")