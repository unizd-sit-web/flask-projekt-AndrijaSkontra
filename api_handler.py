import json
import os

import requests


class APIHandler:
    def __init__(self, city):
        self.city = city
        self.api_key = os.environ.get("WEATHERAPI")
        self.url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&lang=hr&appid=2ca5630c7892ba8104791e904382120d"
        self.json_weather = requests.get(self.url).json()

    def get_weather_data(self):
        weather_list = []
        description = self.json_weather["weather"][0]["description"]
        feels_like_K = self.json_weather["main"]["feels_like"]
        feels_like_C = feels_like_K - 273.15
        icon = self.json_weather["weather"][0]["icon"]
        weather_list.append(description)
        weather_list.append(f"{round(feels_like_C, 2)}")
        weather_list.append(icon)
        return weather_list

    def get_wind_data(self):
        return self.json_weather["wind"]["speed"], self.json_weather["wind"]["deg"]
