import MySQLdb
db = MySQLdb.connect('localhost','root','','davschool')
cursor = db.cursor()
cursor.execute('insert into game values (12,"cricket")')
db.close()