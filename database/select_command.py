#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      acer
#
# Created:     12-04-2018
# Copyright:   (c) acer 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import MySQLdb
from prettytable import PrettyTable
# Open database connection
db = MySQLdb.connect("localhost","root","ramji","cable" )
cursor = db.cursor()
cnt = cursor.execute("select count(*) from customer")
sql ="select * from customer"
cursor.execute(sql)
results = cursor.fetchall()
#print( "ID    Name      Father Name              Address")
print("\n Total records ",cnt)
t = PrettyTable(['ID','Name','FatherName','Address','Phone','Email'])
for idr,name,fname,add,phone,email in results:
    #idr = record[0]
    #name = record[1]
    #fname = record[2]
    #add = record[3]
    t.add_row([idr,name,fname,add,phone,email])
    # print(idr,name,fname,add,phone,email)
print(t)
db.close()