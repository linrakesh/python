#   program to convert json file in to csv file
#   program by      : rakesh kumar
#   last edited     : 14/01/2020

import json
with open(r"C:/Users/rakesh\Desktop/python/jsonFile.json") as json_file:
    data = json.load(json_file)
    single=0
    header=[]
    data=[]
    for x in data:
        if single==0:
            for y in x:
                header.append(y)
            break;
        else:
            for z in data:
                data.append(z[])
    print(header)