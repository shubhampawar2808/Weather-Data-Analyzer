from fastapi import FastAPI, HTTPException
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

app = FastAPI(title="Weather Data Analyzer", version="1.0")

# Root route
@app.get("/")
def read_root():
    return {"message": "🌦️ Welcome to Weather Data Analyzer API!"}

# Weather route
@app.get("/weather/{city}")
def get_weather(city: str):
    if not API_KEY:
        raise HTTPException(status_code=500, detail="API key not found. Please set WEATHER_API_KEY in .env")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="City not found or API request failed")

    data = response.json()

    # Extract useful info
    result = {
        "city": data["name"],
        "temperature": f"{data['main']['temp']} °C",
        "feels_like": f"{data['main']['feels_like']} °C",
        "weather": data["weather"][0]["description"].capitalize(),
        "humidity": f"{data['main']['humidity']}%",
        "wind_speed": f"{data['wind']['speed']} m/s"
    }

    return result
