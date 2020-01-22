#   pandas dataframes generation using different methods

import pandas as pd
df = pd.DataFrame()
print(df)

# DataFrame using python list
df = pd.DataFrame([10,20,30,40,50,60])
print(df)

# DataFrame using pandas series

marks = pd.Series({'rakesh':56,'anuj':89,'Bhumi':90,'Jagdev':80})
age  =  pd.Series({'rakesh':18,'anuj':18,'Bhumi':16,'Jagdev':19})
print(marks)
print(age)

df=pd.DataFrame({'marks':marks,'age':age})
print(df)

#sorting DataFrame values using sort_value() 
print(df.sort_values(by=['marks']))
print(df.sort_values(by=['marks'],ascending=False))