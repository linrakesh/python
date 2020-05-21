import pandas as pd
import numpy as np

s = pd.Series(np.arange(2,20,2))
print(s[2])    # show value at index 2
print(s[1:])   # display all element from 1 index onward
print(s[:4])   # display values present at index 0,1,2,3
print(s[1::2]) # display value present at index 1,3,5,7