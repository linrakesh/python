from tkinter import *

def button1Click():
    print("Button1 clicked and this will do nothing")

def button2Click():
    print("Button2 clicked")

root = Tk()
toolbar = Frame(root,bg='red')

button1 = Button(toolbar,text="Button1",command =button1Click)
button1.pack(side=LEFT)

button2 = Button(toolbar,text="Button2",command =button2Click)
button2.pack(side=LEFT)

toolbar.pack(side=TOP,fill=X)

root.mainloop()