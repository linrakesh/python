#   program to demonstrate the use of yield  in a function
#   made by         : rakesh kumar


def square():
    i =1
    while True:
        yield i*i
        i+=1

for x in square():
    if(x > 100):
        break
    print(x)    
  
