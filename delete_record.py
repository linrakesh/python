import csv
name = input('Name to delete :')
# this is comment
# hello rakesh this is comment
""" this is multi line commnet"""

records=[]
found =0
file = open("student.csv","r")
reader = csv.DictReader(file)
for record in reader:
    record = dict(record)
    if(record['name']!=name):
        records.append(dict(record)) 
    else:
        found =1
file.close()
# Remove the old file and create a new csv file
headers=['rollno','name','stream','fees']
file = open("student.csv","w")
writer = csv.DictWriter(file,fieldnames =headers, lineterminator ='\n') 
writer.writeheader()
writer.writerows(records)
file.close()

if(found==0):
    print(name, " does not exists")
else:
    print(name," deleted successfully")
