import os

import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weather", methods=["GET"])
def weather():
    city = request.args.get("city")
    city_query_url = "http://api.openweathermap.org/geo/1.0/direct"
    city_query_res = requests.get(city_query_url, params={"q": city, "limit": 5, "appid": os.environ.get("WEATHER_API_KEY")})
    city_query_data = city_query_res.json()
    city_data = city_query_data[0]
    city_weather_url = "https://api.openweathermap.org/data/2.5/weather"
    city_weather_res = requests.get(city_weather_url, params={"lat": city_data["lat"], "lon": city_data["lon"], "units": "metric", "appid": os.environ.get("WEATHER_API_KEY")})
    city_weather_data = city_weather_res.json()
    temp = city_weather_data["main"]["temp"]
    return render_template("weather_results.html", temp=temp, city=city)
