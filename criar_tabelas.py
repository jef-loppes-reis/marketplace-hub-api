from src.marketplace_hub_api.core.database import DBBaseModel, engine
from src.marketplace_hub_api.models import ProdutosModel


async def create_tables() -> None:

    print('MetaData: ', list(DBBaseModel.metadata.tables.keys()))

    async with engine.begin() as conn:
        await conn.run_sync(DBBaseModel.metadata.drop_all)
        await conn.run_sync(DBBaseModel.metadata.create_all)

    print('Tabelas criadas !')


if __name__ == '__main__':
    import asyncio
    asyncio.run(create_tables())
