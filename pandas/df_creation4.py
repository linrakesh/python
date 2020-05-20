# create python pandas using Excel file
import pandas as pd
df = pd.read_excel("result.xls","result")
print(df)