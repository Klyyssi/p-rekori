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

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

if __name__ == '__main__':
    init_db()
    app.run()
