from database import session_maker
from .models import Users
from Base.BaseDAO import BaseDAO
from sqlalchemy import select
class UserDAO(BaseDAO):

    @classmethod
    def find_by_email(cls, email:str)->list:
        with session_maker() as session:
            query = select(Users).where(Users.email.ilike(f"%{email}%"))
            result = session.execute(query)
            return [row for row in result.scalars()]