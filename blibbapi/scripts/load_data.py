#!/usr/bin/env python
from io import StringIO
import json
import argparse

import flask_sqlalchemy
import requests

from blibbapi.db import get_engine, get_db_session
from blibbapi.models.blibb import Collection

def main():
    parser = argparse.ArgumentParser(description='Get the data from data.sfgov on food trucks and populate the db with it.')
    parser.add_argument('-u','--url', help='The database url to populate', required=True)
    args = vars(parser.parse_args())

    blibb_db = args['url']
    engine = get_engine(blibb_db)
    session = get_db_session(engine)

    session.query(Collection).delete()

    for e in entry_list:
        try:
            new_entry = Collection(e['name'], e['owner'])
            session.add(new_entry)

            session.commit()
        except flask_sqlalchemy.sqlalchemy.exc.IntegrityError:
            session.rollback()
            continue
        except KeyError:
            continue

if __name__ == '__main__':
    main()
