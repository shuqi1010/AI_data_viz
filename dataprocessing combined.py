import numpy
import pandas as pd



def dataprocessing(name):
    geotag_s = None
    df = pd.DataFrame()
    locations = []
    latitudes = []
    longitudes = []
    counts = []
    p1s = []
    r1s = []
    p2s = []
    PATH = r'processed_data_' + name + '.csv'
    data = pd.read_csv(PATH)
    data.head()
    limit = len(data) - 1
    for x in range(limit):
        z = 1.0
        geotag = data.iloc[x, 1]
        count = data.iloc[x, 4]
        p1 = float(data.iloc[x, 5])
        r1 = float(data.iloc[x, 6])
        p2 = float(data.iloc[x, 7])
        latitude = float(data.iloc[x, 2])
        longitude = float(data.iloc[x, 3])
        if geotag != geotag_s:
            locations.append(geotag)
            latitudes.append(latitude)
            longitudes.append(longitude)
            counts.append(float(count))
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
        geotag_s = geotag
    df['Geotag'] = locations
    df['Latitude'] = latitudes
    df['Longitude'] = longitudes
    df['Counts'] = counts
    df['P1'] = p1s
    df['R1'] = r1s
    df['P2'] = p2s
    df.to_csv('processed_data_' + name + '2.csv')


names = ["Combined"]
for name in names:
    dataprocessing(name)
