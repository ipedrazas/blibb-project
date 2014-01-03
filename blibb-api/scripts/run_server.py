import argparse


from blibb import my_app
from blibb.app import define_urls

def run_server():
    parser = argparse.ArgumentParser(description='Create the data base for :blibb.')
    parser.add_argument('-u','--url', help='The database url to create', required=True)
    args = vars(parser.parse_args())

    blibb_db = args['url']

    from blibb.db import get_engine, get_db_session
    engine = get_engine(food_truck_db)
    my_app.config['DB_SESSION'] = get_db_session(engine)
    define_urls(my_app)
    my_app.debug = True
    return my_app

def dev_server():
    app = run_server()
    app.run()

if __name__ == '__main__':
    dev_server()
