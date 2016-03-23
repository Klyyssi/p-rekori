import sqlite3
import flask

DEBUG = True
DATABASE = './parekori.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'development key'

app = flask.Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
    app.run()
