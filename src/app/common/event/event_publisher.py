import pika
from src.app.common.utils.logger import logger
from src.app.common.utils.str_util import camel_to_snake
from src.app.common.settings.common_settings import CommonSettings

class EventPublisher:

    def __init__(self, settings: CommonSettings):
        logger.info(f'settings {settings}')
        logger.info(f'settings {settings.event_sender}')
        logger.info(f'settings {settings.environment}')
        self.rabbit_params = pika.URLParameters('amqp://guest:guest@localhost/%2f')
        self.rabbit_params.socket_timeout = 5

    def publish(self, payload):
        logger.info(f'add from {self.__class__.__name__}')
        logger.info(f'add from {camel_to_snake(self.__class__.__name__)}')
        logger.debug(f'obj class {payload.__class__.__name__}')
        logger.debug(f'obj class {camel_to_snake(payload.__class__.__name__)}')
        logger.debug(f'self.rabbit_params {self.rabbit_params}')

        # connection = pika.BlockingConnection(self.params)

        # channel = connection.channel() # start a channel
        # channel.queue_declare(queue='example_created') # Declare a queue
        
        # # send a message    
        # channel.basic_publish(exchange='example_exchange', routing_key='', body=b'Test message Britto.')
        # connection.close()
