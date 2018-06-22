from tkinter import *

def showresult():
    print("Value of v is ",v.get())

root = Tk()
v = IntVar()
Label(root, text="Choose a programming language:",justify = LEFT, padx = 20).grid(row=1)
Radiobutton(root, text="Python", padx = 20, variable=v, value=0).grid(row=2)
Radiobutton(root, text="Perl",   padx = 20, variable=v, value=1).grid(row=3)

Button(root,text="Show Result",command=showresult).grid(row=4)
root.mainloop()