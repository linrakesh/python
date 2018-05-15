a  = int(input("Enter any number :"))
sum =0      
while (a!=0):
        rem = a%10
        sum = sum + rem
        a = int(a / 10)
print( sum )
