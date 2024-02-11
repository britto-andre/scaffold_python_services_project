# from datetime import datetime
# from pydantic.dataclasses import dataclass
from pydantic import BaseModel

# @dataclass
class Example (BaseModel):
    name: str
    description: str
    activated: bool

    # def model_post_init(self):
    #     self.activated = True