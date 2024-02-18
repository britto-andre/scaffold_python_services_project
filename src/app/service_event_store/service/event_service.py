from src.app.common.utils.logger import logger
from src.app.common.service.default_service import DefaultService
from src.app.common.event.event import Event
from src.app.service_event_store.repository.event_repository import EventRepository

class EventService(DefaultService):

    def __init__(self) -> None:
        super().__init__()
        self.repository = EventRepository()

    def create(self, obj: Event):
        obj_id = self.repository.create(obj)
        logger.info(f'Event {obj.uuid} created with _id {obj_id}')

    def list_by_aggregate(self, aggregate_type: str, aggregate_id: str):
        return self.repository.find_by_example({
            'aggregate_type': aggregate_type,
            'aggregate_id': aggregate_id,
        })