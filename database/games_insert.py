import MySQLdb
db = MySQLdb.connect('localhost', 'root', 'ramji', 'davschool')
cursor = db.cursor()
cursor.execute('insert into games values(7,"cricket-new",750 )')
db.close()
