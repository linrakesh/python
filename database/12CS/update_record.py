import MySQLdb
db = MySQLdb.connect('localhost', 'root', '', 'davschool')
cursor = db.cursor()
cursor.execute('update games set gname ="fun with python " where id=6')
db.close()
print('Record updated successfully')
