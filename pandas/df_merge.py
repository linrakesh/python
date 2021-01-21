import pandas as pd

right = pd.DataFrame({'admno': ['101', '102', '103', '104'],
                      'Game': ['Cricket', 'BasketBall', 'Badminton', 'Swimming'],
                      'Fee': [1200, 750, 800, 1500]})
print(right['Fee'].count())
print(right['Fee'].max())
print(right['Fee'].min())
print(right['Fee'].sum())
print(right['Fee'].mean()) #average
print(right['Fee'].median()) #average
print(right['Fee'].std()) #standard daviation
print(right['Fee'].var()) #standard variance
print(right['Fee'].quantile())  # quantile of the values
