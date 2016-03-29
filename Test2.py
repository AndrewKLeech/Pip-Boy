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

        radio = Button(self.window, text ="RADIO", bg="black", fg="green", width = 10)
        radio.grid(row = 0, column=1)

        map = Button(self.window, text ="MAP", bg="black", fg="green", width = 10)
        map.grid(row =0, column=2)

        data = Button(self.window, text="DATA", bg="black", fg="green", width = 10)
        data.grid(row = 0, column=3)

        inv = Button(self.window, text ="INV", bg="black", fg="green", width = 10)
        inv.grid(row = 0, column=4)

        stats = Button(self.window, text ="STATS", bg="black", fg="green", width = 10)
        stats.grid(row = 0, column=5)

        photo = "mrPip.gif"

        img = ImageTk.PhotoImage(Image.open(photo))
        tile = Label(self.window, image = img)
        tile.grid(row = 3, column = 3, columnspan = 2)


        self.window.mainloop()

design = MyDesign()
design.mainloop()