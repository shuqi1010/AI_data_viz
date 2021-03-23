import json
import numpy
import folium
import pandas as pd
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="myAddress")

#list of our names
names = ["Shuqi", "Beatrice", "Micol", "Jan", "Nicolas"]
testmap = folium.Map(height='100%',max_lon=180, min_zoom=3, zoom_start=40)
def findColor(name):
    return{
        'Shuqi':'#264653',
        'Beatrice':'#2a9d8f',
        'Micol':'#e9c46a',
        'Jan':'#f4a261',
        'Nicolas':'#e76f51',

    }[name]


# FIGURE A
for name in names:
    #read dataset
    PATH = r'processed_data_' + name + '.csv'
    data = pd.read_csv(PATH)
    data.head()
    limit = len(data) - 1
    geotags = folium.map.FeatureGroup(name)
    for x in range(limit):
        stroke = False
        latitude = float(data.iloc[x,2])
        longitude = float(data.iloc[x,3])
        count = int(data.iloc[x,4])
        visited = data.iloc[x,5]
        geotagName = data.iloc[x,1]
        if visited == 'TRUE':
            stroke = True
        else: stroke = False
        
        geotags.add_child(
            folium.CircleMarker(
                [latitude,longitude],
                radius = 10 + count*1,
                stroke = stroke,
                popup = geotagName.replace(" ","") + '\n(' + name +')',
                color = findColor(name),
                fill = True,
                fill_color = findColor(name),
                fill_opacity =  0.4
            )
        )
    geotags.layer_name = name
    testmap.add_child(geotags)


# FIGURE B


#folium.TileLayer('openstreetmap').add_to(testmap)
#folium.TileLayer('mapquestopen').add_to(testmap)
#folium.TileLayer('MapQuest Open Aerial').add_to(testmap)
#folium.TileLayer('Mapbox Bright').add_to(testmap)
#folium.TileLayer('stamentoner').add_to(testmap)
#folium.TileLayer('stamenwatercolor').add_to(testmap)

folium.LayerControl().add_to(testmap)
testmap.save("Figure A_Final.html")