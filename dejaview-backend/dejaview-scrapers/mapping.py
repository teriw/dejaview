import googlemaps, requests, json
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyCPNuuW1GALn89xaVYxuLzuN3JELL0ClLk')

geocode_result = gmaps.geocode('20 Haines Street, Curtin, ACT, 2605')

# Geocoding an address
#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

print ('Geocode results')

print (geocode_result[0].keys())

print ("Lat:  " + str(geocode_result[0].get("geometry").get("location").get("lat")))
print ("Long: " + str(geocode_result[0].get("geometry").get("location").get("lng")))

targetLat = geocode_result[0].get("geometry").get("location").get("lat")
targetLong = geocode_result[0].get("geometry").get("location").get("lng")


# Look up an address with reverse geocoding
#reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))



# Request directions via public transit
#now = datetime.now()
#directions_result = gmaps.directions("Sydney Town Hall",
#                                     "Parramatta, NSW",
#                                     mode="transit",
#                                     departure_time=now)
#print ('Direction result')
#print directions_result
#Get Target Road Map
pic_url = ''.join(['https://maps.googleapis.com/maps/api/staticmap?center=', str(targetLat), ',', str(targetLong), '&zoom=18&size=640x640&maptype=roadmap'])
with open('googleLocalRoadMap.jpg', 'wb') as handle:
    response = requests.get(pic_url, stream=True)
    if not response.ok:
        print response

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)

    # Get Suburb Road Map
    pic_url = ''.join(['https://maps.googleapis.com/maps/api/staticmap?center=', str(targetLat), ',', str(targetLong),'&zoom=15&size=640x640&maptype=roadmap'])
    with open('googleSuburbRoadMap.jpg', 'wb') as handle:
        response = requests.get(pic_url, stream=True)
        if not response.ok:
            print response

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)

# Get Target Overhead Imagery
pic_url = ''.join(['https://maps.googleapis.com/maps/api/staticmap?center=', str(targetLat), ',', str(targetLong),'&zoom=20&size=640x640&maptype=satellite'])
with open('googleTargetSatellite.jpg', 'wb') as handle:
    response = requests.get(pic_url, stream=True)
    if not response.ok:
        print response

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)

# Get Area Imagery
pic_url = ''.join(['https://maps.googleapis.com/maps/api/staticmap?center=', str(targetLat), ',', str(targetLong),'&zoom=18&size=640x640&maptype=hybrid'])
with open('googleAreaImagery.jpg', 'wb') as handle:
    response = requests.get(pic_url, stream=True)
    if not response.ok:
        print response

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)
