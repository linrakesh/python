# retirve values from pandas series using head() and tail() function

import pandas as pd
s= pd.Series(range(1,1000,5))
#print top 5 entries of the series
print(s.head())
#print top 2 entries of the series
print(s.head(2))

#print last 5 entries of the series
print(s.tail())
# print last 2 entries of the series
print(s.tail(2))
