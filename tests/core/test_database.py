import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from marketplace_hub_api.core.database import Session


@pytest.mark.asyncio
async def test_session():
    session = Session()

    assert isinstance(session, AsyncSession)

    await session.close()