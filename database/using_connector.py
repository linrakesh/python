import mysql.connector
conn = mysql.connector.connect(host='localhost',database='davschool',user='root',password='')
cursor = conn.cursor()
cursor.execute('insert into games values(4,"fun with python",1500)')
conn.close()
print('Record inserted successfully')