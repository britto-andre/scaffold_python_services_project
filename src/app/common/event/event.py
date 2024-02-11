from datetime import datetime
from pydantic import BaseModel
import json
import uuid

from src.app.common.utils.str_util import camel_to_snake

class Event (BaseModel):
    uuid: str
    event_name: str
    aggregate_id: int
    aggregate_type: str
    sender: str
    payload: object
    # date_time: datetime
    # version: str = '0.1'

    # def model_post_init(self):
    #     self.date_time = datetime.now()

    def body_message(self):
        return json.dumps(self.model_dump())

class EventBuilder:

    def build(self, payload_id, payload, event_name, sender) -> Event:
        return Event(
            uuid=str(uuid.uuid4()),
            event_name=event_name,
            aggregate_id=payload_id,
            aggregate_type=camel_to_snake(payload.__class__.__name__),
            sender=sender,
            payload=payload.model_dump()
        )