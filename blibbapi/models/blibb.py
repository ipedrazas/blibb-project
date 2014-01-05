
from sqlalchemy import Column, Integer, String, Float, ForeignKey

from blibbapi.db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name=%s, fullname=%s, password=%s)>" % (
            self.name, self.fullname, self.password)


class Collection(Base):

    __tablename__ = 'blibb_collection'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True)
    owner = Column(Integer, ForeignKey('users.id'))

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
    owner = Column(Integer, ForeignKey('users.id'))
    parent = Column(Integer, ForeignKey('blibb_collection.id'))

    def __init__(self, name, owner, parent):
        self.name = name
        self.owner = owner
        self.parent = parent

    def __repr__(self):
        return '<Item: %s, owner: %s, parent: %s>' % (self.name, self.owner, self.parent)

    def _serialise(self):
        return {
                'name': self.name,
                'owner': self.owner,
                'parent': self.parent
                }
