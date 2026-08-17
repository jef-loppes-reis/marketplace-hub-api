from typing import ClassVar

from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    AsyncSession,
    async_sessionmaker
)

from marketplace_hub_api.core.configs import settings


DBBaseModel = declarative_base()

# Motor para manipular consultas no banco de dados
engine: AsyncEngine = create_async_engine(
    settings.DB_URL
)

# Controle de conexao com o banco de dados
Session: async_sessionmaker = async_sessionmaker(
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)
