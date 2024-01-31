from src.app.common.service.default_service import DefaultService
from src.app.common.utils.logger import logger
from src.app.service_example.entity.example import Example

class ExampleService(DefaultService):

    def persist(self, obj: Example):
        # To-do
        # persist event
        # publish event
        logger.info(obj)