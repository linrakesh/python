from tkinter import *
from tkinter import Tk,scrolledtext,filedialog,messagebox,END,simpledialog,colorchooser
import datetime
import os

def cut():
    textarea.clipboard_clear()
    textarea.clipboard_append(textarea.selection_get())
    textarea.delete(SEL_FIRST, SEL_LAST)

def copy():
    textarea.clipboard_clear()
    textarea.clipboard_append(textarea.selection_get()) 

def paste():
    try:
        text = textarea.selection_get(selection='CLIPBOARD')
        textarea.insert(INSERT, text)
    except:
        messagebox.showerror("Error","Nothing to Paste")

def clear():
    sel = textarea.get(SEL_FIRST, SEL_LAST)
    textarea.delete(SEL_FIRST, SEL_LAST)

def clearall():
    textarea.delete(1.0 , END)

def line():
    lin = "_" * 80
    textarea.insert(INSERT,"\n"+lin)

def date():
    data = datetime.date.today()
    textarea.insert(INSERT,data)

def background():
    color = colorchooser.askcolor()
    print(color)
    if color:
       textarea.config(background=color[1])

def foreground():
    cl = colorchooser.askcolor()
    if cl:
       textarea.config(foreground=cl[1])

def normal():
    textarea.config(font = ("Arial", 12))

def bold():
    textarea.config(font = ("Arial", 12, "bold"))

def underline():
    textarea.config(font = ("Arial", 12, "underline"))

def italic():
    textarea.config(font = ("Arial",12,"italic"))



def NewFile():
    if len(textarea.get('1.0',END+'-1c'))>0:
        yesno = messagebox.askyesno('Save File',"Do you Want to save this File?")
        if yesno:
            SaveFile()
        textarea.delete('1.0',END)

    root.title("Python TextEditor")

def OpenFile():
    file = filedialog.askopenfile(parent=root,mode="rb",title="Select a Text File", filetypes =(("Text Files","*.txt"),("All Files","*.*")))
    root.title(os.path.basename(file.name)+" - Python TextEditor")
    if file!=NONE:
        contents = file.read()
        textarea.insert('1.0',contents)
        file.close()

def SaveFile():
    file = filedialog.asksaveasfile(mode='w',defaultextension=".txt",filetypes =(("Text Files","*.txt"),("HTML","*.html"),('All Files','*.*')))
    if file != None:
        #remove last character and Enter is always added in this file as ENTER 
        data = textarea.get('1.0',END+'-1c')
        file.write(data)
        file.close()

def FindinFile():
    findStr = simpledialog.askstring("Find...","Enter Text")
    data = textarea.get('1.0',END)
    counter = data.count(findStr)
    if counter>0 :
        messagebox.showinfo("Result", str(findStr) +" has been appear "+ str(counter) +" Times")
    else:
        messagebox.showinfo("Result","We are not able to find your data" + str(findStr) )

def ExitCode():
    ask = messagebox.askyesno("Quit","Are you sure to quit")
    if ask:
        root.destroy()

def aboutus():
    messagebox.showinfo('About us',"Python Alternative of NotePad")

# main window thaat will get all the data on the sc
root = Tk(className="Python TextEditor")
textarea = scrolledtext.ScrolledText(root,width=180,height=100)

#status bar
status = Label(root,text="This is status Bar of my Text Editor",bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)

#generate menu system for our Text Editor
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label='New', command=NewFile)
filemenu.add_command(label='Open', command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label='Save', command=SaveFile)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=ExitCode)

editmenu = Menu(menu)
menu.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label='Cut',command=cut)
editmenu.add_command(label='Copy',command=copy)
editmenu.add_command(label='Paste',command=paste)
editmenu.add_separator()
editmenu.add_command(label='Find',command=FindinFile)
editmenu.add_separator()
editmenu.add_command(label='line',command=line)
editmenu.add_command(label='Date',command=date)
editmenu.add_command(label='Clear',command=clear)
editmenu.add_separator()
editmenu.add_command(label='Foreground',command=foreground)
editmenu.add_command(label='Background',command=background)

fontmenu =Menu(menu)

menu.add_cascade(label="Font",menu=fontmenu)
fontmenu.add_command(label='Normal',command=normal)
fontmenu.add_command(label='Bold',command=bold)
fontmenu.add_command(label='Italic',command=italic)
fontmenu.add_command(label='Underline',command=underline)


helpmenu = Menu(menu)
menu.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About us',command=aboutus)

textarea.pack()
textarea.focus_set()
root.mainloop()