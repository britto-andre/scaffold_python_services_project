from src.app.service_example.entity.example import Example
from src.app.common.repository.default_repository import DefaultRepository

class ExampleRepository(DefaultRepository):

    def __init__(self):
        super().__init__()
    
    def _collection(self, client):
        return client['example_db']['examples']

    def create(self, obj: Example):
        with super().client() as client:
            result = self._collection(client).insert_one(obj.model_dump(by_alias=True, exclude=["id"]))
            return result.inserted_id
        
    def find_one_by_id(self, id):
        with super().client() as client:
            result = self._collection(client).find_one(super().obj_id(id))
            if result:
                return Example(**result)
            return {}

    def find_by_example(self, example):
        with super().client() as client:
            results = self._collection(client).find(example)
            return list(map(lambda r: Example(**r), results))    