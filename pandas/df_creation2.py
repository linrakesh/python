# create dataframe using list of Python Dictionary
import pandas as pd
df = pd.DataFrame(
    [
        {'admno': 1101,'name': 'rakesh','marks' :56, 'fees': 5656.56},
        {'admno': 1203, 'name':'jatin jain','marks':56, 'fees': 5666.56},
        {'admno': 1205, 'name':'pushkar','marks':78, 'fees': 5666.56},
        {'admno': 1206, 'name':'arushi','marks':98, 'fees': 4564.34},
        {'admno': 1208, 'name':'mannat bhatia','marks':89, 'fees': 4500}
    ]
)
print(df)
