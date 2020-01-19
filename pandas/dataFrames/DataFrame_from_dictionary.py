#   Pandas DataFrame from python dictionary
import pandas as pd

student ={'name':['rakesh','suresh','disha','arun','gulati','unnati'],'IP':[56,78,56,78,78,67],'English':[67,78,87,67,78,34],'Pol':[55,78,88,56,90,94]}
df= pd.DataFrame(student)
print(df)
print(df[:3])
print(df.head(3))
print(df.tail(2))