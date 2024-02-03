# from datetime import datetime
# from pydantic.dataclasses import dataclass
from pydantic import BaseModel

# @dataclass
class Example (BaseModel):
    name: str
    description: str
    activated: bool

    def __post_init__(self):
        self.activated = True