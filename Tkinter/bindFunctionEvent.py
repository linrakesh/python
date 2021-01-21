from tkinter import *
root = Tk()

def printName(event):
    print("hello my name is rakesh ")

button1= Button(root,text="Print my Name")
button2= Button(root,text="Print my Name-2")
button3= Button(root,text="Print my Name-3")
button4= Button(root,text="Print my Name-4")
button5= Button(root,text="Print my Name-5")

button1.bind('<Button-1>',printName)
button2.bind('<Button-2>',printName)
button3.bind('<Button-3>',printName)
button4.bind('<Button-4>',printName)
button5.bind('<Button-5>',printName)

button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
root.mainloop()