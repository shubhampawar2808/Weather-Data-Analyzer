from fastapi import FastAPI
import requests
import os
import json

app = FastAPI()

DATA_DIR = "../data"
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your API key

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

@app.get("/fetch_weather")
def fetch_weather(city: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    # Save JSON file
    file_path = os.path.join(DATA_DIR, f"{city}.json")
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    
    return {"message": f"Weather data for {city} saved successfully!"}
