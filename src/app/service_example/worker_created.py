import json
from src.app.common.utils.logger import logger
from src.app.common.event.event_worker import EventWorker
from src.app.common.event.event import Event

def callback(channel, method, properties, body):
  event = Event(**json.loads(body))
  logger.info(f'Event {event.uuid} read.')
  logger.info(f'Example {event.aggregate_id} -> {event.payload}.')

def run():
  worker = EventWorker()
  worker.start_consuming('example_created', callback, True)