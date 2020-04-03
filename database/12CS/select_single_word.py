import MySQLdb
db = MySQLdb.connect('localhost', 'root', '', 'davschool')
cursor = db.cursor()
cursor.execute('select gname from games where id=6')
game_name = cursor.fetchone()
print('Your Game is :', game_name)
db.close()
