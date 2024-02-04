from data_models.user import User
from typing import Optional
from data_models import db_session
from passlib.handlers.sha2_crypt import sha512_crypt as crypto
from sqlalchemy import select, func


# sqlalchemy 2.0 with async sessions
async def user_count() -> int:
    async with db_session.create_async_session() as session:
        query = select(func.count(User.id))
        # returns a tuple, need to access with .scalar()
        results = await session.execute(query)
        return results.scalar()

# # sqlalchemy 1.3 with sync session
# def user_count() -> int:
#     session = db_session.create_session()
#
#     try:
#         return session.query(User).count()
#     finally:
#         session.close()


async def create_account(name: str, email: str, password: str) -> User:
    user = User()
    user.email = email
    user.name = name
    user.hash_password = crypto.hash(password, rounds=113_249)

    async with db_session.create_async_session() as session:
        session.add(user)
        await session.commit()

    return user


async def login_account(email: str, password: str) -> Optional[User]:
    async with db_session.create_async_session() as session:
        query = select(User).filter(User.email == email)
        result = await session.execute(query)
        user = result.scalar_one_or_none()

        if not user:
            return user

        if not crypto.verify(password, user.hash_password):
            return None

        return user


async def get_user_by_id(user_id: int) -> Optional[User]:
    async with db_session.create_async_session() as session:
        query = select(User).filter(User.id == user_id)
        # returns a tuple, need to access with .scalar()
        result = await session.execute(query)
        return result.scalar_one_or_none()


async def get_user_by_email(email: str) -> Optional[User]:
    async with db_session.create_async_session() as session:
        query = select(User).filter(User.email == email)
        # returns a tuple, need to access with .scalar()
        result = await session.execute(query)
        return result.scalar_one_or_none()

