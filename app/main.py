# app/main.py
from fastapi import FastAPI, HTTPException
from app.services.weather_service import get_weather
from app.history import save_weather, get_history

app = FastAPI(title="Weather Data Analyzer")

@app.get("/")
def root():
    return {"message": "Weather Data Analyzer running!"}

@app.get("/weather/{city}")
def weather_endpoint(city: str):
    data = get_weather(city)
    if "error" in data:
        raise HTTPException(status_code=404, detail=data["error"])
    saved = save_weather(data)
    return {"fetched": data, "saved": saved}

@app.get("/history")
def history_endpoint(city: str = None, limit: int = 100):
    records = get_history(city=city, limit=limit)
    if not records:
        return {"message": "No history found"}
    return {"history": records}
