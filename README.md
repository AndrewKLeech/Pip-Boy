# Pip-Boy

### Team members:
1. Katie Fitzgerald (C14391781): UI Design, Stats, and music.
2. Andrew Leech (C14403082): Map and Twitter feed.
3. Cillian McCabe (C14454828): Game.

### How to run:
Main program is in game.py. Libraries needed are: 
tkinter
spotipy
webbrowser
PIL
os
twitter
io
urllib.request
urllib.parse
simplejson

### Outline:
The aim of the project is to recreate the OS of a Pip-Boy (Personal Information Processor) from the Fallout series using the Python language.

(Information on the Pip-Boy: http://fallout.wikia.com/wiki/Pip-Boy_3000_Mark_IV as well as Pip-OS: http://fallout.wikia.com/wiki/Pip-OS_v7.1.0.8)

#### UI Design:
UI Design: Design follows the PipBoy/menu style http://o.aolcdn.com/hss/storage/midas/24a0592f92f2765f98cee4c68addc493/202922823/pip-boy-app.gif 
consists of buttons which load different class/pages.

#### Stat:
Stats displays the images from PipBoy, when buttons are pressed. There demonstrating how to do this:  
https://www.youtube.com/watch?v=ys-M_Hgi0mUhttps://www.youtube.com/watch?v=ys-M_Hgi0mU

#### Radio:
Radio uses spotify API (spotipy library). This generates links to a 30 second preview of 9 songs from a button press. 

#### Map:
Map uses the google static map api and google geocode api. It gets an image of a map of the location the user enters.
The geocode info comes through json so a json library was needed to use this.

#### Twitter:
Using a twitter library and the twitter api, the pip-boy program can read a twitter users feed and also send tweets from in the app.
Tutorial video here: https://www.youtube.com/watch?v=Ur2AQKoGbbA&feature=youtu.be

#### Game:
Game to be in the style of the PipBoy, as done within the game: http://fallout.wikia.com/wiki/Pip-Boy_3000_Mark_IV_minigames
The game requires you to install the PyGame library. Tutorial video here: https://www.youtube.com/watch?v=ZRgjAjUfgGI 
