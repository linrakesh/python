from tkinter import *

def doSomething():
    print("This will print only a msg")

root = Tk()
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label='File', menu= filemenu)
filemenu.add_command(label='New Project',command=doSomething)
filemenu.add_command(label='open Project',command=doSomething)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=doSomething)

editmenu = Menu(menu)
menu.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut',command=doSomething)
editmenu.add_command(label='copy',command=doSomething)

root.mainloop()