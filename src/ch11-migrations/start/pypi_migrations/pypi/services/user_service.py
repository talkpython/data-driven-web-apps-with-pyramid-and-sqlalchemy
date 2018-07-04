from pypi import DbSession
from pypi.data.users import User


def user_count() -> int:
    session = DbSession.factory()
    return session.query(User).count()
