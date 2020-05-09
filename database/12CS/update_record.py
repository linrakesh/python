import MySQLdb
db = MySQLdb.connect('localhost', 'root', '', 'davschool')
cursor = db.cursor()
cursor.execute('update games set gname ="fun with rakesh " where id=5')
db.close()
print('Record updated successfully')
