from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, BigInteger, Float, Boolean

from config import db_location


engine = create_async_engine(db_location, echo=False)

async_session = async_sessionmaker(bind=engine)



class Base(AsyncAttrs, DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(BigInteger(), nullable=False, primary_key=True)
    user_name: Mapped[str] = mapped_column(String(150), nullable=True)
    chat_id: Mapped[int] = mapped_column(BigInteger(), nullable=False)
    full_name: Mapped[str] = mapped_column(String(150), nullable=True)
    phone_number: Mapped[int] = mapped_column(Integer(), nullable=True)
    email: Mapped[str] = mapped_column(String(150), nullable=True)
    date_registration: Mapped[str] = mapped_column(String(150))
    language: Mapped[str] = mapped_column(String(4), nullable=True)
    

class UserCategorys(Base):
    __tablename__ = 'categorys'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger(), nullable=False)
    category: Mapped[str] = mapped_column(String(150), nullable=False)




async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


