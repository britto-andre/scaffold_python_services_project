from fastapi import FastAPI
from src.app.common.utils.logger import logger
from src.app.service_example.service.example_service import ExampleService
from src.app.service_example.entity.example import Example

app = FastAPI()

@app.get("/")
async def home():
    logger.debug('access home.')
    obj = Example(id=1234, name='Teste Name')
    service = ExampleService()
    service.create(obj, 'api', 'queue_test')
    return obj