from tkinter import *
root = Tk()

def printName(event):
    print("hello my name is rakesh ")

button1= Button(root,text="Print my Name")
button1.bind('<Button-1>',printName)

button1.pack()
root.mainloop()