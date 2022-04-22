# today may be cloudy but tomorrow will be a better day
# keep the streak alive!!

import requests

API_KEY = "f9f2f48d25f6c8d6da3d188b16ffc993"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print(weather)
    temp = round(data['main']['temp'] - 273.15, 2)


    print("Weather:", weather)
    print("Temperature:", temp, "celsius")

else:
    print("An error occured")
