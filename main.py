import json
import turtle
import urllib.request
import time
import webbrowser   
import geocoder

#free API
url = "http://api.open-notify.org/astro.json"

response = urllib.request.urlopen(url)
result = json.loads(response.read())

#print astrounats
file = open("iss.txt","w")
file.write("Atualmente, possui" + str(result["number"]) + "astrounatas na estação espacial internacional: \n\n")

people = result["people"]

for p in people:
    file.write(p['name'] + " - a bordo" + "\n")
    
# print long and lat
g = geocoder.ip('me')
file.write("\nA atual lang / long é: " + str(g.latlng))
file.close()
webbrowser.open("iss.txt")

# Setup the world map in turtle module
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

# load the world map image
screen.bgpic("map.gif")
screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45)
iss.penup()

while True:
    # load the current status of the ISS in real-time
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    # Extract the ISS location
    location = result["iss_position"]
    lat = location['latitude']
    lon = location['longitude']

    # Ouput lon and lat to the terminal
    lat = float(lat)
    lon = float(lon)
    print("\nLatitude: " + str(lat))
    print("\nLongitude: " + str(lon))

    # Update the ISS location on the map
    iss.goto(lon, lat)

    time.sleep(5)
