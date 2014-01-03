# -*- coding: utf-8 -*-
"""Tests for the Collection model"""

import unittest

import sys
import os
from os.path import join, abspath, dirname
parentpath = abspath(join(dirname(__file__), '../../..'))
sys.path.append(parentpath)

from blibbapi.db import get_engine, init_db, get_db_session, Base
from blibbapi.models.blibb import Collection, Item


class TestCollectionModel(unittest.TestCase):

    def setUp(self):
        # self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        # test_sql = 'sqlite:///test_db.sql'
        test_sql = 'postgresql://postgres:postgres@192.168.33.10/test_db'
        self.engine = get_engine(test_sql)
        self.db = init_db(self.engine, Base)
        self.db_session = get_db_session(self.engine)

    def tearDown(self):
        self.db_session.remove()
        os.unlink('test_db.sql')

    def test_basic(self):
        col = Collection('First Collection', 'Ivan')
        self.db_session.add(col)
        self.db_session.commit()

        results = self.db_session.query(Collection).all()
        print str(results)

        self.assertEquals(len(results), 1)
        self.assertEquals(results[0].__repr__(), u'<Collection: First Collection, owner: Ivan>')
        self.assertEquals(results[0]._serialise(), {'name': 'First Collection', 'owner': 'Ivan'})



class TestItemModel(unittest.TestCase):

    def setUp(self):
        # self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        test_sql = 'sqlite:///test_db.sql'
        self.engine = get_engine(test_sql)
        self.db = init_db(self.engine, Base)
        self.db_session = get_db_session(self.engine)

    def tearDown(self):
        self.db_session.remove()
        os.unlink('test_db.sql')

    def test_basic(self):
        item = Item('First Item', 'Ivan')
        self.db_session.add(item)
        self.db_session.commit()

        results = self.db_session.query(Item).all()
        print str(results)

        self.assertEquals(len(results), 1)
        self.assertEquals(results[0].__repr__(), u'<Item: First Item, owner: Ivan>')
        self.assertEquals(results[0]._serialise(), {'name': 'First Item', 'owner': 'Ivan'})




