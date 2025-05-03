from datetime import datetime

import requests
from loguru import logger


def get_data(url, params):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logger.error(f"Error getting data from {url}: {e}")
        return None


def parse_weather_data(data):
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    description = data["weather"][0]["description"]
    icon_name = data["weather"][0]["icon"]
    icon = f"static/icons/{icon_name}_t@4x.png"
    dt = datetime.fromtimestamp(data["dt"])
    weather_date = dt.strftime("%A, %B %d, %Y, %I:%M %p")
    return {
        "city": data["city"],
        "temp": temp,
        "description": description,
        "icon": icon,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "weather_date": weather_date,
    }
