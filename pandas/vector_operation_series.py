import pandas as pd
s = pd.Series(range(2,40))
print("Print True if Values Greater than 12 else faslse")
print(s>12)

print("Print values greater than 12")
print(s[s>12])