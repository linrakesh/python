import MySQLdb
db = MySQLdb.connect("localhost", "root", "", "binarynote")
cursor = db.cursor()
name = input("Enter current name  : ")
new_name = input("Enter new name :")
sql = "update user set uname='{}' where uname like '%{}';".format(
    name, new_name)
cursor.execute(sql)
db.commit()
db.close()
print("Row updated successfully")
