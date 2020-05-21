import csv
f = open(r"C:\Users\rakesh\Desktop\student.csv", "r")
data = csv.DictReader(f)
for record in data:
    print(dict(record))
f.close()
