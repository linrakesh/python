#-------------------------------------------------------------------------------
# Name:        insert row
# Purpose:     add a new record in any existing database table
#
# Author:      rakesh kumar
#
# Created:     12-04-2018
# Copyright:   (c) acer 2018
# Licence:     MIT
#-------------------------------------------------------------------------------
import MySQLdb
from prettytable import PrettyTable

def del_record(cursor):
    data = input("Enter something related to your record :")
    sql =  "delete from customer where name like '%"+data+"%' or fname like '%"+data+"%' or address like '%"+data+"%'"
    sql =  sql +" or phone like '%"+data+"%' or email like '%"+data +"%'"
    cursor.execute(sql)

def show_result(cursor):
    sql ="select * from customer"
    cursor.execute(sql)
    results = cursor.fetchall()
    t = PrettyTable(['ID','Name','FatherName','Address','Phone','Email'])
    for idr,name,fname,add,phone,email in results:
        t.add_row([idr,name,fname,add,phone,email])
    print(t)

def input_data(cursor):
    admno = input("Enter Admno : ")
    name  = input("Enter student Name : ")
    fname  = input("Enter Father Name : ")
    address = input("Enter Address : ")
    phone = input ("Enter any valid Phone NO :")
    email  = input("Enter any valid Email ID : ")
    """ create cursor to generate/ execute sql statement"""
    sql = "insert into customer values (" + admno + ",'"+name+"','"+fname+"','"+address+"','"+phone+"','"+email+"');"
    # print(sql)
    cursor.execute(sql)

"""MAIN PROGRAM START FROM HERE """

if __name__=='__main__':
    db = MySQLdb.connect("localhost","root","ramji","cable")
    cursor = db.cursor()
    # sql ="insert into customer values(20,'rakesh','jagdish','cf-4 arun vihar','12121212','arun@bin.com');"
    # cursor.execute(sql)
    input_data(cursor)
    db.commit()
    show_result(cursor)
    del_record(cursor)
    db.commit()
    show_result(cursor)
    db.close()
    