from tkinter import *

def leftClick(event):
    print("Left Mouse button clicked")

def rightClick(event):
    print("right  Mouse button clicked")

def middleClick(event):
    print("middle Mouse button clicked")

root = Tk()

frame = Frame(root, width=400, height=400)
frame.bind('<Button-1>',leftClick)
frame.bind('<Button-2>',middleClick)
frame.bind('<Button-3>',rightClick)

frame.pack()

root.mainloop()