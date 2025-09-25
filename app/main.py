from fastapi import FastAPI
from app.services.weather_service import get_weather
from app.history import save_weather
from app.database import SessionLocal
from app.models import WeatherHistory

app = FastAPI()


@app.get("/weather/{city}")
def read_weather(city: str):
    """Fetch weather for a city and save it to DB"""
    data = get_weather(city)
    save_weather(data)  # DB मध्ये save
    return data


@app.get("/history")
def get_history():
    """Get all saved weather history from DB"""
    db = SessionLocal()
    try:
        records = db.query(WeatherHistory).all()
        return records
    finally:
        db.close()
