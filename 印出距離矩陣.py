import numpy as np
import pandas as pd
import googlemaps
import time
from datetime import datetime
# AIzaSyAI5Yz-aJ5D2OCv-ZxSjzz-apIBpG__GO0
gmaps = googlemaps.Client(key='AIzaSyA65CeniB1QhUdJEUJtJ9IJl4mojffBw5w')

df = pd.read_csv('豐原媽祖廟_tour.csv')
distances = []

for i in range(10):
    row = []
    for j in range(10):
        if i == j:
            row.append(0)
        else:
            time.sleep(0.05)
            origin = df.loc[i, 'name']
            destination = df.loc[j, 'name']
            result = gmaps.distance_matrix(origin, destination)
            if 'distance' in result['rows'][0]['elements'][0]:
                distance = result['rows'][0]['elements'][0]['distance']['text']
                row.append(distance)
            else:
                row.append(None)
    distances.append(row)
for i in range(10):
    for j in range(i+1, 10):  # Start from i+1 to avoid overwriting already calculated distances
        if distances[i][j] is not None:
            distances[j][i] = distances[i][j]
        elif distances[j][i] is not None:
            distances[i][j] = distances[j][i]

for i in range (10):
    print(distances[i], end='\n')
for i in range (10):
    places = []
    for i in range(10):
        places.append(df.loc[i, 'name'])
print(places)
