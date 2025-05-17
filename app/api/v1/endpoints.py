import typing as t

from dependency_injector.wiring import inject
from dependency_injector.wiring import Provide
from fastapi import APIRouter
from fastapi import Depends
from fastapi import FastAPI
from pydantic_extra_types.phone_numbers import PhoneNumber
from redis.asyncio import Redis
from starlette.responses import JSONResponse

from app.container import AppContainer
from app.models import WriteDataModel

__all__ = ('init_ep_something',)


def init_ep_something(app: FastAPI) -> None:
    endpoints_v1 = APIRouter(prefix="/api/v1/something", tags=["something"])

    @endpoints_v1.post('/write_data')
    @inject
    async def write_data(
        data: WriteDataModel,
        redis_con: t.Annotated[Redis, Depends(Provide[AppContainer.redis_con])],
    ) -> None:
        """ Сохранить/Обновить текущую информацию о номере """
        await redis_con.set(name=data.phone, value=data.address)

    @endpoints_v1.get('/check_data')
    @inject
    async def check_data(
        phone: PhoneNumber,
        redis_con: t.Annotated[Redis, Depends(Provide[AppContainer.redis_con])],
    ) -> JSONResponse:
        """ Получить адрес по номеру телефона """
        value = await redis_con.get(name=phone)
        return JSONResponse(content={"data": value})

    app.include_router(endpoints_v1)
