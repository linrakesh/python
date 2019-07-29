#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      acer
#
# Created:     12-04-2018
# Copyright:   (c) acer 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import MySQLdb


def show_records():
    db = MySQLdb.connect("localhost", "root", "ramji", "cable")
    cursor = db.cursor()
    sql = "select * from customer"
    cursor.execute(sql)
    results = cursor.fetchall()
    for idr, name, fname, add, phone, email in results:
        print(idr, name, fname, phone, email)
    db.close()


def del_record():
    db = MySQLdb.connect("localhost", "root", "ramji", "cable")
    cursor = db.cursor()
    name = input("Enter name you want to delete")
    sql = "delete from customer where name like '%" + name + "'%"
    cursor.execute(sql)
    db.commit()
    db.close()
    print("Record Deleted successfully")


def update_record():
    db = MySQLdb.connect("localhost", "root", "ramji", "cable")
    cursor = db.cursor()
    email = input("Admin ID :")
    sql = "update customer set  email = 'admin@binarynote.com where email like '%" + email + "'%"
    cursor.execute(sql)
    db.commit()
    db.close()
    print("Record Updated successfully")


def main():
    n = 1
    while n != 4:
        n = int(input("Enter any no (1..3) "))
        print(n)
        if n == 1:
            show_records()
        if next == 2:
            del_record()
        if next == 3:
            update_record()


if __name__ == '__main__':
    main()
