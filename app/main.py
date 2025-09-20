from fastapi import FastAPI
import requests
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

app = FastAPI()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.get("/")
def home():
    return {"message": "Weather Data Analyzer is running!"}

@app.get("/fetch_weather/{city}")
def fetch_weather(city: str):
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            return {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "weather": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"]
            }
        else:
            return {"error": data.get("message", "Unable to fetch weather data")}
    except Exception as e:
        return {"error": str(e)}
