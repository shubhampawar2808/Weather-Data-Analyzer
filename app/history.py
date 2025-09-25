# app/history.py
from app.database import SessionLocal, engine, Base
from app.models import WeatherHistory

# Create tables
Base.metadata.create_all(bind=engine)

def save_weather(data: dict):
    db = SessionLocal()
    try:
        record = WeatherHistory(
            city=data.get("city"),
            temperature=data.get("temperature"),
            description=data.get("description")
        )
        db.add(record)
        db.commit()
        db.refresh(record)
        return record
    finally:
        db.close()
