from pymongo import MongoClient

from src.app.common.utils.logger import logger
from src.app.service_example.entity.example import Example

class ExampleRepository:

    def create(self, obj: Example):
        with MongoClient() as client:
            msg_collection = client['example_db']['examples']
            result = msg_collection.insert_one(obj.dict())
            ack = result.acknowledged
            logger.info(f'create repository -> obj {obj} - {ack}')
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


    