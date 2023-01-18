from starlite import Starlite

from controllers.habit import HabitController

app = Starlite(route_handlers=[HabitController])

