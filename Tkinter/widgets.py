from tkinter import *
root = Tk()
one = Label(root,text="My Label",bg="red", fg="green")
one.pack(fill=X)
two = Label(root,text="second Label", bg="green" , fg="white")
two.pack()
three = Label(root,text="Third Label",bg="blue",fg="yellow")
three.pack(side=LEFT,fill=Y)
root.mainloop()