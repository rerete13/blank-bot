from sqlalchemy.future import select
from bot.db.models import UserConnections, async_session

async def get_connection_by_id(connection_id: int):
    async with async_session() as session:
        result = await session.execute(select(UserConnections).where(UserConnections.id == connection_id))
        connection = result.scalars().first()
        return connection

async def get_connections_by_user_id(user_id: int):
    async with async_session() as session:
        result = await session.execute(select(UserConnections).where(UserConnections.user_id == user_id))
        connections = result.scalars().all()
        return connections

async def get_connection_by_user_and_partner(user_id: int, partner_id: int):
    async with async_session() as session:
        result = await session.execute(
            select(UserConnections).where(UserConnections.user_id == user_id, UserConnections.partner_id == partner_id)
        )
        connection = result.scalars().first()
        return connection


async def add_connection(user_id: int, partner_id: int, partner_full_name:str, status: bool, time_start: str, time_end: str = None):
    async with async_session() as session:
        new_connection = UserConnections(
            user_id=user_id,
            partner_id=partner_id,
            partner_full_name=partner_full_name,
            status=status,
            time_start=time_start,
            time_end=time_end
        )
        session.add(new_connection)
        await session.commit()
        return new_connection

async def delete_connection_by_id(connection_id: int):
    async with async_session() as session:
        result = await session.execute(select(UserConnections).where(UserConnections.id == connection_id))
        connection_to_delete = result.scalars().first()
        if connection_to_delete:
            await session.delete(connection_to_delete)
            await session.commit()
            return True
        return False

from sqlalchemy.future import select

async def update_connection_by_user_id_and_partner_id(user_id: int, partner_id: int, status: bool = None, time_start: str = None, time_end: str = None):
    async with async_session() as session:

        result = await session.execute(
            select(UserConnections)
            .where(UserConnections.user_id == user_id, UserConnections.partner_id == partner_id)
        )
        connection_to_update = result.scalar_one_or_none()

        if connection_to_update:
            if status is not None:
                connection_to_update.status = status
            if time_start is not None:
                connection_to_update.time_start = time_start
            if time_end is not None:
                connection_to_update.time_end = time_end

            await session.commit()
            return connection_to_update
        return None

