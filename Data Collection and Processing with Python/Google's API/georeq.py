import requests
import json

api_key = False
# if you have a google places API key, place it here
# api_key = 'AIzaSy__IDByT70'

if api_key is False:
	api_key = 42
	serviceurl = 'http://py4e-data.dr-chuck.net/json'
else:
	serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json'

while True:
	address = input('Enter location: ')
	if len(address) < 1: break

	payload = dict()
	payload['address'] = address
	if api_key is not False: payload['key'] = api_key

	r = requests.get(serviceurl, params=payload)
	data = r.text
	print('Retrieved', len(data), 'characters')

	try:
		js = json.loads(data)
	except:
		js = None

	if not js or 'status' not in js or js['status'] != 'OK':
		print('==== Failure To Retrieve ====')
		print(data)
		continue

	print(json.dumps(js, indent=4))

	lat = js['results'][0]['geometry']['location']['lat']
	lng = js['results'][0]['geometry']['location']['lng']
	print('lat', lat, 'lng', lng)
	location = js['results'][0]['formatted_address']
	print(location) 