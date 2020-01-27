import csv
import json

data = []
keys = []
with open("E:/python/Tools/SampleData.csv") as csv_file:
    csv_data = csv.reader(csv_file)
    count = 1
    for row in csv_data:
        if count == 1:
            for y in row:
                keys.append(y)
        else:
            element = {}
            for y in range(len(row)):
                element[keys[y]] = row[y]
            data.append(element)
        count = count+1

print(json.dumps(data,))
