from sqlalchemy import Column, Integer, ForeignKey, Float, Date

from database import Base


class OrderHistory(Base):
    __tablename__ = "history"
    id = Column(Integer, primary_key=True)
    product = Column(ForeignKey("products.id"), nullable=False)
    date = Column(Date, nullable=False)
    quantity = Column(Integer, default=1, nullable=False)
    full_cost = Column(Float, nullable=False)
    client = Column(ForeignKey("clients.id"), nullable=False)
