from src.app.common.service.default_service import DefaultService
from src.app.common.utils.logger import logger
from src.app.service_example.entity.example import Example

class ExampleService(DefaultService):

    def create(self, obj: Example):
        # To-do
        # persist object
        # persist event
        # publish event
        logger.info(f'create -> obj {obj}')

    def update_name(self, id: str, name: str):
        # To-do
        # persist event
        # publish event
        logger.info(f'update_name -> id: {id}, name: {name}')

    def delete(self, id: str):
        # To-do
        # persist event
        # publish event
        logger.info(f'delete -> id: {id}')