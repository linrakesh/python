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
sql = "select * from question where qid=10"
cursor.execute(sql)
results = cursor.fetchall()
t = PrettyTable(['ID', 'Question', 'A', 'B', 'C', 'D',
                 'Ans', 'Exp', 'gid', 'sid', 'tid'])
for idr, question, a, b, c, d, ans, exp, gid, sid, tid in results:
    #idr = record[0]
    #name = record[1]
    #fname = record[2]
    #add = record[3]
    t.add_row([idr, question, a, b, c, d, ans, exp, gid, sid, tid])
    # print(idr,name,fname,add,phone,email)
print(t)
db.close()
