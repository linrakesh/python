import csv
import json
with open('e:/python/tools/SampleData.csv') as csf_file:
    csv_reader = csv.reader(csf_file)
    line = 0
    keys = []
    jon = []
    for row in csv_reader:
        d = {}
        if line == 0:
            for col in row:
                keys.append(col)
        else:
            for i in range(len(row)):
                d[keys[i]] = row[i]

        if(line >= 1):
            jon.append(d)
        line += 1
# print(jon)

with open("jsonFile.json", "w") as json_file:
    json_file.write(json.dumps(jon,))
