import pandas as pd
import numpy as np

#blank series
s = pd.Series()
print(s)

#series with numbers
s = pd.Series([10, 20, 30, 40, 50])
print(s)

#series with numbers and index

s = pd.Series([10, 20, 30, 40, 50], index=[1, 2, 3, 4, 5])
print(s)

#series with numbers and char index
s = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print(s)

#series with constant values
s = pd.Series(55, index=[1, 2, 3, 4, 5, 6])
print(s)

#series with constant and python function
s = pd.Series(34, index=range(100))
print(s)

# series with python function
s = pd.Series(range(2, 89))
print(s)

# series with float values
s = pd.Series([10, 20, 30, 40.5, 50])
print(s)

# series with string type values
s = pd.Series('Welcome to DAV Chander Nagar', index=[1, 2, 3, 4, 5, 6])
print(s)

# series with string and index also in string

s = pd.Series('Welcome to DAV Chander Nagar', index=[
              'rakesh', 'arushi', 'mannat', 'vinay', 'pratham'])
print(s)

# series with range and for loop
s = pd.Series(range(5), index=[x for x in 'abcde'])
print(s)

# series with two different lists
names = ['rakesh', 'vishank', 'nikunj', 'unnati', 'vipul']
city = ['GZB', 'Delhi', 'Meerut', 'Pune', 'Panji']
s = pd.Series(names, index=city)
print(s)


#series with Nan values of numpy

s = pd.Series([10, 20, 30, np.NaN, -34.5, 6])
print(s)

#series from a python Dictionary
dict1 = {'name': 'rakesh', 'roll': 20, 'city': 'Gzb',
         'age': 40, 'profession': 'Teaching'}
s = pd.Series(dict1)
print(s)


# series using a mathematical expression
data = np.arange(10, 15)
s = pd.Series(data**2, index=data)
print(s)
