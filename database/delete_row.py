import MySQLdb
db=MySQLdb.connect('localhost',  'root',  '',  'davschool')
cursor=db.cursor()
cursor.execute('delete from game where gname="cricket" ')
db.close()