#-------------------------------------------------------------------------------
# Name:        insert row
# Purpose:     add a new record in any existing database table
#
# Author:      rakesh kumar
#
# Created:     12-04-2018
# Copyright:   (c) acer 2018
# Licence:     MIT
#-------------------------------------------------------------------------------
import MySQLdb

db = MySQLdb.connect("localhost","root","ramji","cable")
cursor = db.cursor();
sql ="insert into customer values(20,'rakesh','jagdish','cf-4 arun vihar','12121212','arun@bin.com');"
cursor.execute(sql)
db.close()
print("Row inserted successfully")