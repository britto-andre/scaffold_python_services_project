from src.app.common.repository.default_repository import DefaultRepository
from src.app.common.event.event import Event

class EventRepository(DefaultRepository):

    def __init__(self):
        super().__init__()
    
    def _collection(self, client):
        return client['event_db']['events']

    def create(self, obj: Event):
        with super().client() as client:
            result = self._collection(client).insert_one(obj.model_dump(by_alias=True, exclude=["id"]))
            return result.inserted_id

    def find_by_example(self, example):
        with super().client() as client:
            results = self._collection(client).find(example)
            return list(map(lambda r: Event(**r), results))