import googlemaps, requests, bingmaps

gmaps = googlemaps.Client(key='AIzaSyCPNuuW1GALn89xaVYxuLzuN3JELL0ClLk')
geocode_result = gmaps.geocode('20 Haines Street, Curtin, ACT, 2605')

targetLatLong = str(str(geocode_result[0].get("geometry").get("location").get("lat")) + ',' + str(geocode_result[0].get("geometry").get("location").get("lng")))
targetAddress = str(geocode_result[0].get("formatted_address"))

print('Collecting Google Maps imagery...')

#Get Google Local Road Map
pic_url = str('https://maps.googleapis.com/maps/api/staticmap?center=' + targetLatLong + '&zoom=18&size=640x640&maptype=roadmap')
with open('googleLocalRoadMap.jpg', 'wb') as handle:
    response = requests.get(pic_url, stream=True)
    if not response.ok:
        print (response)

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)
    print('  Target Street Map Downloaded')

# Get Google Suburb Road Map
pic_url = str('https://maps.googleapis.com/maps/api/staticmap?center=' + targetLatLong + '&zoom=15&size=640x640&markers=color:red%7C' + targetLatLong + '&maptype=roadmap')
with open('googleSuburbRoadMap.jpg', 'wb') as handle:
    response = requests.get(pic_url, stream=True)
    if not response.ok:
        print (response)

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)
    print('  Suburb Street Map Downloaded')

# Get Google Target Overhead Imagery
pic_url = str('https://maps.googleapis.com/maps/api/staticmap?center=' + targetLatLong + '&zoom=20&size=640x640&maptype=satellite')
with open('googleTargetSatellite.jpg', 'wb') as handle:
    response = requests.get(pic_url, stream=True)
    if not response.ok:
        print (response)

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)
    print('  Target Overhead Imagery Downloaded')

# Get Google Area Imagery
pic_url = str('https://maps.googleapis.com/maps/api/staticmap?center=' + targetLatLong + '&zoom=18&size=640x640&markers=color:red%7C' + targetLatLong + '&maptype=hybrid')
with open('googleAreaImagery.jpg', 'wb') as handle:
    response = requests.get(pic_url, stream=True)
    if not response.ok:
        print (response)

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)
    print('  Area Imagery Downloaded')

# Get Google Street View
pic_url = str('https://maps.googleapis.com/maps/api/streetview?size=680x400&location=' + targetAddress + '&fov=110&pitch=0&key=AIzaSyCPNuuW1GALn89xaVYxuLzuN3JELL0ClLk')
pic_url = pic_url.replace(' ', '%20')
with open('googleStreetView.jpg', 'wb') as handle:
    response = requests.get(pic_url, stream=True)
    if not response.ok:
        print (response)

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)
    print('  Street View Downloaded')


print('Collecting Bing Maps Imagery...')

#Get Bing Local Road Map
pic_url = str('https://dev.virtualearth.net/REST/V1/Imagery/Map/CanvasLight/' + targetLatLong + '/17?mapSize=680,680&pushpin=' + targetLatLong + ';0&key=AluRHNFmdS409Z_IbVrx1_qZEQNEgGJMqce4A1UP1DC0Q0lpQz04g3BcZmCGYkbC')
with open('bingLocalRoadMap.jpg', 'wb') as handle:
    response = requests.get(pic_url, stream=True)
    if not response.ok:
        print (response)

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)
    print('  Target Street Map Downloaded')


#Get Bing Target Overhead Imagery
pic_url = str('https://dev.virtualearth.net/REST/V1/Imagery/Map/AerialWithLabels/' + targetLatLong + '/20?mapSize=680,680&key=AluRHNFmdS409Z_IbVrx1_qZEQNEgGJMqce4A1UP1DC0Q0lpQz04g3BcZmCGYkbC')
with open('bingTargetSatellite.jpg', 'wb') as handle:
    response = requests.get(pic_url, stream=True)
    if not response.ok:
        print (response)

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)
    print('  Target Overhead Imagery Downloaded')

#Get Bing Area Imagery
pic_url = str('https://dev.virtualearth.net/REST/V1/Imagery/Map/AerialWithLabels/' + targetLatLong + '/18?mapSize=680,680&pushpin=' + targetLatLong + ';89&key=AluRHNFmdS409Z_IbVrx1_qZEQNEgGJMqce4A1UP1DC0Q0lpQz04g3BcZmCGYkbC')
with open('bingAreaImagery.jpg', 'wb') as handle:
    response = requests.get(pic_url, stream=True)
    if not response.ok:
        print (response)

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)
    print('  Area Imagery Downloaded')

