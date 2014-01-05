# -*- coding: utf-8 -*-
"""Tests for the Item model"""

import unittest

import sys
import os
from os.path import join, abspath, dirname
parentpath = abspath(join(dirname(__file__), '../../..'))
sys.path.append(parentpath)

from blibbapi.db import get_engine, init_db, get_db_session, Base
from blibbapi.models.blibb import Item

class TestItemModel(unittest.TestCase):

    def setUp(self):
        test_sql = 'postgresql://postgres:postgres@localhost/test_db'
        self.engine = get_engine(test_sql)
        self.db = init_db(self.engine, Base)
        self.db_session = get_db_session(self.engine)

    def tearDown(self):
        self.db_session.execute("truncate blibb_item")
        self.db_session.commit()
        self.db_session.remove()


    def test_basic(self):
        user_id = 12
        parent_id = 14
        item = Item('First Item', user_id, parent_id)
        self.db_session.add(item)
        self.db_session.commit()

        results = self.db_session.query(Item).all()
        print str(results)

        self.assertEquals(len(results), 1)
        self.assertEquals(results[0].__repr__(), u'<Item: First Item, owner: %s>' % user_id)
        self.assertEquals(results[0]._serialise(), {'name': 'First Item', 'owner': '%s' % user_id})
