# series using a mathematical expression
import pandas as pd
import numpy as np
data = np.arange(10, 15)
s = pd.Series(data**2, index=data)
print(s)
