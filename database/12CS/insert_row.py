import MySQLdb
db = MySQLdb.connect('localhost', 'root', '', 'davschool')
cursor = db.cursor()
cursor.execute('insert into games values (7,"fun with class xii")')
db.close()
print('Record added successfully')
