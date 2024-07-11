from sqlalchemy import Column, Integer, String, ForeignKey

from database import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(20), nullable=False)
    hashed_password = Column(String(50), nullable=False)
    role = Column(Integer, ForeignKey('roles.id'), nullable=True)


