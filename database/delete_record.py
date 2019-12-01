#-------------------------------------------------------------------------------
# Name:        delete_record
# Purpose:     delete a record from any existing database table
#
# Author:      rakesh
#
# Created:     12-04-2018
# Copyright:   (c) acer 2018
# Licence:     MIT
#-------------------------------------------------------------------------------

import MySQLdb
db = MySQLdb.connect("localhost","root","","binarynote")
cursor = db.cursor()
name = input("Enter any name : ")
sql ="delete from user where uname like '%" + name + "';"
cursor.execute(sql)
db.commit()
db.close()
print("Row deleted successfully")
