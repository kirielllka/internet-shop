from sqlalchemy import Column, Integer, String

from database import Base


class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    full_name = Column(String(100), nullable=True)
    phone_number = Column(String(20), nullable=False)



