from pymongo import MongoClient

from src.app.common.event.event import Event

class EventRepository:

    def create(self, event: Event):
        with MongoClient() as client:
            event_collection = client['event_db']['events']
            result = event_collection.insert_one(event.model_dump())
            return result.inserted_id