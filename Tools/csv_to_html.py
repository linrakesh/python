#   python program to convert any csv file into html file
#   made by         : rakesh kumar

import csv
html = "<table>"
with open("E:/python/Tools/SampleData.csv") as csv_file:
    csv_data = csv.reader(csv_file)
    count = 1
    for row in csv_data:
        html += "<tr>"
        if count == 1:
            for y in row:
                html += "<th>"+y+"</th>"
        else:
            for y in row:
                html += "<td>"+y+"</td>"
        html += "</tr>"
        count += 1

html += "</table>"
print(html)
