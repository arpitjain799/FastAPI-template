from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request

{%- if cookiecutter.enable_taskiq == "True" %}
from taskiq import TaskiqDepends
{%- endif %}


async def get_db_session(request: Request {%- if cookiecutter.enable_taskiq == "True" %} = TaskiqDepends(){%- endif %}) -> AsyncGenerator[AsyncSession, None]:
    """
    Create and get database session.

    :param request: current request.
    :yield: database session.
    """
    session: AsyncSession = request.app.state.db_session_factory()

    try:  # noqa: WPS501
        yield session
    finally:
        await session.commit()
        await session.close()
