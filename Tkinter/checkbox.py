from tkinter import *
master = Tk()

def var_states():
   print("male: %d,\nfemale: %d" % (var1.get(), var2.get()))

label = Label(master, text="Your sex:")
label.grid(row=0, sticky=W)

var1 = IntVar()
checkbox1= Checkbutton(master, text="male", variable=var1)
checkbox1.grid(row=1, sticky=W)

var2 = IntVar()
checkbox2= Checkbutton(master, text="female", variable=var2)
checkbox2.grid(row=2, sticky=W)

button1= Button(master, text='Quit', command=master.quit)
button1.grid(row=3, sticky=W, pady=4)

button2= Button(master, text='Show Results', command=var_states)
button2.grid(row=4, sticky=W, pady=4)
mainloop()