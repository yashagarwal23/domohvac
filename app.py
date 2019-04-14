from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socket = SocketIO(app)

from routes import *

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://yash:Hisar*123@localhost/device'

# from models import db
# db.create_all()

if __name__ == '__main__':
    socket.run(app)