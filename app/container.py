import typing as t

from dependency_injector import containers
from dependency_injector import providers
from pydantic_settings import BaseSettings
from redis.asyncio import ConnectionPool
from redis.asyncio import Redis

__all__ = ('AppContainer',)


async def init_redis_pool(host: str) -> t.AsyncGenerator[ConnectionPool]:
    pool = ConnectionPool.from_url(host, encoding="utf-8", decode_responses=True)
    yield pool
    await pool.aclose()


class CsGoMarketSettings(BaseSettings):
    redis_url: str


class AppContainer(containers.DeclarativeContainer):
    config = CsGoMarketSettings()
    redis_pool = providers.Resource(init_redis_pool, host=config.redis_url)
    redis_con = providers.Factory(Redis.from_pool, connection_pool=redis_pool)
