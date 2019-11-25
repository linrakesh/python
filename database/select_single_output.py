# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      acer
#
# Created:     12-04-2018
# Copyright:   (c) acer 2018
# Licence:     <your licence>
# -------------------------------------------------------------------------------

import MySQLdb
from prettytable import PrettyTable
# Open database connection
db = MySQLdb.connect("localhost", "root", "", "binarynote")
cursor = db.cursor()
sql = "select count(*) from question"
cursor.execute(sql)
result = cursor.fetchone()
print(result[0])
db.close()
