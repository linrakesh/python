from tkinter import *
import  tkinter.messagebox
import tkinter.simpledialog
root = Tk()

""" 
yesno  = tkinter.messagebox.askyesno('Question',"Are you sure to delete this record ?")
tkinter.messagebox.askokcancel()
tkinter.messagebox.askquestion()
tkinter.messagebox.askretrycancel()
tkinter.messagebox.askyesnocancel()

if yesno ==True :
    print("You selected to delete record") 
 """

no = tkinter.simpledialog.askstring('List Input','Enter number ')
no = no.split()
print(no)

root.mainloop()
