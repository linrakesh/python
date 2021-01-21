import csv
import re
import xlwt


def write2_cell(ws, row, roll, gender, name, marks):
    ws.write(row, 0, roll)
    ws.write(row, 1, name)
    ws.write(row, 2, gender)

    for values in marks.values():
        if(values[0] == '301'):
            ws.write(row, 3, values[1])
        if(values[0] == '302'):
            ws.write(row, 4, values[1])
        if(values[0] == '041'):
            ws.write(row, 5, values[1])
        if(values[0] == '042'):
            ws.write(row, 6, values[1])
        if(values[0] == '043'):
            ws.write(row, 7, values[1])
        if(values[0] == '283'):
            ws.write(row, 8, values[1])
        if(values[0] == '265'):
            ws.write(row, 9, values[1])
        if(values[0] == '044'):  # biology
            ws.write(row, 10, values[1])
        if(values[0] == '048'):  # physical
            ws.write(row, 11, values[1])
        if(values[0] == '030'):     # economics
            ws.write(row, 12, values[1])
        if(values[0] == '055'):     # Accounts
            ws.write(row, 13, values[1])
        if(values[0] == '054'):     # BST
            ws.write(row, 14, values[1])
        if(values[0] == '812'):  # marketing
            ws.write(row, 15, values[1])
        if(values[0] == '028'):  # Pol science
            ws.write(row, 16, values[1])
        if(values[0] == '034'):  # music
            ws.write(row, 17, values[1])
        if(values[0] == '049'):  # music
            ws.write(row, 18, values[1])


file = open(r'C:\Users\rakesh\Desktop\z60074.txt', 'r')
rows = csv.reader(file)
wb = xlwt.Workbook()
ws = wb.add_sheet("result")
""" ws1 = wb.add_sheet("result1") """

st = xlwt.easyxf('font: bold yes;align: horiz centre , vert centre ,wrap yes')
ws.write(0, 0, "Roll No", st)
ws.write(0, 1, "Student Name", st)
ws.write(0, 2, "Gender", st)
ws.write(0, 3, "English", st)
ws.write(0, 4, "Hindi", st)
ws.write(0, 5, "Maths", st)
ws.write(0, 6, "Physics", st)
ws.write(0, 7, "Chemistry", st)
ws.write(0, 8, "CS", st)
ws.write(0, 9, "IP", st)
ws.write(0, 10, "Bio", st)
ws.write(0, 11, "Physical", st)
ws.write(0, 12, "Eco", st)
ws.write(0, 13, "Account", st)
ws.write(0, 14, "Bst", st)
ws.write(0, 15, "marketing", st)
ws.write(0, 16, "Pol Sci", st)
ws.write(0, 17, "Music", st)
ws.write(0, 18, "ART", st)
ws.write(0, 19, "result", st)

n = 1
count = 0
for row in rows:
    if(len(row) <= 0):
        continue
    else:
        count += 1
        line1 = ''.join(row)
        line2 = re.sub(' +', ' ', line1)
        line3 = line2.split(' ')
        if(count % 2 == 1):
            sub = {}
            roll = line3[0]
            gender = line3[1]
            name = line3[2] + " " + line3[3]
            number = False
            try:
                sub[1] = ['' . join(line3[4])]
                sub[2] = ['' . join(line3[5])]
                sub[3] = ['' . join(line3[6])]
                sub[4] = ['' . join(line3[7])]
                sub[5] = ['' . join(line3[8])]
                if(line3[9][0].isdigit()):
                    sub[6] = ['' . join(line3[9])]
                    number = True
            except:
                continue

        else:
            try:
                sub[1].append(line3[1])
                sub[2].append(line3[3])
                sub[3].append(line3[5])
                sub[4].append(line3[7])
                sub[5].append(line3[9])
                if number:
                    sub[6].append(line3[11])
            except:
                print(roll, name, line3)
                continue

        if(count % 2 == 0):
            write2_cell(ws, n, roll, gender, name, sub)
            n = n+1

wb.save(r"C:\Users\rakesh\Desktop\result123.xls")
print('File Generated.....Please check your file')
