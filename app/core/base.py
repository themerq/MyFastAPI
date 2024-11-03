from sqlalchemy.future import select
from app.database import async_session_maker


class BaseCore:
    model = None

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

@classmethod
async def delete_product_by_id(cls, product_id: int):
    async with async_session_maker() as session:
        async with session.begin():
            query = select(cls.model).filter_by(id=product_id)
            result = await session.execute(query)
            product_to_delete = result.scalar_one_or_none()

            if not product_to_delete:
                return None

            # Удаляем товар
            await session.execute(
                delete(cls.model).filter_by(id=product_id)
            )

            await session.commit()
            return product_id
