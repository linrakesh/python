# mathematical operation on pandas series

import pandas as pd
s= pd.Series(range(10))
s1 = pd.Series(range(20,30))
print(s)
print(s1)

s2 = s+s1
print("s2 = s+s1")
print(s2)

s2 = s+50
print("s2= s+50")
print(s2)

s2 = s*s1
print("s2= s*s1")
print(s2)