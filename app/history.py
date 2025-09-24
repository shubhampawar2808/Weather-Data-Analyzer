import csv
from datetime import datetime

FILE_NAME = "weather_history.csv"

# Save weather data
def save_weather(city, temperature, condition):
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([city, temperature, condition, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

# Get city weather history
def get_history(city):
    records = []
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].lower() == city.lower():
                    records.append({
                        "city": row[0],
                        "temperature": row[1],
                        "condition": row[2],
                        "timestamp": row[3]
                    })
    except FileNotFoundError:
        return []
    return records
