from typing import Optional

from pypi import DbSession
from pypi.data.users import User
from passlib.handlers.sha2_crypt import sha512_crypt


def user_count() -> int:
    session = DbSession.factory()
    return session.query(User).count()


def create_user(email: str, name: str, password: str) -> User:
    user = User()
    user.name = name
    user.email = email.lower().strip()
    user.hashed_password = hash_text(password)

    session = DbSession.factory()
    session.add(user)
    session.commit()

    return user


def hash_text(text: str) -> str:
    hashed_text = sha512_crypt.encrypt(text, rounds=150000)
    return hashed_text


def verify_hash(hashed_text: str, plain_text: str) -> bool:
    return sha512_crypt.verify(plain_text, hashed_text)


def login_user(email: str, password: str) -> Optional[User]:
    if not email:
        return None

    email = email.lower().strip()

    session = DbSession.factory()
    user = session.query(User).filter(User.email == email).one()
    if not user:
        return None

    if not verify_hash(user.hashed_password, password):
        return None

    return user
