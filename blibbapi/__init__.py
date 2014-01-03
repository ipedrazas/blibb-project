# -*- coding: utf-8 -*-
"""
This package contains a :blibb flask app RESTFul api

"""
# pylint: disable=C
from flask import Flask

my_app = Flask(__name__, static_folder='static', static_url_path='',
               template_folder='templates')
