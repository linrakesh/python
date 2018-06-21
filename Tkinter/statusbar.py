from tkinter import *
root = Tk()

status = Label(root,text="This is status Bar of my app",bd=1,relief=SUNKEN,anchor=W)
#bd = border 
#anchor = alignment and in tkinterr W means west - so left aligned
status.pack(side=BOTTOM,fill=X)

root.mainloop()