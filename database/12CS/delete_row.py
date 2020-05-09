import MySQLdb
db = MySQLdb.connect('localhost', 'root', '', 'davschool')
cursor = db.cursor()
cursor.execute('delete from games  where id=6')
db.close()
print('record deleted')
