from tkinter import *

class myButtons:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame,text="Print Message", command = self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton  = Button(frame,text ="Quit application",command=frame.quit)
        self.quitButton.pack(side=RIGHT)

    def printMessage(self):
        print("Wow just created a class for GUI")




root = Tk()
button = myButtons(root)
root.mainloop()