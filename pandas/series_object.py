#   python pandas series attributes
#   series.index        - Return index onfthe series
#   series.values       - return ndarray
#   series.dtype        - return dtype object of the underlying data
#   series.shape        - return tuple of the shape of the underlying data
#   series.nbytes       - return number of bypes of underlying data
#   series.ndim         - return the number of dimension
#   series.size         - return the number of elements
#   series.hasnans      - return true if there are any Nan value
#   series.empty        - return true if series object is empty

import pandas as pd

s= pd.Series(range(3,30,3))
print(s.index)
print(s.values)
print(s.dtype)
print(s.shape)
print(s.nbytes)
print(s.ndim)
print(s.size)
print(s.hasnans)
print(s.empty)