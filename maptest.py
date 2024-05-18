import googlemaps
import time
from datetime import datetime
import csv

gmaps = googlemaps.Client(key='AIzaSyA65CeniB1QhUdJEUJtJ9IJl4mojffBw5w')

geocode_result = gmaps.geocode('草屯鎮公所, 南投縣')[0]
location = geocode_result['geometry']['location']
## 印出目前的位置
print("Location: ", location['lat'], location['lng'])
places_result = gmaps.places_nearby(location,keyword='tour' ,radius=100000)
results = places_result['results']
with open('草屯鎮公所_2_food.csv', 'w', newline='',encoding='utf-8') as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile)
    # Write the header row
    writer.writerow(['name', 'latitude', 'longitude', 'rating'])

    # Write the first page of results
    for place in places_result['results']:
        name = place['name']
        latitude = place['geometry']['location']['lat']
        longitude = place['geometry']['location']['lng']
        rating = place.get('rating', 'N/A')
        writer.writerow([name, latitude, longitude, rating])

    # Handle the next pages
    while 'next_page_token' in places_result:
        time.sleep(2.0)
        places_result = gmaps.places_nearby(page_token=places_result['next_page_token'])

        # Write each place to the CSV file
        for place in places_result['results']:
            name = place['name']
            latitude = place['geometry']['location']['lat']
            longitude = place['geometry']['location']['lng']
            rating = place.get('rating', 'N/A')
            writer.writerow([name, latitude, longitude, rating])
    # Print a message to indicate that the CSV file has been created
    print("CSV file created successfully.")
for i, place in enumerate(results, 1):
    print(i, ':', place['name'])
#print('hello2')