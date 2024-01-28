from datetime import datetime
from pydantic.dataclasses import dataclass

@dataclass
class Example:
    id: int
    name: str
    example_date: datetime = None
    activated: bool = True

    def __post_init__(self):
        self.example_date = datetime.now()