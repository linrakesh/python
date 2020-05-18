
#series with Nan values of numpy
import pandas as pd
import numpy as np
s = pd.Series([10, 20, 30, np.NaN, -34.5, 6])
print(s)
