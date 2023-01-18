from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Column, DateTime, Integer, String, select
from datetime import datetime
from starlite import DTOFactory
from starlite.plugins.sql_alchemy import SQLAlchemyPlugin

Base = declarative_base()

SQLAlchemyDTOFactory = DTOFactory(plugins=[SQLAlchemyPlugin()])

class Habit(Base):
    __tablename__ = "habits"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    creation_ts: Mapped[datetime] = mapped_column(DateTime)

CreateHabitDTO = SQLAlchemyDTOFactory("CreateHabitDTO", Habit, exclude=['id'])
