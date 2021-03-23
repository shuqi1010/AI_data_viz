import numpy
import pandas as pd
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="myAddress")



def dataprocessing(name):
    limit = 225
    location_s = None
    df = pd.DataFrame()
    locations = []
    latitude = []
    longitude = []
    counts = []
    visited = []
    p1s = []
    r1s = []
    p2s = []
    hasVisited = False
    PATH = r'AI exercise two\data_' + name + '.csv'
    data = pd.read_csv(PATH)
    data.head()
    for x in range(limit):
        z = 1.0
        geotag = data.iloc[x,0]
        count = data.iloc[x,5]
        if data.iloc[x,1] == "Yes":
            hasVisited = True
        else:
            hasVisited = False
        p1 = float(data.iloc[x,2])
        r1 = float(data.iloc[x,3])
        p2 = float(data.iloc[x,4])
        location = geolocator.geocode(geotag)
        if location != None:
            if location != location_s:
                locations.append(geotag)
                latitude.append(float(location.latitude))
                longitude.append(float(location.longitude))
                counts.append(float(count))
                visited.append(hasVisited)
                p1s.append(p1)
                r1s.append(r1)
                p2s.append(p2)
                p1_s = float(p1)
                r1_s = float(r1)
                p2_s = float(p2)
                count_s = count
            else:
                z = z+1
                count_sum = count_s + count
                del counts[-1]
                counts.append(float(count_sum))
                p1_avg = float(p1_s * ((z-1)/z) + p1 * (1/z))
                del p1s[-1]
                p1s.append(p1_avg)
                p2_avg = float(p2_s * ((z-1)/z) + p1 * (1/z))
                del p2s[-1]
                p2s.append(p2_avg)
                r1_avg = float(r1_s * ((z-1)/z) + r1 * (1/z))
                del r1s[-1]
                r1s.append(r1_avg)
                count_s = count_sum
                p1_s = p1_avg
                p2_s = p2_avg
                r1_s = r1_avg
        location_s = location
    df['Geotag'] = locations
    df['Latitude'] = latitude
    df['Longitude'] = longitude
    df['Counts'] = counts
    df['Visited'] = visited
    df['P1'] = p1s
    df['R1'] = r1s
    df['P2'] = p2s
    df.to_csv('processed_data_' + name + '.csv')

names = ["Beatrice"]
for name in names:
    dataprocessing(name)
