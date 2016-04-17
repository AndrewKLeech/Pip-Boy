import matplotlib
import numpy
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import *
import spotipy
import sys
import io
spotify = spotipy.Spotify()
import webbrowser
from urllib.request import urlopen

from PIL import Image, ImageTk

song1 = "spotify:artist:58lV9VcRSjABbAbfWS6skp"
song2 = 'spotify:artist:0PFtn5NtBbbUNbU9EAmIWF'
song3 = 'spotify:artist:5INjqkS1o8h1imAzPqGZBb'
song4 = 'spotify:artist:1HwM5zlC5qNWhJtM00yXzG'
song5 = 'spotify:artist:4tZwfgrHOc3mvqYlEYSvVi'
song6 = 'spotify:artist:3AA28KZvwAUcZuOKwyblJQ'
song7 = 'spotify:artist:5T0MSzX9RC5NA6gAI6irSn'
song8 = 'spotify:artist:0SwO7SWeDHJijQ3XNS7xEE'
song9 = 'spotify:artist:1dWEYMPtNmvSVaDNLgB6NV'


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

   def music(self, uri):

       spotify = spotipy.Spotify()
       results = spotify.artist_top_tracks(uri)

       #getting the track and audio link to top song
       for track in results['tracks'][:1]:
          text2 = track['preview_url']

          return text2

       if uri == song1:
            self.coverart("Bon Jovi")
       if uri == song2:
            self.coverart("Toto")
       if uri == song3:
            self.coverart("Tame Impala")
       if uri == song4:
           self.coverart("DMX")
       if uri == song5:
            self.coverart("Daft Punk")
       if uri == song6:
            self.coverart("Gorrillaz")
       if uri == song7:
            self.coverart("Estelle")
       if uri == song8:
            self.coverart("MGMT")
       if uri == song9:
            self.coverart("Saint Motel")

   def coverart(self, name):

        if len(sys.argv) > 1:
            artistName = ' '.join(sys.argv[1:])
        else:
            artistName = name

        results = spotify.search(q='artist:' + artistName, type='artist')
        items = results['artists']['items']
        if len(items) > 0:
            artist = items[0]
            url = artist['images'][0]['url']

        image_bytes = urlopen(url).read()
        data_stream = io.BytesIO(image_bytes)

        pil_image = Image.open(data_stream)

        tk_image = ImageTk.PhotoImage(pil_image)

        label = tk.Label(self, image = tk_image, height = 200, width = 200)
        label.image = tk_image #keeping refrence
        label.pack(padx = 5, pady = 5)




class StartPage(tk.Frame):

   def __init__(self, parent, controller):

       tk.Frame.__init__(self, parent)
       tk.Frame.configure(self, bg = "black")

       radio = tk.Button(self, text ="RADIO", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(RadioPage))
       radio.place(x = 15, y = 0)

       map = tk.Button(self, text ="MAP", bg="black", fg="green", width = 10,
                       command = lambda: controller.show_frame(MapPage))
       map.place(x = 95, y = 0)

       data = tk.Button(self, text="DATA", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(DataPage))
       data.place(x = 175, y = 0)

       inv = tk.Button(self, text ="INV", bg="black", fg="green", width = 10,
                       command = lambda: controller.show_frame(InvPage))
       inv.place(x = 255, y = 0)

       stats = tk.Button(self, text ="STATS", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(StatsPage))
       stats.place(x = 335, y = 0)

       image = Image.open("mrPip.gif")
       photo = ImageTk.PhotoImage(image)

       label = tk.Label(self, image = photo, bg = "black", fg = "white", height = 40, width = 40)
       label.image = photo #keeping refrence
       label.pack(side = BOTTOM, padx = 10, pady = 10)

       #to make width for now
       label = tk.Label(self, width = 60, bg = "black")
       label.pack(side = BOTTOM)


class RadioPage(tk.Frame):
   def __init__(self, parent, controller):

       tk.Frame.__init__(self, parent)
       tk.Frame.configure(self, bg = "black")

       radio = tk.Button(self, text ="RADIO", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(RadioPage))
       radio.place(x = 15, y = 0)

       map = tk.Button(self, text ="MAP", bg="black", fg="green", width = 10,
                       command = lambda: controller.show_frame(MapPage))
       map.place(x = 95, y = 0)

       data = tk.Button(self, text="DATA", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(DataPage))
       data.place(x = 175, y = 0)

       inv = tk.Button(self, text ="INV", bg="black", fg="green", width = 10,
                       command = lambda: controller.show_frame(InvPage))
       inv.place(x = 255, y = 0)

       stats = tk.Button(self, text ="STATS", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(StatsPage))
       stats.place(x = 335, y = 0)

       music1 = tk.Button(self, text = "Song 1", fg = "white", bg = "black", cursor = "hand2", width = 10, height = 3,
                          command = lambda: webbrowser.open_new(controller.music(song1)))
       music1.place(x = 70, y = 75)

       music2 = tk.Button(self, text = "Song 2", bg = "black", fg = "white", cursor = "hand2", width = 10, height = 3,
                          command = lambda: webbrowser.open_new(controller.music(song2)))
       music2.place(x = 70, y = 150)

       music3 = tk.Button(self, text = "Song 3", bg = "black", fg = "white", cursor = "hand2", width = 10, height = 3,
                          command = lambda: webbrowser.open_new(controller.music(song3)))
       music3.place(x = 70, y = 225)

       music4 = tk.Button(self, text = "Song 4", bg = "black", fg = "white", cursor = "hand2", width = 10, height = 3,
                          command = lambda: webbrowser.open_new(controller.music(song4)))
       music4.place(x = 175 , y = 75)

       music5 = tk.Button(self, text = "Song 5", bg = "black", fg = "white", cursor = "hand2", width = 10, height = 3,
                          command = lambda: webbrowser.open_new(controller.music(song5)))
       music5.place( x = 175 , y = 150)

       music6 = tk.Button(self, text = "Song 6", bg = "black", fg = "white", cursor = "hand2", width = 10, height = 3,
                          command = lambda: webbrowser.open_new(controller.music(song6)))
       music6.place(x = 175, y = 225)

       music7 = tk.Button(self, text = "Song 7", bg = "black", fg = "white", cursor = "hand2", width = 10, height = 3,
                          command = lambda: webbrowser.open_new(controller.music(song7)))
       music7.place(x = 280, y = 75)

       music8 = tk.Button(self, text = "Song 8", bg = "black", fg = "white", cursor = "hand2", width = 10, height = 3,
                          command = lambda: webbrowser.open_new(controller.music(song8)))
       music8.place(x = 280, y = 150)

       music9 = tk.Button(self, text = "Song 9", bg = "black", fg = "white", cursor = "hand2", width = 10, height = 3,
                          command = lambda: webbrowser.open_new(controller.music(song9)))
       music9.place(x = 280, y = 225)

       coverart = tk.Button(self, text = "Cover", bg = "black", fg = "white", cursor = "hand2", width = 10, height = 3,
                            command = lambda: controller.coverart("Estelle"))
       coverart.place(x = 290, y = 240)

class MapPage(tk.Frame):
   def __init__(self, parent, controller):

       tk.Frame.__init__(self, parent)
       tk.Frame.configure(self, bg = "black")

       radio = tk.Button(self, text ="RADIO", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(RadioPage))
       radio.place(x = 15, y = 0)

       map = tk.Button(self, text ="MAP", bg="black", fg="green", width = 10,
                       command = lambda: controller.show_frame(MapPage))
       map.place(x = 95, y = 0)

       data = tk.Button(self, text="DATA", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(DataPage))
       data.place(x = 175, y = 0)

       inv = tk.Button(self, text ="INV", bg="black", fg="green", width = 10,
                       command = lambda: controller.show_frame(InvPage))
       inv.place(x = 255, y = 0)

       stats = tk.Button(self, text ="STATS", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(StatsPage))
       stats.place(x = 335, y = 0)

       label = tk.Label(self, text = "map functionality", bg = "black", fg = "white")
       label.pack(side = BOTTOM)


class DataPage(tk.Frame):
   def __init__(self, parent, controller):

       tk.Frame.__init__(self, parent)
       tk.Frame.configure(self, bg = "black")

       radio = tk.Button(self, text ="RADIO", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(RadioPage))
       radio.place(x = 15, y = 0)

       map = tk.Button(self, text ="MAP", bg="black", fg="green", width = 10,
                       command = lambda: controller.show_frame(MapPage))
       map.place(x = 95, y = 0)

       data = tk.Button(self, text="DATA", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(DataPage))
       data.place(x = 175, y = 0)

       inv = tk.Button(self, text ="INV", bg="black", fg="green", width = 10,
                       command = lambda: controller.show_frame(InvPage))
       inv.place(x = 255, y = 0)

       stats = tk.Button(self, text ="STATS", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(StatsPage))
       stats.place(x = 335, y = 0)

       image = Image.open("WalkPip.gif")
       photo = ImageTk.PhotoImage(image)

       label = tk.Label(self, image = photo, bg = "black", fg = "white")
       label.image = photo #keeping refrence
       label.pack(side = BOTTOM, padx = 10, pady = 25)



class InvPage(tk.Frame):
   def __init__(self, parent, controller):

       tk.Frame.__init__(self, parent)
       tk.Frame.configure(self, bg = "black")

       radio = tk.Button(self, text ="RADIO", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(RadioPage))
       radio.place(x = 15, y = 0)

       map = tk.Button(self, text ="MAP", bg="black", fg="green", width = 10,
                       command = lambda: controller.show_frame(MapPage))
       map.place(x = 95, y = 0)

       data = tk.Button(self, text="DATA", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(DataPage))
       data.place(x = 175, y = 0)

       inv = tk.Button(self, text ="INV", bg="black", fg="green", width = 10,
                       command = lambda: controller.show_frame(InvPage))
       inv.place(x = 255, y = 0)

       stats = tk.Button(self, text ="STATS", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(StatsPage))
       stats.place(x = 335, y = 0)

       label = tk.Label(self, text = "inv functionality", bg = "black", fg = "white")
       label.pack(side = BOTTOM)


class StatsPage(tk.Frame):
   def __init__(self, parent, controller):

       tk.Frame.__init__(self, parent)
       tk.Frame.configure(self, bg = "black")

       radio = tk.Button(self, text ="RADIO", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(RadioPage))
       radio.place(x = 15, y = 0)

       map = tk.Button(self, text ="MAP", bg="black", fg="green", width = 10,
                       command = lambda: controller.show_frame(MapPage))
       map.place(x = 95, y = 0)

       data = tk.Button(self, text="DATA", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(DataPage))
       data.place(x = 175, y = 0)

       inv = tk.Button(self, text ="INV", bg="black", fg="green", width = 10,
                       command = lambda: controller.show_frame(InvPage))
       inv.place(x = 255, y = 0)

       stats = tk.Button(self, text ="STATS", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(StatsPage))
       stats.place(x = 335, y = 0)

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
       canvas.get_tk_widget().pack(side = BOTTOM)

app = SetUp()
app.mainloop()
