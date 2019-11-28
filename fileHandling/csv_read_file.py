# Python program to read csv file


import csv

file = open("08849.csv", "r")
csv_reader = csv.reader(file)
count = 0
for x in csv_reader:
    print(x)
    count += 1

file.close()
print('Total rows {}'.format(count))
