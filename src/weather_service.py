import os

from utils import get_data


appid = os.environ.get("WEATHER_API_KEY")

class WeatherService:
    def __init__(self, city_name):
        self.city_name = city_name

    def _get_coordinates(self):
        url = "http://api.openweathermap.org/geo/1.0/direct"
        params = {"q": self.city_name, "limit": 5, "appid": appid}
        return get_data(url, params)

    def get_weather_data(self):
        coordinates = self._get_coordinates()
        if not coordinates:
            return {}
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "lat": coordinates[0]["lat"],
            "lon": coordinates[0]["lon"],
            "units": "metric",
            "appid": appid
        }
        weather_data = get_data(url, params)
        if not weather_data:
            return {}
        weather_data["city"] = coordinates[0]["name"]
        return weather_data
