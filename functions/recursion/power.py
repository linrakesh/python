def xpower(x,y):
    if y ==1 :
        return x
    else:
        return (x*xpower(x,y-1))

x = int(input("Enter x : "))
y  = int (input("Enter y : "))
result = xpower(x,y)

print("\n\n {} power {} is {} ".format(x,y,result))