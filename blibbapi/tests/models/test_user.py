# -*- coding: utf-8 -*-
"""Tests for the User model"""

import unittest

import sys
import os
from os.path import join, abspath, dirname
parentpath = abspath(join(dirname(__file__), '../../..'))
sys.path.append(parentpath)

from blibbapi.db import get_engine, init_db, get_db_session, Base
from blibbapi.models.blibb import User


class TestUserModel(unittest.TestCase):
    def cleanup(self):
        self.db_session.execute("truncate users cascade")
        self.db_session.commit()

    def setUp(self):
        test_sql = 'postgresql://postgres:postgres@localhost/test_db'
        self.engine = get_engine(test_sql)
        self.db = init_db(self.engine, Base)
        self.db_session = get_db_session(self.engine)
        self.cleanup()

    def tearDown(self):
        self.cleanup()
        self.db_session.remove()

    def test_basic(self):
        user = User(name='Ivan', fullname='Ivan Pedrazas', password='mipassword')
        self.db_session.add(user)
        self.db_session.commit()

        results = self.db_session.query(User).all()
        print str(results)

        self.assertEquals(len(results), 1)
        self.assertEquals(results[0].__repr__(), u'<User(name=Ivan, fullname=Ivan Pedrazas, password=mipassword)>')
