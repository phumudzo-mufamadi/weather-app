from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify

from utils import parse_weather_data
from weather_service import WeatherService

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weather", methods=["GET"])
def weather():
    city = request.args.get("city")
    weather_service = WeatherService(city)
    weather_data = weather_service.get_weather_data()
    if not weather_data:
        return jsonify({})
    data = parse_weather_data(weather_data)
    return jsonify(data)
