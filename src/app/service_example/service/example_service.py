from src.app.common.utils.logger import logger
from src.app.service_example.entity.example import Example

class ExampleService:

    def create(self, obj: Example):
        # To-do
        # persist event
        # publish event
        logger.info(obj)