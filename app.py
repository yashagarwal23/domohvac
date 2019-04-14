from flask import Flask
from flask_socketio import SocketIO
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socket = SocketIO(app)

from routes import *

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

if __name__ == '__main__':
    socket.run(app)