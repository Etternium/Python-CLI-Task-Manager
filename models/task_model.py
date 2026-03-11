from database import Base
from sqlalchemy import Column, String, Boolean, Integer

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    complete = Column(Boolean, default=False)