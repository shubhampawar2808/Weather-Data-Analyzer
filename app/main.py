from fastapi import FastAPI
from app.services.weather_service import get_weather
from app.history import save_weather, get_history

app = FastAPI()


@app.get("/weather/{city}")
def weather(city: str):
    data = get_weather(city)
    if "error" in data:
        return {"error": data["error"]}

    # Save fetched data to history
    save_weather(city, data["temperature"], data["condition"])
    return data


@app.get("/history/{city}")
def history(city: str):
    records = get_history(city)
    if not records:
        return {"message": f"No history found for {city}"}
    return {"history": records}
