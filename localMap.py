from io import BytesIO
import urllib.request
import PIL.Image
from PIL import ImageTk
import socket
import simplejson
from tkinter import *

#url used for google geocodeing api
googleGeocodeUrl = 'http://maps.googleapis.com/maps/api/geocode/json?'


def get_map(lat,lng):
    latString = str(lat)
    lngString = str(lng)
    #Map url from google maps, has marker and colors included
    url = ("https://maps.googleapis.com/maps/api/staticmap?center="+latString+","+lngString+"&size=500x500&zoom=16&style=feature:road.local%7Celement:geometry%7Ccolor:0x00ff00%7Cweight:1%7Cvisibility:on&style=feature:landscape%7Celement:geometry.fill%7Ccolor:0x000000%7Cvisibility:on&style=feature:landscape%7Celement:geometry.fill%7Ccolor:0x000000%7Cvisibility:on&style=feature:administrative%7Celement:labels%7Cweight:3.9%7Cvisibility:on%7Cinverse_lightness:true&style=feature:poi%7Cvisibility:simplified&markers=color:blue%7Clabel:H%7C"+latString+","+lngString+"&markers=size:tiny%7Ccolor:green%7CDelta+Junction,AK\
&sensor=false")
    buffer = BytesIO(urllib.request.urlopen(url).read())
    pil_image = PIL.Image.open(buffer)
    tk_image = ImageTk.PhotoImage(pil_image)
    # put the image in program
    label = Label(master, image=tk_image)
    label.pack(padx=5, pady=5)
    master.mainloop()


def get_coordinates(from_sensor=False):
    global entryWidget

    if entryWidget.get().strip() == "":
        print("Empty")
    else:
        query=entryWidget.get().strip()
        print("working")
        query = query.encode('utf-8')
        params = {
            'address': query,
            'sensor': "true" if from_sensor else "false"
        }
        url = googleGeocodeUrl + urllib.parse.urlencode(params)
        json_response = urllib.request.urlopen(url)
        response = simplejson.loads(json_response.read())
        if response['results']:
            location = response['results'][0]['geometry']['location']
            latitude, longitude = location['lat'], location['lng']
            print(query, latitude, longitude)
        else:
            latitude, longitude = None, None
            print(query, "<no results>")
        get_map(latitude, longitude)


master = Tk()


master.title("Map")
master.geometry('500x500')

master["padx"] = 40
master["pady"] = 20
# Create a text frame to hold the text Label and the Entry widget
textFrame = Frame(master)
#Create a Label in textFrame
entryLabel = Label(textFrame)
entryLabel["text"] = "Where are you?"
entryLabel.pack(side=LEFT)
# Create an Entry Widget in textFrame
entryWidget = Entry(textFrame)
entryWidget["width"] = 50
entryWidget.pack(side=LEFT)
textFrame.pack()
button = Button(master, text="Submit", command=get_coordinates)
button.pack()
master.mainloop()





