from sqlalchemy import select

from Base.BaseDAO import BaseDAO
from .models import Roles
from database import session_maker


class RolesDAO(BaseDAO):
    @classmethod
    def find_by_name(cls, role_name: str) -> list:
        with session_maker() as session:
            query = select(Roles).where(Roles.\
                                             role_name.ilike(f"%{role_name}%"))
            result = session.execute(query)
            return [row for row in result.scalars()]