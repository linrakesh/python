# program to update a record in csv file
import csv
name = input('Name to Update :')
records = []
found = 0
file = open("student.csv", "r")
reader = csv.DictReader(file)
for record in reader:
    record = dict(record)
    if(record['name'] == name):
        record = dict(record)
        record['name'] =input('New Name:')
        records.append(record)
        found=1
    else:
        records.append(dict(record))
file.close()

# Remove the old file and create a new csv file
pr
headers = ['rollno', 'name', 'stream', 'fees']
file = open("student.csv", "w")
writer = csv.DictWriter(file, fieldnames=headers, lineterminator='\n')
writer.writeheader()
writer.writerows(records)
file.close()

if(found == 0):
    print(name, " does not exists")
else:
    print(name, " updated successfully")
