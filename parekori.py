import sqlite3
import flask
from contextlib import closing
from main_page import get_main_page_routes

DEBUG = True
DATABASE = './parekori.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'development key'

app = flask.Flask(__name__)
app.config.from_object(__name__)

def connect():
    return sqlite3.connect(app.config['DATABASE'])

def initialize_database():
    conn = None
    try:
        conn = connect()
        with conn:
            with app.open_resource('schema.sql', mode='r') as f:
                with closing(conn.cursor()) as cursor:
                    cursor.executescript(f.read())
    finally:
        if conn is not None:
            conn.close()

def get_connection():
    conn = getattr(flask.g, '_connection', None)
    if conn is None:
        conn = connect()
        flask.g._connection = conn
    return conn

def close_connection():
    conn = getattr(flask.g, '_connection', None)
    if conn is not None:
        conn.close()

@app.teardown_appcontext
def close_connection_on_teardown(exception):
    close_connection()

def execute(statement, args=()):
    with get_connection() as conn:
        with closing(conn.execute(statement, args)) as cursor:
            return cursor.fetchall()

app.register_blueprint(get_main_page_routes(execute))

if __name__ == '__main__':
    initialize_database()
    app.run()
