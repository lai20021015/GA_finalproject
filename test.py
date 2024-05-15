def create_request_payload(origin, destination):
    return {
        "origin": {
            "location": {
                "latLng": {
                    "latitude": origin["latitude"],
                    "longitude": origin["longitude"]
                }
            }
        },
        "destination": {
            "location": {
                "latLng": {
                    "latitude": destination["latitude"],
                    "longitude": destination["longitude"]
                }
            }
        },
        "travelMode": "TWO_WHEELER"
    }


origin = {
    "latitude": 37.419734,
    "longitude": -122.0827784
}

destination = {
    "latitude": 37.417670,
    "longitude": -122.079595
}

payload = create_request_payload(origin, destination)
print(payload)