# series with range and for loop
import pandas as pd
s = pd.Series(range(5), index=[x for x in 'abcde'])
print(s)
