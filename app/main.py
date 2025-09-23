from fastapi import FastAPI
from app.services.weather_service import get_weather

# Initialize FastAPI app
app = FastAPI(
    title="Weather Data Analyzer",
    description="A simple API to fetch real-time weather data using OpenWeatherMap",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Weather Data Analyzer API is running!"}

@app.get("/weather/{city}")
def fetch_weather(city: str):
    """
    Fetch real-time weather data for a given city
    """
    data = get_weather(city)

    # If error occurred in API
    if "error" in data:
        return data

    # Clean structured response (corporate-level look 😎)
    response = {
        "city": data.get("name"),
        "country": data.get("sys", {}).get("country"),
        "temperature": f"{data.get('main', {}).get('temp')} °C",
        "humidity": f"{data.get('main', {}).get('humidity')}%",
        "weather": data.get("weather", [{}])[0].get("description"),
        "wind_speed": f"{data.get('wind', {}).get('speed')} m/s"
    }
    return response
