from cgitb import text
from tkinter import *
from tkinter import ttk
class MyDesign():
    def __init__(self):

        self.window = Tk()

        self.window.title('PipBoy')

        radioB = Button(self.window, text ="RADIO", width=6, bg="black", fg="green")
        radioB.pack(side=TOP)

        mapB = Button(self.window, text ="MAP", width=6, bg="black", fg="green")
        mapB.pack(side=TOP)

        dataB = Button(self.window, text ="DATA", width=6, bg="black", fg="green")
        dataB.pack(side=TOP)

        invB = Button(self.window, text="INV", width=6, bg="black", fg="green")
        invB.pack(side=TOP)

        statsB = Button(self.window, text ="STATS", width=6, bg="black", fg="green")
        statsB.pack(side=TOP)

        label = Label(self.window, text = "Example text")
        label.pack(padx = 200, pady = 200)

        self.window.mainloop()

design = MyDesign()
design.root.mainloop()