import MySQLdb
db = MySQLdb.connect('localhost', 'root', '', 'davschool')
cursor = db.cursor()
cursor.execute('select * from games;')
rows = cursor.rowcount
db.close()
print('Total number of records :',rows)