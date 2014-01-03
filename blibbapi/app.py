"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This flask app exposes some restful api endpoints for :blibb

"""

from flask import render_template, send_from_directory

from blibbapi import my_app


@my_app.teardown_appcontext
def shutdown_session(exception=None):
    if 'DB_SESSION' in my_app.config:
        my_app.config['DB_SESSION'].remove()


@my_app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

@my_app.route('/')
def static_from_root():
    return send_from_directory(my_app.static_folder, 'index.html')

