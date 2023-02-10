from sqlalchemy.ext.asyncio import AsyncSession


class BaseCRUD:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def __aenter__(self):
        await self.session.begin()
        return self

    async def __aexit__(self, exc_type, exc, td):
        await self.session.close()
