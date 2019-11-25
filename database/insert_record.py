import MySQLdb
data = MySQLdb.connect("localhost", "root", "", "binarynote")
cursor = data.cursor()
uname = input("Enter your user ID :")
upass = input("Enter your Password :")
sql = "insert into user(uname,upass) values('{}','{}');".format(
    uname, upass)
result = cursor.execute(sql)
data.close()
if(result == 1):
    print("Record Added................")
