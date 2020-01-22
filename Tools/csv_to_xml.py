#   python program to convert any csv file into xml file
#   made by         : rakesh kumar

import csv
xml = '<?xml version= "1.0" encoding="UTF-8" ?><rows>'
keys = []
with open("E:/python/Tools/SampleData.csv") as csv_file:
    csv_data = csv.reader(csv_file)
    count = 1
    for row in csv_data:

        if count == 1:
            for y in row:
                keys.append(y)
        else:
            xml += "<row>"
            for y in range(len(row)):
                xml += "<"+keys[y]+">"+row[y]+"</"+keys[y]+">"
            xml += "</row>"
        count += 1

xml += "</rows>"
print(xml)
