from typing import Any
from starlite import Controller, Partial, get, post, put, patch, delete, HTTPException
from starlite.status_codes import HTTP_404_NOT_FOUND
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from schemas.models import CreateHabitDTO, Habit, PartialHabitDTO, UpdateHabitDTO
import json
from pydantic import UUID4
from datetime import datetime


class HabitController(Controller):
    path = "/habits"

    @post()
    async def create_habit(self, data: CreateHabitDTO, async_session: AsyncSession) -> Habit:
        #make DB call to create a habit
        habit: Habit = data.to_model_instance()
        async_session.add(habit)
        await async_session.commit()
        return habit

    @get()
    async def list_users(self, async_session: AsyncSession) -> list[Habit]:
        #make DB call to get a list of the habits
        result = await async_session.scalars(select(Habit).order_by(Habit.id))
        habits: Habit | None = result.all()
        if not habits:
            raise HTTPException(detail=f'No habits created', status_code=HTTP_404_NOT_FOUND)
        return habits

    @patch(path="/{habit_id:int}")
    async def partial_update_habit(self, habit_id: int, data: PartialHabitDTO, async_session:AsyncSession) -> Habit:
        #make DB call to completely update a habit
        current_habit: Habit = await self._get_habit(habit_id, async_session)
    
        for key, value in data.dict().items():
            if value:
                setattr(current_habit, key, value) 
        async_session.add(current_habit)
        await async_session.commit()
        return current_habit

    @put(path="{habit_id:int}")
    async def update_habit(self, habit_id: int, data: UpdateHabitDTO, async_session: AsyncSession) -> Habit:
        #make DB call to completely update a habit or create it if it doesn't exist
        
        try: #if already exists then update fields
            current_habit = await self._get_habit(habit_id, async_session)
            for key, value in data.dict().items():
                if value:
                    setattr(current_habit, key, value) 
        except HTTPException: #if it doesn't exist then create a new habit with the id
            current_habit: Habit = data.to_model_instance()
            current_habit.id = habit_id
                 
        async_session.add(current_habit)
        await async_session.commit()
        return current_habit
        

    @get(path='/{habit_id:int}')
    async def get_habit(self, habit_id: int, async_session: AsyncSession) -> Habit:
        #make DB call to get a habit
        habit = await self._get_habit(habit_id, async_session)
        
        return habit

    @delete(path='/{habit_id:int}')
    async def delete_habit(self, habit_id:int, async_session: AsyncSession) -> None:
        #delete habit from db
        habit = await self._get_habit(habit_id, async_session)
        await async_session.delete(habit)
        await async_session.commit()
        return

    async def _get_habit(self, habit_id: int, async_session: AsyncSession) -> Habit:
        #helper function to make the query to get a habit
        result = await async_session.scalars(select(Habit).where(Habit.id==habit_id))

        habit: Habit | None = result.one_or_none()
        if not habit:
            raise HTTPException(detail=f'Habit with ID {habit_id} not found', status_code=HTTP_404_NOT_FOUND)

        return habit