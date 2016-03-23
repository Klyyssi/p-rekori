import sqlite3
import flask
from contextlib import closing

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


if __name__ == '__main__':
    initialize_database()
    app.run()
