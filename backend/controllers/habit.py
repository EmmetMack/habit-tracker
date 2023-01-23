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
        #make DB call to partially update habit
        new_habit_data = data.to_model_instance()
        print(f"DATA dictionary: {new_habit_data.__dict__()}")
        result = await async_session.execute(
            update(Habit).where(Habit.id==habit_id).values(json.dumps(new_habit_data.__dict__()))
        )
        updated_habit: Habit | None = result.one_or_none()
        if not updated_habit:
            raise HTTPException(detail=f"No habit with id: {habit_id} found, update could not be completed", status_code=HTTP_404_NOT_FOUND) 
        return updated_habit

    @put(path="{habit_id:int}")
    async def update_user(self, habit_id: int, data: UpdateHabitDTO, async_session: AsyncSession) -> Habit:
        #make DB call to completely update a habit
        updated_habit_data = data.to_model_instance()
        result = await async_session.execute(
            update(Habit).where(Habit.id==habit_id).values(updated_habit_data)
        )
        updated_habit: Habit | None = result.one_or_none()
        if not updated_habit:
            raise HTTPException(detail=f'No habit with id: {habit_id} found and thus not updated', status_code=HTTP_404_NOT_FOUND)
        return updated_habit

    @get(path='/{habit_id:int}')
    async def get_habit(self, habit_id: int, async_session: AsyncSession) -> Habit:
        #make DB call to get a habit
        result = await async_session.scalars(select(Habit).where(Habit.id == habit_id))
        habit: Habit | None = result.one_or_none()
        if not habit:
            raise HTTPException(detail=f'Habit with ID {habit_id} not found', status_code=HTTP_404_NOT_FOUND)
        return habit

    # @delete(path='/{habit_id:uuid}')
    # async def delete_habit(self, user_id:UUID4) -> None:
    #     #delete habit from db
    #     return 