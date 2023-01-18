from starlite import Controller, Partial, get, post, put, patch, delete, HTTPException
from starlite.status_codes import HTTP_404_NOT_FOUND
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from schemas.models import CreateHabitDTO, Habit
from pydantic import UUID4


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
    async def list_users(self) -> list[Habit]:
        #make DB call to get a list of the habits
        return

    @patch(path="/{habit_id:uuid}")
    async def partial_update_habit(self, habit_id: UUID4, data: Partial[Habit]) -> Habit:
        #make DB call to partially update habit
        return

    @put(path="{habit_id:uuid}")
    async def update_user(self, habit_id: UUID4, data: Habit) -> Habit:
        #make DB call to completely update a habit
        return

    @get(path='/{habit_id:int}')
    async def get_habit(self, habit_id: int, async_session: AsyncSession) -> Habit:
        #make DB call to get a habit
        result = await async_session.scalars(select(Habit).where(Habit.id == habit_id))
        habit: Habit | None = result.one_or_none()
        if not habit:
            raise HTTPException(detail=f'Habit with ID {habit_id} not found', status_code=HTTP_404_NOT_FOUND)
        return habit

    @delete(path='/{habit_id:uuid}')
    async def delete_habit(self, user_id:UUID4) -> None:
        #delete habit from db
        return 