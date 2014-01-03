#!/usr/bin/env python

"""
This script creates all the models in the defined sql database
"""


import os
import argparse

from blibb.db import init_db, get_engine, Base

def main():
    parser = argparse.ArgumentParser(description='Create the data base for :blibb.')
    parser.add_argument('-u','--url', help='The database url to create', required=True)
    args = vars(parser.parse_args())

    BLIBB_db = args['url']
    engine = get_engine(blibb_db)
    init_db(engine, Base)


if __name__ == '__main__':
    main()
