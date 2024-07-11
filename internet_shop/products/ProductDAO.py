from sqlalchemy import select

from Base.BaseDAO import BaseDAO
from .models import Products
from database import session_maker

class ProductsDAO(BaseDAO):
    @classmethod
    def find_by_name(cls, product_name: str) -> list:
        with session_maker() as session:
            query = select(Products).where(Products.\
                                             product_name.ilike(f"%{product_name}%"))
            result = session.execute(query)
            return [row for row in result.scalars()]

