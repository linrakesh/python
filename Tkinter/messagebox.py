from tkinter import *
import  tkinter.messagebox
root = Tk()

tkinter.messagebox.showinfo('Window Title','This is the message')
answer = tkinter.messagebox.askyesno('Question',"Are you sure to delete this record ?")
if answer ==True :
    print("You selected to delete record")

root.mainloop()