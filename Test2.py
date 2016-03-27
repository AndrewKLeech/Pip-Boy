from cgitb import text
from tkinter import *
from PIL import Image, ImageTk


class MyDesign():
    def __init__(self):

        self.window = Tk()
        self.window.title('PipBoy')
        self.window.configure(bg = "black")
        self.window.geometry('400x300')

        self.window.columnconfigure((0,2), weight=1)

        label = Label(self.window, text = "Example text")

        radio = Button(self.window, text ="RADIO", width=10, bg="black", fg="green")
        radio.grid(row = 0, column=1)

        map = Button(self.window, text ="MAP", width=10, bg="black", fg="green")
        map.grid(row =0, column=2)

        data = Button(self.window, text="DATA", width=10, bg="black", fg="green")
        data.grid(row = 0, column=3)

        inv = Button(self.window, text ="INV", width=10, bg="black", fg="green")
        inv.grid(row = 0, column=4)

        stats = Button(self.window, text ="STATS", width=10, bg="black", fg="green")
        stats.grid(row = 0, column=5)

        img = PhotoImage(file = "pip-boy.gif")
        label = Label(self.window, image = img, bg = "black")


        self.window.mainloop()

design = MyDesign()
design.mainloop()