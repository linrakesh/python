import csv
f = open(r"C:\Users\rakesh\Desktop\student.csv", "r")
data = csv.reader(f)
for record in data:
    print(record)
f.close()
