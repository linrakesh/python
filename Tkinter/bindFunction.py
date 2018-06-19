from tkinter import *
root = Tk()

def printName():
    print("hello my name is rakesh ")

button1= Button(root,text="Print my Name",command=printName)

button1.pack()
root.mainloop()