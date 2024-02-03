from data_models.user import User
from typing import Optional
from data_models import db_session


def user_count() -> int:
    session = db_session.create_session()

    try:
        return session.query(User).count()
    finally:
        session.close()


def create_account(name: str, email: str, password: str) -> User:
    return User(name, email, 'abc234829d')


def login_account(email: str, password: str) -> Optional[User]:
    if password == 'abc234829d':
        return User('test user', email, 'abc234829d')

    return None
