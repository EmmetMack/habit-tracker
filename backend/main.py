from starlite import Starlite, OpenAPIConfig
from sqlalchemy.ext.asyncio import AsyncSession
from starlite.plugins.sql_alchemy import SQLAlchemyConfig, SQLAlchemyPlugin
from controllers.habit import HabitController
from schemas.models import Base

sqlalchemy_config = SQLAlchemyConfig(
    connection_string="sqlite+aiosqlite:///test.sqlite", dependency_key="async_session"
)
sqlalchemy_plugin = SQLAlchemyPlugin(config=sqlalchemy_config)

async def on_startup() -> None:
    """Initialize the DB"""
    async with sqlalchemy_config.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app = Starlite(
    route_handlers=[HabitController],
    on_startup = [on_startup],
    plugins=[sqlalchemy_plugin],
    openapi_config=OpenAPIConfig(title="Habit API", version="1.0.0")
)