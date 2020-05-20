# create dataframe using Python Dictionary
import pandas as pd
df= pd.DataFrame(
    {
        'admno' :[10,12,45,56,78,88],
        'name'  :['rakesh','tarun','nikunj','arushi','pushkar','jatin'],
        'marks' :[56,67,78,99,67,56],
        'fees'  :[345.67,676.45,677,456,7687,5656]
    }
)
print(df)