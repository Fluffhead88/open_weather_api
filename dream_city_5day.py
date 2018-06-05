import requests
import datetime

api_key = 'be719e8432aa621a508a5bba848e6bfe' # Put your API key in this string.

test_url = 'http://api.openweathermap.org/data/2.5/forecast?q=Athens,us&APPID=' + api_key +'&units=imperial'
resp = requests.get(test_url)
if resp.status_code in [200, 201]:
    weather_data = resp.json()

    my_data = weather_data['list']

    for x in my_data[0::4]:
        print("In {}, GA the weather is {} and the temperature is {} degrees on {}.\n".format(weather_data['city']['name'], x['weather'][0]['description'], x['main']['temp'], x['dt_txt']))

else:
    print("ERROR: " + str(resp.status_code))
