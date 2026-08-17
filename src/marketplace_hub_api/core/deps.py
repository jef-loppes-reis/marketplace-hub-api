from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from marketplace_hub_api.core.database import Session


async def get_session() -> AsyncGenerator:
    """Manipula a sessao para uso. Abre e fecha a conexao com o banco de dados.

    Returns
    -------
    AsyncGenerator
        _description_

    Yields
    ------
    Iterator[AsyncGenerator]
        _description_
    """    

    session: AsyncSession = Session()

    try:
        yield session
    finally:
        await session.close()
