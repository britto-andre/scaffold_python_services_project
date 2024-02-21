from src.app.common.utils.logger import logger
from src.app.common.service.default_service import DefaultService
from src.app.service_example.entity.example import Example
from src.app.service_example.repository.example_repository import ExampleRepository

class ExampleService(DefaultService):

    def __init__(self) -> None:
        super().__init__()
        self.repository = ExampleRepository()

    def create(self, obj: Example):
        obj_id = self.repository.create(obj)
        logger.info(f'Example Created with _id {obj_id}.')
        self.publisher.publish(obj_id, obj, 'example_created')
        return obj_id

    def list(self):
        return self.repository.find_by_example({})
    
    def find_one_by_id(self, id):
        return self.repository.find_one_by_id(id)

    def update_name(self, id: str, name: str):
        logger.info(f'update_name -> id: {id}, name: {name}')

    
    def request_delete(self, id: str):
        obj = self.repository.find_one_by_id(id)
        if obj:
            self.publisher.publish(id, obj, 'example_delete_requested')
            return True
        return False

    def delete(self, id: str):
        obj = self.repository.find_one_by_id(id)
        if obj:
            self.repository.delete(obj)
            return True
        return False