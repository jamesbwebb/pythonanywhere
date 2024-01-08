import datetime as dt
import requests

import geocoder

#g = geocoder.ip('me')
#print(g) # Ashburn Virginia us
#print(g.latlng) #[39.0437, -77.4875]

#print('\n')

# Signing to get your key or generate a new one
#https://home.openweathermap.org/users/sign_in

# Read the docs, current weather data.
#https://openweathermap.org/current

# Not sure if my setup will work as the website is asking for lat/long data to be included in the api call.
# while the code below might work the back end supporting the locations is no longer
# being kept up. Proposed solution is to use the suggested geocoder api to get lat/long data for a location and put that in.

# "Please use Geocoder API if you need automatic convert city names and zip-codes to geo coordinates and the other way around."

WEATHER_BASE_URL = 'https://api.openweathermap.org/data/2.5/weather/?' # Tested
API_KEY = open('apikey.txt','r').read().strip() # Tested
CITY = "Tucson"
GEO_LIMIT = 5 # for our example it doesn't seem to matter if the limit is 1 or 5
STATE_CODE = "AZ"
COUNTRY_CODE = 840 # usa
# http://api.openweathermap.org/geo/1.0/direct?q=Tucson,AZ,840&limit=5&appid=ef9f1df2479efce4d227d3a18b38c256
# The above line is Tested

url = "http://api.openweathermap.org/geo/1.0/direct?q={},{},{}&limit={}&appid={}"

response = requests.get(url.format(CITY, STATE_CODE, COUNTRY_CODE, GEO_LIMIT, API_KEY)).json()


print("{}\nlat: {}, lon: {}".format(response[0]['name'], response[0]['lat'], response[0]['lon']))
print('\n')


LAT, LON = response[0]['lat'], response[0]['lon']

url = WEATHER_BASE_URL + "lat=" + str(LAT) + "&lon=" + str(LON) + "&APPID=" + API_KEY

response = requests.get(url).json()

#print(response)
print('Temp: {}°\nHumidity: {}%'.format((response['main']['temp'] - 273.15), response['main']['humidity']))

# We put Tucson into the Geocoder and got South Tucson from the weather api,
# The first returned lat/lon data which was fed into the 2nd.

# Django tut for weather app integration.
# https://www.youtube.com/watch?v=lyeK0aE_qRg
