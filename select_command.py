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
# Open database connection
db = MySQLdb.connect("localhost","root","ramji","cable" )
cursor = db.cursor();
sql ="select * from customer"
cursor.execute(sql)
results = cursor.fetchall()
#print( "ID    Name      Father Name              Address")
for idr,name,fname,add,phone,email in results:
    #idr = record[0]
    #name = record[1]
    #fname = record[2]
    #add = record[3]
    print(idr,name,fname,add,phone,email)
db.close()