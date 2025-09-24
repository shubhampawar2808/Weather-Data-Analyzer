import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city: str):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code != 200:
        return {"error": data.get("message", "Failed to fetch weather")}

    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["description"]
    }
