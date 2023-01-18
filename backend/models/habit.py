from pydantic import BaseModel, UUID4
from datetime import datetime

class Habit(BaseModel):
    id: UUID4
    name: str
    description: str
    creation_ts: datetime = None
