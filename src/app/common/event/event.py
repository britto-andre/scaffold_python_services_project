import uuid

from datetime import datetime
from typing import Annotated, Optional
from pydantic import BaseModel, BeforeValidator, Field

from src.app.common.utils.str_util import camel_to_snake

PyObjectId = Annotated[str, BeforeValidator(str)]

class Event (BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id', default=None)
    uuid: str
    event_name: str
    aggregate_id: str
    aggregate_type: str
    sender: str
    payload: object
    created_time: datetime

    def model_post_init(self, *args, **kwargs):
        if self.created_time == None: self.created_time = datetime.now()


class EventBuilder:

    def build(self, payload_id, payload, event_name, sender) -> Event:
        return Event(
            uuid=str(uuid.uuid4()),
            event_name=event_name,
            aggregate_id=str(payload_id),
            aggregate_type=camel_to_snake(payload.__class__.__name__),
            sender=sender,
            payload=payload.model_dump(by_alias=True, exclude=["id"]),
            created_time=datetime.now()
        )