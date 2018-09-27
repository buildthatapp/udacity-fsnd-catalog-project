from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'name'        :  self.name,
            'id'          :  self.id,
            }

class Item(Base):
    __tablename__ = 'item'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    price = Column(String(10))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)

    @property
    def serialize(self):
         """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'description'         : self.description,
           'id'         : self.id,
           'price'         : self.price,
       }

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    first_name = Column(String(20), nullable = False)
    last_name = Column(String(30), nullable = False)
    email = Column(String(30), nullable = False)
    password = Column(String(20), nullable = False)
    phone_number = Column(String(10), nullable = True)


engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)
    
