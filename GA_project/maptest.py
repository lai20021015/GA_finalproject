import googlemaps
import time
from datetime import datetime

## googlemaps.Client(key='AIzaSyA65CeniB1QhUdJEUJtJ9IJl4mojffBw5w')
gmaps = googlemaps.Client(key='AIzaSyA65CeniB1QhUdJEUJtJ9IJl4mojffBw5w')

geocode_result = gmaps.geocode('National Yang Ming Chiao Tung University Hshinchu Taiwan')[0]
location = geocode_result['geometry']['location']
#location = {'lat': 24.18162, 'lng': 120.719682}
places_result = gmaps.places_nearby(location,keyword='restaurant',radius=2000)

#places_result = gmaps.places_nearby(location, keyword='park',radius=25)


## 印出目前的位置
print("Location: ", location['lat'], location['lng'])
#print('hello')
# cnt = 0
# for place in places_result['results']:
#     print(cnt+1,': ' ,place['name']) #, place.get['formatted_address', 'No address provided']
#     cnt+=1
places_result = gmaps.places_nearby(location,keyword='swimming' ,radius=2000)
results = places_result['results']
print("總共找到這麼多間: ", len(results))
while 'next_page_token' in places_result:
    time.sleep(2)
    places_result = gmaps.places_nearby(page_token=places_result['next_page_token'])
    results.extend(places_result['results'])

for i, place in enumerate(results, 1):
    print(i, ':', place['name'])
#print('hello2')