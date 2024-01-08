import datetime as dt # Core python package
import requests # requires install

import geocoder


g = geocoder.ip('me')
#print(g) # Ashburn Virginia us
#print(g.latlng) #[39.0437, -77.4875]

def index(request):
	API_KEY = open('apikey.txt','r').read().strip() # Tested
	WEATHER_BASE_URL = 'https://api.openweathermap.org/data/2.5/weather/?q=' # Tested


	CITY = "Tucson"
	GEO_LIMIT = 1
	STATE_CODE = "AZ"
	COUNTRY_CODE = 840 # usa

	GEO_BASE_URL = "http://api.openweathermap.org/geo/1.0/direct?"
	url = GEO_BASE_URL + CITY + "," + STATE_CODE + "," + str(COUNTRY_CODE) + "&limit=" + str(GEO_LIMIT) + "&appid=" + API_KEY
	response = requests.get(url).json()

	#print(response)
	#print('\n')

	LAT, LON = response[0]['lat'], response[0]['lon']

	url = WEATHER_BASE_URL + "lat=" + str(LAT) + "&lon=" + str(LON) + "&APPID=" + API_KEY

	response = requests.get(url).json()

	#print(response)


# https://www.youtube.com/watch?v=lyeK0aE_qRg
