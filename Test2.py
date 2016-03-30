import matplotlib
import numpy

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import tkinter as tk
import tkinter as ttk
from PIL import Image, ImageTk
from pylab import *

PIP_FONT = ("Verdana", 12)
photo = "mrPip.gif"


class SetUp(tk.Tk):  #inheriting

    def __init__(self, *args, **kwargs):  #method, initialisng

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_iconbitmap(self, default="favicon.ico")

        container = tk.Frame(self) #container for holding everything
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}  #dictionary of frames

        for F in (StartPage, RadioPage, MapPage, DataPage, InvPage, StatsPage): #loop through the number of pages

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew") #alignment plus stretch

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise() #raised to the front

class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg = "black")

        radio = tk.Button(self, text ="RADIO", bg="black", fg="green", width = 10,
                          command = lambda: controller.show_frame(RadioPage))
        radio.grid(row = 0, column=1)

        map = tk.Button(self, text ="MAP", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(MapPage))
        map.grid(row =0, column=2)

        data = tk.Button(self, text="DATA", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(DataPage))
        data.grid(row = 0, column=3)

        inv = tk.Button(self, text ="INV", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(InvPage))
        inv.grid(row = 0, column=4)

        stats = tk.Button(self, text ="STATS", bg="black", fg="green", width = 10,
                          command = lambda: controller.show_frame(StatsPage))
        stats.grid(row = 0, column=5)

        img = tk.PhotoImage(Image.open(photo))
        label = tk.Label(self, text = "photo will appear here", bg = "black", fg = "white")
        label.grid(column = 1)


class RadioPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg = "black")

        radio = tk.Button(self, text ="RADIO", bg="black", fg="green", width = 10)
        radio.grid(row = 0, column=1)

        map = tk.Button(self, text ="MAP", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(MapPage))
        map.grid(row =0, column=2)

        data = tk.Button(self, text="DATA", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(DataPage))
        data.grid(row = 0, column=3)

        inv = tk.Button(self, text ="INV", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(InvPage))
        inv.grid(row = 0, column=4)

        stats = tk.Button(self, text ="STATS", bg="black", fg="green", width = 10,
                          command = lambda: controller.show_frame(StatsPage))
        stats.grid(row = 0, column=5)

        label = tk.Label(self, text = "radio functionality", bg = "black", fg = "white")
        label.grid(row = 1, column = 1)


class MapPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg = "black")

        radio = tk.Button(self, text ="RADIO", bg="black", fg="green", width = 10,
                          command = lambda: controller.show_frame(RadioPage))
        radio.grid(row = 0, column=1)

        map = tk.Button(self, text ="MAP", bg="black", fg="green", width = 10)
        map.grid(row =0, column=2)

        data = tk.Button(self, text="DATA", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(DataPage))
        data.grid(row = 0, column=3)

        inv = tk.Button(self, text ="INV", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(InvPage))
        inv.grid(row = 0, column=4)

        stats = tk.Button(self, text ="STATS", bg="black", fg="green", width = 10,
                          command = lambda: controller.show_frame(StatsPage))
        stats.grid(row = 0, column=5)

        label = tk.Label(self, text = "map functionality", bg = "black", fg = "white")
        label.grid(row = 1, column = 1)


class DataPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg = "black")

        radio = tk.Button(self, text ="RADIO", bg="black", fg="green", width = 10,
                          command = lambda: controller.show_frame(RadioPage))
        radio.grid(row = 0, column=1)

        map = tk.Button(self, text ="MAP", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(MapPage))
        map.grid(row =0, column=2)

        data = tk.Button(self, text="DATA", bg="black", fg="green", width = 10)
        data.grid(row = 0, column=3)

        inv = tk.Button(self, text ="INV", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(InvPage))
        inv.grid(row = 0, column=4)

        stats = tk.Button(self, text ="STATS", bg="black", fg="green", width = 10,
                          command = lambda: controller.show_frame(StatsPage))
        stats.grid(row = 0, column=5)

        label = tk.Label(self, text = "data functionality", bg = "black", fg = "white")
        label.grid(row = 1, column = 1)


class InvPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg = "black")

        radio = tk.Button(self, text ="RADIO", bg="black", fg="green", width = 10,
                          command = lambda: controller.show_frame(RadioPage))
        radio.grid(row = 0, column=1)

        map = tk.Button(self, text ="MAP", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(MapPage))
        map.grid(row =0, column=2)

        data = tk.Button(self, text="DATA", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(DataPage))
        data.grid(row = 0, column=3)

        inv = tk.Button(self, text ="INV", bg="black", fg="green", width = 10)
        inv.grid(row = 0, column=4)

        stats = tk.Button(self, text ="STATS", bg="black", fg="green", width = 10,
                          command = lambda: controller.show_frame(StatsPage))
        stats.grid(row = 0, column=5)

        label = tk.Label(self, text = "inv functionality", bg = "black", fg = "white")
        label.grid(row = 1, column = 1)


class StatsPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg = "black")

        radio = tk.Button(self, text ="RADIO", bg="black", fg="green", width = 10,
                          command = lambda: controller.show_frame(RadioPage))
        radio.grid(row = 0, column=1)

        map = tk.Button(self, text ="MAP", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(MapPage))
        map.grid(row =0, column=2)

        data = tk.Button(self, text="DATA", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(DataPage))
        data.grid(row = 0, column=3)

        inv = tk.Button(self, text ="INV", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(InvPage))
        inv.grid(row = 0, column=4)

        stats = tk.Button(self, text ="STATS", bg="black", fg="green", width = 10)
        stats.grid(row = 0, column=5)

        f = Figure(figsize = (4,2), dpi = 100)
        a = f.add_subplot(111) #onexone chart number 1

        data = (1, 2, 3, 4, 5)
        ind = numpy.arange(5) #the x plots
        width = .5

        barh = a.bar(ind, data, width)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().grid(row = 1, column = 1)

app = SetUp()
app.mainloop()




