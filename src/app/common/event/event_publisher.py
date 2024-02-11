import pika
from src.app.common.utils.logger import logger
from src.app.common.settings.common_settings import CommonSettings
from src.app.common.event.event import EventBuilder

class EventPublisher:

    def __init__(self, settings: CommonSettings):
        self.settings = settings
        self.rabbit_params = pika.URLParameters(self.settings.amqp_uri)
        self.rabbit_params.socket_timeout = 5

    def publish(self, payload_id, payload, event_name):
        event = EventBuilder().build(payload_id = payload_id,
                                     payload = payload,
                                     event_name = event_name,
                                     sender = self.settings.event_sender)
        event_queue_store = self.settings.event_queue_store
        queue = event_name

        with pika.BlockingConnection(self.rabbit_params) as connection:
            # Store Event
            channel_store = connection.channel()
            channel_store.queue_declare(queue=event_queue_store)
            channel_store.basic_publish(exchange='', routing_key=event_queue_store,  body=event.body_message())

            # Publish Event
            channel = connection.channel()
            channel.queue_declare(queue=queue)
            channel.basic_publish(exchange='', routing_key=queue,  body=event.body_message())
