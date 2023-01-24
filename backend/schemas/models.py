from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func
from datetime import datetime
from starlite import DTOFactory
from starlite.types.partial import Partial
from starlite.plugins.sql_alchemy import SQLAlchemyPlugin

Base = declarative_base()

SQLAlchemyDTOFactory = DTOFactory(plugins=[SQLAlchemyPlugin()])

class Habit(Base):
    __tablename__ = "habits"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    creation_ts: Mapped[datetime] = mapped_column(DateTime, default=func.now())

CreateHabitDTO = SQLAlchemyDTOFactory("CreateHabitDTO", Habit, exclude=['id', 'creation_ts'])
UpdateHabitDTO = SQLAlchemyDTOFactory("UpdateHabitDTO", Habit, exclude=["id", "creation_ts"])
PartialHabitDTO = Partial[UpdateHabitDTO]