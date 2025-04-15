
from dotenv import load_dotenv
import os
import requests


load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")
DAYS = 1
LANG = 'ru'
AQI = 'yes'


def load_data(city):
    response = requests.get(API_URL, params={'key': API_KEY, 'q': city, 'days': DAYS, 'aqi': AQI, 'lang': LANG})
    data = response.json()

    location = data['location']
    forecast_days = data['forecast']['forecastday']
    forecast_hours = forecast_days[0]['hour']
    
    city_name = location['name']
    current = data['current']
    icon = current['condition']['icon']
    condition = current['condition']['text']
    temp = current['temp_c']
    hours = [h['time'][-5:] for h in forecast_hours]
    temps = [h['temp_c'] for h in forecast_hours]
    
    air = data['current']['air_quality']
    
    co = [h['air_quality']['co'] for h in forecast_hours]
    no2 = [h['air_quality']['no2'] for h in forecast_hours]
    o3 = [h['air_quality']['o3'] for h in forecast_hours]
    so2 = [h['air_quality']['so2'] for h in forecast_hours]
    pm2_5 = [h['air_quality']['pm2_5'] for h in forecast_hours]
    pm10 = [h['air_quality']['pm10'] for h in forecast_hours]

    return {"location": location,
            "city_name": city_name,
            "icon": icon,
            "temp": temp,
            "hours": hours,
            "temps": temps,
            "co": co,
            "no2": no2,
            "o3": o3,
            "so2": so2,
            "pm2_5": pm2_5,
            "pm10": pm10,
            "condition": condition}
