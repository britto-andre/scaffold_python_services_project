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
        self.publisher.publish(obj_id, obj, 'exemple_created')

    def update_name(self, id: str, name: str):
        logger.info(f'update_name -> id: {id}, name: {name}')

    def delete(self, id: str):
        logger.info(f'delete -> id: {id}')