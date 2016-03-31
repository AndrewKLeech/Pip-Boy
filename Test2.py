import matplotlib
import numpy
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import tkinter as tk
import tkinter as ttk
import spotipy
import sys
import webbrowser

PIP_FONT = ("Verdana", 12)
photo = "mrPip.gif"

uri_ID = 'spotify:artist:1Xylc3o4UrD53lo9CvFvVg'

spotify = spotipy.Spotify()
results = spotify.artist_top_tracks(uri_ID)

#getting the track and audio link to top zara larrson song
for track in results['tracks'][:1]:
   text = 'Track    : ' + track['name']
   text2 = track['preview_url']


def callback(event):
    webbrowser.open_new(text2)


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

        var = tk.StringVar()
        var.set(text)

        var2 = tk.StringVar()
        var2.set(text2)

        label = tk.Label(self, textvariable = var, bg = "black", fg = "white")
        label.grid(row = 1, column = 1, sticky = "w")

        label2 = tk.Label(self, textvariable = var2, bg = "black", fg = "white", cursor = "hand2")
        label2.bind("<Button-1>", callback)
        label2.grid(row = 2, column = 1, sticky = "w", columnspan = 6)



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

        f = Figure(figsize = (7,5), dpi = 50)
        a = f.add_subplot(111) #onexone chart number 1

        data = (1, 2, 3, 4, 5)
        ind = numpy.arange(5) #the x plots
        width = 0.4

        a.barh(ind + width, data, width, color = 'g')

        a.set_axis_bgcolor('black')
        a.set_title('Stats')
        a.set_xticks(ind + width)
        a.set_xticklabels(('Strength', 'Perception', 'Endurance', 'Charisma', 'Agility'))

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().grid(row = 2, column = 0, sticky = "w", columnspan = 6)

app = SetUp()
app.mainloop()