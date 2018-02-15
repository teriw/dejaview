import googlemaps, requests

gmaps = googlemaps.Client(key='AIzaSyCPNuuW1GALn89xaVYxuLzuN3JELL0ClLk')
geocode_result = gmaps.geocode('20 Haines Street, Curtin, ACT, 2605')

targetLat = geocode_result[0].get("geometry").get("location").get("lat")
targetLong = geocode_result[0].get("geometry").get("location").get("lng")
targetAddress = str(geocode_result[0].get("formatted_address"))

print ('Collecting Google Maps imagery...')

#Get Local Road Map
pic_url = ''.join(['https://maps.googleapis.com/maps/api/staticmap?center=', str(targetLat), ',', str(targetLong), '&zoom=18&size=640x640&maptype=roadmap'])
with open('googleLocalRoadMap.jpg', 'wb') as handle:
    response = requests.get(pic_url, stream=True)
    if not response.ok:
        print response

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)
    print('  Target Street Map Downloaded')

# Get Suburb Road Map
pic_url = ''.join(['https://maps.googleapis.com/maps/api/staticmap?center=', str(targetLat), ',', str(targetLong),'&zoom=15&size=640x640&markers=color:red%7C', str(targetLat), ',', str(targetLong),'&maptype=roadmap'])
with open('googleSuburbRoadMap.jpg', 'wb') as handle:
    response = requests.get(pic_url, stream=True)
    if not response.ok:
        print response

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)
    print('  Suburb Street Map Downloaded')

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
    print('  Target Overhead Imagery Downloaded')

# Get Area Imagery
pic_url = ''.join(['https://maps.googleapis.com/maps/api/staticmap?center=', str(targetLat), ',', str(targetLong),'&zoom=18&size=640x640&markers=color:red%7C', str(targetLat), ',', str(targetLong),'&maptype=hybrid'])
with open('googleAreaImagery.jpg', 'wb') as handle:
    response = requests.get(pic_url, stream=True)
    if not response.ok:
        print response

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)
    print('  Area Imagery Downloaded')

# Get Street View
pic_url = ''.join(['https://maps.googleapis.com/maps/api/streetview?size=680x400&location=', str(targetAddress),'&fov=110&heading=235&pitch=0&key=AIzaSyCPNuuW1GALn89xaVYxuLzuN3JELL0ClLk'])
pic_url = pic_url.replace(' ', '%20')

with open('googleStreetView.jpg', 'wb') as handle:
    response = requests.get(pic_url, stream=True)
    if not response.ok:
        print response

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)
    print('  Street View Downloaded')