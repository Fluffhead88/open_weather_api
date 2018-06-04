import requests

api_key = 'be719e8432aa621a508a5bba848e6bfe' # Put your API key in this string.

test_url = 'http://api.openweathermap.org/data/2.5/weather?q=Greenville&APPID=' + api_key
resp = requests.get(test_url)
if resp.status_code in [200, 201]:
    weather_data = resp.json()
    print("The weather in {} is {}.".format(weather_data['name'],
                                            weather_data['weather'][0]['description']))
else:
    print("ERROR: " + str(resp.status_code))
