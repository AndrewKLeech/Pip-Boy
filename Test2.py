from cgitb import text
from tkinter import *
from tkinter import ttk

window  = Tk()

window.title('PipBoy')

radioB = Button(window, text ="RADIO", width=6, bg="black", fg="green")
radioB.pack(side=TOP)

mapB = Button(window, text ="MAP", width=6, bg="black", fg="green")
mapB.pack(side=TOP)

dataB = Button(window, text ="DATA", width=6, bg="black", fg="green")
dataB.pack(side=TOP)

invB = Button(window, text="INV", width=6, bg="black", fg="green")
invB.pack(side=TOP)

statsB = Button(window, text ="STATS", width=6, bg="black", fg="green")
statsB.pack(side=TOP)

label = Label(window, text = "Example text")
label.pack(padx = 200, pady = 200)

window.mainloop()