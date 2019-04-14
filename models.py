from flask_sqlalchemy import SQLAlchemy

from app import app
db = SQLAlchemy(app)


class device(db.Model):
    __tablename__ = "device"
    machine_id = db.Column('machine_id', db.String, primary_key=True)
    result = db.Column('result', db.String)
    prob = db.Column('prob', db.String)

    def __init__(self, machine_id, result, prob):
        self.machine_id = machine_id
        self.result = result
        self.prob = prob


# db.create_all()
