from src.app.service_example.entity.example import Example
from src.app.common.settings.common_settings import CommonSettings
from src.app.common.repository.default_repository import DefaultRepository

class ExampleRepository(DefaultRepository):

    def __init__(self):
        super().__init__()
    
    def _collection(self, client):
        return client['example_db']['examples']

    def create(self, obj: Example):
        with super().client() as client:
            result = self._collection(client).insert_one(obj.model_dump())
            return result.inserted_id

            # return {"insertion": ack}

        # new_student = await student_collection.insert_one(
    #     student.model_dump(by_alias=True, exclude=["id"])
    # )
    # created_student = await student_collection.find_one(
    #     {"_id": new_student.inserted_id}
    # )
        # To-do
        # persist object
        # persist event
        # publish event


    