# series with two different lists
import pandas as pd
names = ['rakesh', 'vishank', 'nikunj', 'unnati', 'vipul']
city = ['GZB', 'Delhi', 'Meerut', 'Pune', 'Panji']
s = pd.Series(names, index=city)
print(s)