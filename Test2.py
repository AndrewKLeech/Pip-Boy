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

       image = Image.open("Pip Boy Images\mrPip.gif")
       photo = ImageTk.PhotoImage(image)

       label = tk.Label(self, image = photo, bg = "black", fg = "white", height = 40, width = 40)
       label.image = photo #keeping refrence
       label.pack(side = BOTTOM, padx = 10, pady = 10)

       #to make width for now
       label = tk.Label(self, width = 60, bg = "black")
       label.pack(side = BOTTOM, pady = 120)


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

        #opening images for buttons

       bonjovi1 = Image.open("coverart\Bonjovi.gif")
       bonjovi = ImageTk.PhotoImage(bonjovi1)

       toto1 = Image.open("coverart\Toto.gif")
       toto = ImageTk.PhotoImage(toto1)

       tameimpala1 = Image.open("coverart\Tameimpala.gif")
       tameimpala = ImageTk.PhotoImage(tameimpala1)

       dmx1 = Image.open("coverart\Dmx.gif")
       dmx = ImageTk.PhotoImage(dmx1)

       daftpunk1 = Image.open("coverart\Daftpunk.gif")
       daftpunk = ImageTk.PhotoImage(daftpunk1)

       gorrillaz1 = Image.open("coverart\Gorrillaz.gif")
       gorrillaz = ImageTk.PhotoImage(gorrillaz1)

       estelle1 = Image.open("coverart\estelle.gif")
       estelle = ImageTk.PhotoImage(estelle1)

       mgmt1 = Image.open("coverart\Mgmt.gif")
       mgmt = ImageTk.PhotoImage(mgmt1)

       saintmotel1 = Image.open("coverart\Saintmotel.gif")
       saintmotel = ImageTk.PhotoImage(saintmotel1)

       music1 = tk.Button(self, image = bonjovi, fg = "white", bg = "black", cursor = "hand2", width = 75, height = 75,
                          command = lambda: webbrowser.open_new(controller.music(song1)))
       music1.image = bonjovi #keeping refrence
       music1.place(x = 70, y = 75)

       music2 = tk.Button(self, image = toto, bg = "black", fg = "white", cursor = "hand2", width = 75, height = 75,
                          command = lambda: webbrowser.open_new(controller.music(song2)))
       music2.image = toto
       music2.place(x = 70, y = 150)

       music3 = tk.Button(self, image = tameimpala, bg = "black", fg = "white", cursor = "hand2", width = 75, height = 75,
                          command = lambda: webbrowser.open_new(controller.music(song3)))
       music3.image = tameimpala
       music3.place(x = 70, y = 225)

       music4 = tk.Button(self, image = dmx, bg = "black", fg = "white", cursor = "hand2", width = 75, height = 75,
                          command = lambda: webbrowser.open_new(controller.music(song4)))
       music4.image = dmx
       music4.place(x = 175 , y = 75)

       music5 = tk.Button(self, image = daftpunk, bg = "black", fg = "white", cursor = "hand2", width = 75, height = 75,
                          command = lambda: webbrowser.open_new(controller.music(song5)))
       music5.image = daftpunk
       music5.place( x = 175 , y = 150)

       music6 = tk.Button(self, image = gorrillaz, bg = "black", fg = "white", cursor = "hand2", width = 75, height = 75,
                          command = lambda: webbrowser.open_new(controller.music(song6)))
       music6.image = gorrillaz
       music6.place(x = 175, y = 225)

       music7 = tk.Button(self, image = estelle, bg = "black", fg = "white", cursor = "hand2", width = 75, height = 75,
                          command = lambda: webbrowser.open_new(controller.music(song7)))
       music7.image = estelle
       music7.place(x = 280, y = 75)

       music8 = tk.Button(self, image = mgmt, bg = "black", fg = "white", cursor = "hand2", width = 75, height = 75,
                          command = lambda: webbrowser.open_new(controller.music(song8)))
       music8.image = mgmt
       music8.place(x = 280, y = 150)

       music9 = tk.Button(self, image = saintmotel, bg = "black", fg = "white", cursor = "hand2", width = 75, height = 75,
                          command = lambda: webbrowser.open_new(controller.music(song9)))
       music9.image = saintmotel
       music9.place(x = 280, y = 225)


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

       #new buttons

       strength = tk.Button(self, text ="STRENGTH", bg="black", fg="green", width = 20,
                            command = lambda: self.ImageShow("Pip Boy Images\Strength.gif"))
       strength.place(x = 35, y = 50)

       perception = tk.Button(self, text ="PERCEPTION", bg="black", fg="green", width = 20,
                              command = lambda: self.ImageShow("Pip Boy Images\Perception.gif"))
       perception.place(x = 35, y = 75)

       endurance = tk.Button(self, text ="ENDURANCE", bg="black", fg="green", width = 20,
                              command = lambda: self.ImageShow("Pip Boy Images\Endurance.gif"))
       endurance.place(x = 35, y = 100)

       charisma = tk.Button(self, text ="CHARISMA", bg="black", fg="green", width = 20,
                              command = lambda: self.ImageShow("Pip Boy Images\Charisma.gif"))
       charisma.place(x = 35, y = 125)

       intelligence = tk.Button(self, text ="INTELLIGENCE", bg="black", fg="green", width = 20,
                              command = lambda: self.ImageShow("Pip Boy Images\Intelligence.gif"))
       intelligence.place(x = 35, y = 150)

       agility = tk.Button(self, text ="AGILITY", bg="black", fg="green", width = 20,
                              command = lambda: self.ImageShow("Pip Boy Images\Agility.gif"))
       agility.place(x = 35, y = 175)

       luck = tk.Button(self, text ="LUCK", bg="black", fg="green", width = 20,
                        command = lambda: self.ImageShow("Pip Boy Images\Luck.gif"))
       luck.place(x = 35, y = 200)


   def ImageShow(self, path):

       label = tk.Label(self, bg = "black",  width = 40, height = 40)
       label.place(x = 215, y = 75)

       image = Image.open(path)
       photo = ImageTk.PhotoImage(image)

       label = tk.Label(self, image = photo, bg = "black", fg = "white")
       label.image = photo #keeping refrence
       label.place(x = 200, y = 75)



app = SetUp()
app.mainloop()