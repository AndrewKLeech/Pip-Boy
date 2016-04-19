from io import BytesIO
import urllib.request
import PIL.Image
import socket
import simplejson
from tkinter import *

googleGeocodeUrl = 'http://maps.googleapis.com/maps/api/geocode/json?'


def get_map(lat,lng):
    latString = str(lat)
    lngString = str(lng)
    print(lat)
    url = ("https://maps.googleapis.com/maps/api/staticmap?center="+latString+","+lngString+"&size=500x500&zoom=16&sensor=false")
    buffer = BytesIO(urllib.request.urlopen(url).read())
    image = PIL.Image.open(buffer)
    image.show()


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


master.title("Tkinter Entry Widget")
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