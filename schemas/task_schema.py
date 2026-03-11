from pydantic import BaseModel

class TaskResponse(BaseModel):
    id: int
    description: str
    complete: bool

    class Config:
        orm_mode=True