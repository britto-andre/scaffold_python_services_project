from datetime import datetime
from pydantic.dataclasses import dataclass

@dataclass
class Event:
    _id: int
    event_name: str
    aggregate_id: int
    aggregate_type: str
    sender: str
    payload: object
    date_time: datetime = None
    version: str = '0.1'

    def __post_init__(self):
        self.example_date = datetime.now()