import pandas as pd

#blank series
s = pd.Series()
print(s)

#series with numbers
s = pd.Series([10,20,30,40,50])
print(s)

#series with numbers and index

s= pd.Series([10,20,30,40,50],index=[1,2,3,4,5])
print(s)

#series with numbers and char index
s = pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])
print(s)

#series with constant values
s = pd.Series(55,index=[1,2,3,4,5,6])
print(s)

#series with constant and python function
s = pd.Series(34,index= range(100))
print(s)

# series with python function
s = pd.Series(range(2,89))
print(s)

