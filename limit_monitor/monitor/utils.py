import requests
from django.conf import settings

def fetch_weather_data(location):
    url = f"https://api.weatherapi.com/v1/current.json?key={settings.WEATHER_API_KEY}&q={location}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching weather data: {response.status_code}")
        return None  # Handle errors appropriately (e.g., raise exception)
