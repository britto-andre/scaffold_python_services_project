import json
from src.app.common.utils.logger import logger
from src.app.common.event.event_worker import EventWorker
from src.app.common.event.event import Event
from src.app.service_event_store.service.event_service import EventService

service = EventService()

def callback(channel, method, properties, body):
  event = Event(**json.loads(body))
  logger.info(f'Event {event.uuid} read.')
  service.create(event)

def run():
  worker = EventWorker()
  worker.start_consuming(worker.settings.event_queue_store, callback, True)