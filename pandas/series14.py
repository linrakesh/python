#series from a python Dictionary
import pandas as pd
dict1 = {'name': 'rakesh', 'roll': 20, 'city': 'Gzb',
         'age': 40, 'profession': 'Teaching'}
s = pd.Series(dict1)
print(s)
