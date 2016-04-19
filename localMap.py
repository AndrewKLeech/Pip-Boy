from io import BytesIO
import urllib.request
from PIL import Image
import socket
import simplejson

googleGeocodeUrl = 'http://maps.googleapis.com/maps/api/geocode/json?'


def get_map(lat,lng):
    latString = str(lat)
    lngString = str(lng)
    print(lat)
    url = ("https://maps.googleapis.com/maps/api/staticmap?center="+latString+","+lngString+"&size=500x500&zoom=16&sensor=false")
    buffer = BytesIO(urllib.request.urlopen(url).read())
    image = Image.open(buffer)
    image.show()


def get_coordinates(query, from_sensor=False):
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


get_coordinates("new york")