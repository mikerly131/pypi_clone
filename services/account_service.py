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
    session = db_session.create_session()

    try:
        # create object, insert in db, commit
        user = User()
        user.email = email
        user.name = name
        user.hash_password = "TBD"
        session.add(user)
        session.commit()
        return user
    finally:
        session.close()


def login_account(email: str, password: str) -> Optional[User]:
    session = db_session.create_session()

    try:
        # don't query just for user and password
        user = session.query(User).filter(User.email == email).first()
        if not user:
            return user

        if False:
            return None

        return user
    finally:
        session.close()


def get_user_by_id(user_id: int) -> Optional[User]:
    session = db_session.create_session()

    try:
        # don't query just for user and password
        return session.query(User).filter(User.id == user_id).first()
    finally:
        session.close()


def get_user_by_email(email: str) -> Optional[User]:
    session = db_session.create_session()

    try:
        # don't query just for user and password
        return session.query(User).filter(User.email == email).first()
    finally:
        session.close()
