import datetime as dt

import requests
from apikey import apikey
#import geocoder

from django.shortcuts import render

# Create your views here.

def index(request):
	API_KEY = apikey.key
#	API_KEY = open('/home/jameswebb/django_projects/mysite/weater_app/apikey.txt','r').read().strip()
	WEATHER_BASE_URL = 'https://api.openweathermap.org/data/2.5/weather/?q='

	current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
	forecast_url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}"

	if request.method == "POST":
		city1 = request.POST['city1']
		city2 = request.POST.get('city2', None) # I don't think I wasn to include this functionality in my final version of the project. Thinking for the moment I want one location to display the weather kind of in the background but make the location customizable.

		weather_data1, daily_forcasts1 = fetch_weather_and_forcast(city1, API_KEY, current_weather_url, forcast_url)

		if city2:
			weather_data2, daily_forcasts2 = fetch_weather_and_forcast(city1, API_KEY, current_weather_url, forcast_url)
		else:
			weather_data2, daily_forcasts2 = None, None

		context = {
			"weather_data1": weather_data1,
			"daily_forcasts1": daily_forcasts1,
			"weather_data2": weather_data2,
			"daily_forcasts2": daily_forcasts2
		}

		return render(request, "weather_app/index.html", context)

	else: # if it's a get request
		return render(request, "weather_app/index.html")

# In my final version I don't think I'm interested in having a forcast, at least not displayed all the time. maybe on click/on mouseover add it in?
def fetch_weather_and_forcast(city, api_key, current_weather_url, forecast_url):
	response = requests.get(current_weather_url.format(city, apikey)).json() # This is interesting, I hadn't though of setting up the string then in a later line doing the .format.
	lat, lon = response['coord']['lat'], response['coord']['lon']
	forcast_response = requests.get(forcast_url.format(lat, lon, api_key)).json()

	weather_data = {
		"city": city,
		"temerature": round(response['main']['temp'] - 273.15, 2),
		"description": response['weather'][0]['description'],
		"icon": response['weather'][0]['icon']
	}

	daily_forcasts = []
	for daily_data in forcast_response['daily'][:5]:
		daily_forcasts.append({
			"day": datetime.datetime.fromtimestamp(daily_data['dt']).strftime("%A"),
			"min_temp": round(daily_data['temp']['min'] - 273.15, 2),
			"max_temp": round(daily_data['temp']['max'] - 273.15, 2),
			"description": daily_data['weather'][0]['description'],
			"icon": daily_data['weather'][0]['icon']
		})
	return weather_data, daily_forcasts


# This is ordered backwards for the moment.
#CITY = "Tucson"
#        GEO_LIMIT = 1
#        STATE_CODE = "AZ"
#        COUNTRY_CODE = 840 # usa
#
#        GEO_BASE_URL = "http://api.openweathermap.org/geo/1.0/direct?"
#        url = GEO_BASE_URL + CITY + "," + STATE_CODE + "," + str(COUNTRY_CODE) + "&limit=" + str(GEO_LIMIT) + "&appid=" + API_KEY
#        response = requests.get(url).json()
#
#        #print(response)
#        #print('\n')
#
#        LAT, LON = response[0]['lat'], response[0]['lon']
#        url = WEATHER_BASE_URL + "lat=" + str(LAT) + "&lon=" + str(LON) + "&APPID=" + API_KEY
#        response = requests.get(url).json()
#print(response)
#
# https://www.youtube.com/watch?v=lyeK0aE_qRg
# stopped at 19:24, but I need to run this back as I'm having trouble staying focused.
