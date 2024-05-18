import numpy as np
import pandas as pd
import googlemaps
import csv
import time

gmaps = googlemaps.Client(key='AIzaSyA65CeniB1QhUdJEUJtJ9IJl4mojffBw5w')

geocode_result = gmaps.geocode('媽祖廟, 台中市豐原區')[0]
location = geocode_result['geometry']['location']
# Define the center point and radius for the search
radius = 10000  # meter

# Query tourist attractions within the specified radius
places_result = gmaps.places_nearby(location=location, keyword='tourist', radius=radius)
results = places_result['results']

# Fetch additional pages of results if available
while 'next_page_token' in places_result:
    time.sleep(2)
    places_result = gmaps.places_nearby(page_token=places_result['next_page_token'])
    results.extend(places_result['results'])

# Sort attractions by rating
results.sort(key=lambda x: x.get('rating', 0), reverse=True)

# Filter out attractions with a rating count less than 300
results_filtered = [place for place in results if place.get('user_ratings_total', 0) >= 100]

# Write attractions to CSV
with open('Pintung_Restaurant.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    fieldnames = ['name', 'latitude', 'longitude', 'rating', 'rating_count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writeheader()

    # Query details for each attraction and write to CSV
    for i, place in enumerate(results_filtered[:11], 1):
        place_name = place['name']

        # Use geocoding API to get the Place ID of the attraction
        geocode_result = gmaps.geocode(place_name)
        if not geocode_result:
            print(f"Could not find location: {place_name}")
            continue

        place_id = geocode_result[0]['place_id']

        # Fetch details for the attraction
        place_details = gmaps.place(place_id=place_id, fields=['name', 'rating', 'user_ratings_total', 'geometry'])

        if 'result' in place_details:
            result = place_details['result']
            place_name = result.get('name')
            rating = result.get('rating', 'N/A')
            rating_count = result.get('user_ratings_total', 'N/A')
            location = result['geometry']['location']

            # Write data to CSV
            writer.writerow({
                'name': place_name,
                'latitude': location['lat'],
                'longitude': location['lng'],
                'rating': rating,
                'rating_count': rating_count
            })

            print(f"{i}: {place_name} - Rating: {rating}, Rating Count: {rating_count}, Location: ({location['lat']}, {location['lng']})")
        else:
            print(f"Could not retrieve place details for {place_name}")

# Read attractions from CSV
df = pd.read_csv('Pintung_Restaurant.csv')
distances = []

# Calculate distances between attractions
for i in range(10):
    row = []
    for j in range(10):
        if i == j:
            row.append(0)
        else:
            origin = df.loc[i, 'name']
            destination = df.loc[j, 'name']
            result = gmaps.distance_matrix(origin, destination)

            if 'distance' in result['rows'][0]['elements'][0]:
                distance = result['rows'][0]['elements'][0]['distance']['text']
                row.append(distance)
            else:
                row.append(None)
    distances.append(row)

# Print distances matrix
for row in distances:
    print(row)