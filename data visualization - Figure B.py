import json
import numpy
import folium
import pandas as pd
from geopy.geocoders import Nominatim
import branca.colormap as cmp
geolocator = Nominatim(user_agent="myAddress")

#list of our names
#names = ["Combined", "Beatrice", "Micol", "Jan", "Nicolas"]
testmap = folium.Map(height='100%',max_lon=180, min_zoom=3, zoom_start=40)

list = ['P1', 'R1', 'P2']

 #read dataset
PATH = r'processed_data_Combined2.csv'
data = pd.read_csv(PATH)
data.head()
limit = len(data) - 1

def colorScale(v):
    if v < 3: color = '#cff4d2'
    if (v > 2 and v < 5): color = '#7be495'
    if (v > 4 and v < 7): color = '#56c596'
    if (v > 6 and v < 9): color = '#329d9c'
    if v > 8: color = '#205072'
    return color


# FIGURE B
circles = folium.map.FeatureGroup()
for x in range(limit):
    geotagName = data.iloc[x,1]
    latitude = float(data.iloc[x,2])
    longitude = float(data.iloc[x,3])
    P1 = float(data.iloc[x,5])
    folium.CircleMarker(
        location = [latitude, longitude],
        radius = 18,
        popup = geotagName.replace(" ","") + '\n P1: ' + str('{0:.1f}'.format(P1)),
        stroke = False,
        fill = True,
        fill_color=colorScale(P1),
        fill_opacity =  0.5
    ).add_to(circles)
circles.layer_name = 'P1'
testmap.add_child(circles)


circles = folium.map.FeatureGroup()
for x in range(limit):
    geotagName = data.iloc[x,1]
    latitude = float(data.iloc[x,2])
    longitude = float(data.iloc[x,3])
    P2 = float(data.iloc[x,7])
    folium.CircleMarker(
        location = [latitude, longitude],
        radius = 18,
        popup = geotagName.replace(" ","") + '\n P2: ' + str('{0:.1f}'.format(P2)),
        stroke = False,
        fill = True,
        fill_color=colorScale(P2),
        fill_opacity =  0.5
    ).add_to(circles)
circles.layer_name = 'P2'
testmap.add_child(circles)


circles = folium.map.FeatureGroup()
for x in range(limit):
    geotagName = data.iloc[x,1]
    latitude = float(data.iloc[x,2])
    longitude = float(data.iloc[x,3])
    R1 = float(data.iloc[x,6])
    folium.CircleMarker(
        location = [latitude, longitude],
        radius = 18,
        popup = geotagName.replace(" ","") + '\n R1: ' + str('{0:.1f}'.format(R1)),
        stroke = False,
        fill = True,
        fill_color=colorScale(R1),
        fill_opacity =  0.5
    ).add_to(circles)
circles.layer_name = 'R1'
testmap.add_child(circles)

top = folium.map.FeatureGroup()
toplist = [73, 144,195,207,307,324,57,58,265,306,37,143,235,95,131,237,211,286,303,291,9,266,275,1,124,142,51,56,89,136,146,50,80,116,220,326]
for y in toplist:
    folium.Marker(
    location=[float(data.iloc[y,2]), float(data.iloc[y,3])],
    popup= data.iloc[y,1]
    ).add_to(top)
top.layer_name = 'The most Instagrammable'
testmap.add_child(top)





#folium.TileLayer('openstreetmap').add_to(testmap)
#folium.TileLayer('mapquestopen').add_to(testmap)
#folium.TileLayer('MapQuest Open Aerial').add_to(testmap)
#folium.TileLayer('Mapbox Bright').add_to(testmap)
#folium.TileLayer('stamentoner').add_to(testmap)
#folium.TileLayer('stamenwatercolor').add_to(testmap)

folium.LayerControl().add_to(testmap)
testmap.save("Figure B_test.html")