import io
import urllib.request
from PIL import Image


def get_location(query):


    params = { }
    params[ 'sensor' ] = "false"
    params[ 'address' ] = query

    params = urllib.parse.urlencode( params )
    print("https://maps.googleapis.com/maps/api/geocode/json?%s" % params)

    f = urllib.request.urlopen("https://maps.googleapis.com/maps/api/geocode/json?%s" % params)


def get_map():

    url = "https://maps.googleapis.com/maps/api/staticmap?center=53.3766353,-6.3887243&size=500x500&zoom=15&sensor=false"
    buffer = io.BytesIO(urllib.request.urlopen(url).read())
    image = Image.open(buffer)
    image.show()

get_location("14 cherry ave, dublin 15")
get_map()