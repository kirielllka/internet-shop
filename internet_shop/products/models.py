from sqlalchemy import Column, Integer, String, ForeignKey, Text, Float

from database import Base


class Products(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    product_name = Column(String(200), nullable=False)
    category = Column(ForeignKey("categories.id"), nullable=False, default=1)
    description = Column(Text)
    cost = Column(Float)
    count_of_sells = Column(Integer, default=0, nullable=False)
    discount = Column(Float, default=0.0, nullable=False)




