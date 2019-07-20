#program to show how numpy array consume less memory space and runs faster 
# written by        : rakesh kumar
# last revised on   : 20-july-2019

import numpy as np
import time
import sys

l = range(10000)
print(sys.getsizeof(5)*len(l))

array = np.arange(10000)
print(array.size*array.itemsize)


# time comparision
size= 1000000
l1 = range(size)
l2 = range(size)

n1 = np.arange(size)
n2 = np.arange(size)

start = time.time()  #capture starting time
result = [(x+y) for x,y in zip(l1,l2)]
print("List took :",(time.time()-start)*1000)

start = time.time()  #start time again
result = n1+n2
print("Numpy took :",(time.time()-start)*1000)