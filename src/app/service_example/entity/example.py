# from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from src.app.common.utils.field_util import PyObjectId

class Example (BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id', default=None)
    name: str
    description: str
    activated: bool

    # def model_post_init(self):
    #     self.activated = True