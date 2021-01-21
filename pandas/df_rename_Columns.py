import pandas as pd
data = [
    (1101, 'rakesh', 56, 5656.56),
    (1203, 'jatin jain', 56, 5666.56),
    (1205, 'pushkar', 78, 5666.56),
    (1206, 'arushi', 98, 4564.34),
    (1208, 'mannat bhatia', 89,  4500),
    (1234, 'unnati', 67, 3500.56),
    (1245, 'Nikunj Tyagi', 68, 4500),
    (5755, 'vishank', 89, 5000)
]
heading = ["admno", "name", "marks", "fees"]
df = pd.DataFrame(data, columns=heading)
#df =df.rename(columns={"fees":'Annual Fees'})
#df = df.rename({'fees':'Yealy fees'},axis=1)
df = df.rename({'fees':'yealy fees', 'marks':'ut-2'}, axis=1)
#df.rename({'fees': 'yealy fees', 'marks': 'ut-2'}, axis=1,inplace=True)
print(df)