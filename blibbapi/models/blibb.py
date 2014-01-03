
from sqlalchemy import Column, Integer, String, Float

from blibbapi.db import Base

class Collection(Base):

    __tablename__ = 'blibb_collection'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True)
    owner = Column(String(200))

    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    def __repr__(self):
        return '<Collection: %s, owner: %s>' % (self.name, self.owner)

    def _serialise(self):
        return {
                'name': self.name,
                'owner': self.owner
                }


class Item(Base):

    __tablename__ = 'blibb_item'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True)
    owner = Column(String(200))

    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    def __repr__(self):
        return '<Item: %s, owner: %s>' % (self.name, self.owner)

    def _serialise(self):
        return {
                'name': self.name,
                'owner': self.owner
                }
