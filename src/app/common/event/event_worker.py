import pika
from src.app.common.utils.logger import logger
from src.app.common.settings.common_settings import CommonSettings

class EventWorker:

    def __init__(self):
        self.settings = CommonSettings()
        self.rabbit_params = pika.URLParameters(self.settings.amqp_uri)
        self.rabbit_params.socket_timeout = 5
    
    def start_consuming(self, queue_name, callback, auto_ack):

        with pika.BlockingConnection(self.rabbit_params) as connection:
            channel = connection.channel()
            channel.queue_declare(queue=queue_name)
            channel.basic_consume(queue_name, callback, auto_ack)
            
            logger.info(f'Start Consuming queue {queue_name} with auto_ack {auto_ack}.')
            channel.start_consuming()
