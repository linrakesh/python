#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      acer
#
# Created:     01-02-2018
# Copyright:   (c) acer 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    n = int(input ("Enter total no of items in List"))
    list = []
    while n!=0:
        item = input("Enter list item")
        list.append(item)
        n= n-1
    print("Here is your Generated List :")
    print(list)
    choice = input("Do you want to change ?")
    if(choice =="yes"):
        newitem = input("Enter current list item name")
        list.remove(newitem)
        newitem = input("Enter new list item name")
        list.append(newitem)
        print("Your final modified list ")
    else:
        print("Original List ")
    print(list)
if __name__ == '__main__':
    main()
