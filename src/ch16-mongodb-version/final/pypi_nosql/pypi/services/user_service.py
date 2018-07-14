from typing import Optional

from pypi import DbSession
from pypi.nosql.users import User
from passlib.handlers.sha2_crypt import sha512_crypt


def user_count() -> int:
    return User.objects().count()


def create_user(email: str, name: str, password: str) -> User:
    user = User()
    user.name = name
    user.email = email.lower().strip()
    user.hashed_password = hash_text(password)

    user.save()

    return user


def hash_text(text: str) -> str:
    hashed_text = sha512_crypt.encrypt(text, rounds=150000)
    return hashed_text


def verify_hash(hashed_text: str, plain_text: str) -> bool:
    return sha512_crypt.verify(plain_text, hashed_text)


def login_user(email: str, password: str) -> Optional[User]:
    if not email:
        return None

    user = find_user_by_email(email)
    if not user:
        return None

    if not verify_hash(user.hashed_password, password):
        return None

    return user


def find_user_by_id(user_id: int) -> Optional[User]:
    return User.objects(id=user_id).first()


def find_user_by_email(email: str) -> Optional[User]:
    if not email:
        return None

    email = email.lower().strip()

    return User.objects(email=email).first()
