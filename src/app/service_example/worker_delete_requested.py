import json
from src.app.common.utils.logger import logger
from src.app.common.event.event_worker import EventWorker
from src.app.common.event.event import Event

from src.app.service_example.service.example_service import ExampleService

service = ExampleService()

def callback(channel, method, properties, body):
  event = Event(**json.loads(body))
  logger.info(f'Event {event.uuid} read.')
  service.delete(event.aggregate_id)
  logger.info(f'Example {event.aggregate_id} deleted.')

def run():
  worker = EventWorker()
  worker.start_consuming('example_delete_requested', callback, True)