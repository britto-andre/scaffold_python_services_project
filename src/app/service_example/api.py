from fastapi import FastAPI
from src.app.common.utils.logger import logger
from src.app.service_example.service.example_service import ExampleService
from src.app.service_example.entity.example import Example

import pika

app = FastAPI()

@app.get("/")
async def home():
    logger.debug('access home.')
    obj = Example(id=1234, name='Teste Name')
    service = ExampleService()
    service.create(obj, 'api', 'queue_test')
    return obj

@app.get("/test")
async def test():

    params = pika.URLParameters('amqp://guest:guest@localhost/%2f')
    params.socket_timeout = 5

    connection = pika.BlockingConnection(params)

    channel = connection.channel() # start a channel
    channel.queue_declare(queue='example_created') # Declare a queue
    
    # send a message    
    channel.basic_publish(exchange='example_exchange', routing_key='', body=b'Test message Britto.')
    connection.close()

    return 'Ok'