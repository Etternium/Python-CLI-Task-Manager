from pydantic import BaseModel, field_serializer
from datetime import datetime

class TaskResponse(BaseModel):
    id: int
    description: str
    complete: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode=True
        
    @field_serializer("created_at", "updated_at")
    def serialize_datetime(self, value: datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")