import MySQLdb
db = MySQLdb.connect('localhost', 'root', '', 'davschool')
cursor = db.cursor()
cursor.execute('select id,gname from games')
game_name = cursor.fetchall()
print('Your Game is :', game_name)
print('Game Id :', game_name[0])
print('Game name :', game_name[1])
db.close()
