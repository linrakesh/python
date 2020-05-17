import csv
name = input('Name to Search :')

file = open('student.csv','r')
reader = csv.DictReader(file)
found =0
for x in reader:
    x = dict(x)
    if(x['name']==name):
        print(name,' found in CSV file..')
        found =1
file.close()

if(found == 0):
    print(name, ' not found....')