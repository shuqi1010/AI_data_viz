import json
import numpy
import folium
import pandas as pd
from geopy.geocoders import Nominatim
import branca.colormap as cmp
geolocator = Nominatim(user_agent="myAddress")


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



for name in names:
    circles = folium.map.FeatureGroup()
    circles.layer_name = name
    PATH = 'processed_2year_data_' + name + '.csv'
    data = pd.read_csv(PATH)
    data.head()
    limit = len(data) - 1
    lat_s = 0
    lon_s = 0
    z = 0
    for x in range(limit):
        locationName = data.iloc[x,1]
        lat = data.iloc[x,2]
        lon = data.iloc[x,3]
        folium.CircleMarker(
            location = [lat, lon],
            radius = 12,
            popup = locationName,
            stroke = False,
            fill = True,
            fill_color=findColor(name),
            fill_opacity = 0.6
        ).add_to(circles)
        if z == 0: 
            lat_s = lat
            lon_s = lon
        folium.PolyLine(
            [[lat_s,lon_s],[lat, lon]], color = findColor(name),weight=2
            ).add_to(circles)
        lat_s = lat
        lon_s = lon
        z = z + 1
    
    testmap.add_child(circles)
    
    




folium.LayerControl().add_to(testmap)
testmap.save("2year.html")
