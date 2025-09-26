# app/history.py
from app.database import SessionLocal, engine, Base
from app.models import WeatherHistory

# create tables if not existing
Base.metadata.create_all(bind=engine)

def save_weather(data: dict):
    """
    data expected keys: city, temperature, description
    """
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
        return {
            "id": record.id,
            "city": record.city,
            "temperature": record.temperature,
            "description": record.description,
            "timestamp": record.timestamp.isoformat()
        }
    finally:
        db.close()

def get_history(city: str = None, limit: int = 100):
    db = SessionLocal()
    try:
        q = db.query(WeatherHistory)
        if city:
            q = q.filter(WeatherHistory.city.ilike(f"%{city}%"))
        q = q.order_by(WeatherHistory.timestamp.desc()).limit(limit)
        records = q.all()
        return [
            {
                "id": r.id,
                "city": r.city,
                "temperature": r.temperature,
                "description": r.description,
                "timestamp": r.timestamp.isoformat()
            } for r in records
        ]
    finally:
        db.close()
