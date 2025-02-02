from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship

from database import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    detail = Column(String, index=True)
    short = Column(String, index=True)
    genre = Column(String, index=True)
    year = Column(Integer, index=True)
    is_published = Column(Boolean, index=True)
    
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    stu_id = Column(Integer, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    bod = Column(String, index=True)
    sex = Column(String, index=True)
    age = Column(Integer, index=True)

class Menu(Base):
    __tablename__ = 'menus'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    quantity = Column(Integer, index=True)
    note = Column(String, index=True)
    price = Column(Integer, index=True)
    detail = Column(String, index=True)
    
class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    quantity = Column(Integer, index=True)
    note = Column(String, index=True)
    price = Column(Integer, index=True)