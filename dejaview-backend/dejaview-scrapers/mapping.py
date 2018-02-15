import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyCPNuuW1GALn89xaVYxuLzuN3JELL0ClLk')

geocode_result = gmaps.geocode('20 Haines Street, Curtin, ACT, 2605')

# Geocoding an address
#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

print ('Geocode results')
print geocode_result

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)
print ('Direction result')
print directions_result
