from pydantic import UUID4
from starlite import Controller, Partial, get, post, put, patch, delete 

from models import Habit

class HabitController(Controller):
    path = "/habits"

    @post()
    async def create_habit(self, data: Habit) -> Habit:
        #make DB call to create a habit
        return

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

    @get(path='/{habit_id:uuid}')
    async def get_habit(self, habit_id: UUID4) -> Habit:
        #make DB call to get a habit
        return

    @delete(path='/{habit_id:uuid}')
    async def delete_habit(self, user_id:UUID4) -> None:
        #delete habit from db
        return 