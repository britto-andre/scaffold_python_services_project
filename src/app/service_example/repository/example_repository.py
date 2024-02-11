from pymongo import MongoClient

from src.app.common.utils.logger import logger
from src.app.service_example.entity.example import Example

class ExampleRepository:

    def create(self, obj: Example):
        with MongoClient() as client:
            collection = client['example_db']['examples']
            result = collection.insert_one(obj.model_dump())
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


    