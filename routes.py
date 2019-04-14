from utils import prob_failure, load_model
from flask import jsonify, request
from app import app, socket
from models import db, device
import numpy


@app.route('create_db')
def create_db():
    from models import db
    db.create_all()


@app.route("/")
def index():
    return "Domovoy Homepage"


@app.route('/put', methods=['GET', 'POST'])
def getDeviceStats():
    machine_id = request.form['machine_id']
    # machine_inputs = data['machine_inputs']
    # model = load_model()
    # failure_prob = prob_failure(model, machine_inputs)
    failure_prob = numpy.random.random()
    # print(failure_prob)

    device_list = device.query.filter_by(machine_id = machine_id).first()
    # print("djbjdb", device_list)
    if device_list:
        device_list.prob = failure_prob
        if failure_prob >= 0.6 :
            device_list.result = "NOT OK"
        else:
            device_list.result = "OK"
    else :
        new_device = device(machine_id, "OK", failure_prob)
        print(new_device)
        if failure_prob >= 0.6:
            new_device.result = "NOT_OK"
            db.session.add(new_device)

    db.session.commit()
    return "success"


@app.route("/getresult")
def getresult():
    return jsonify({
        "result" : list(map(lambda x : {
            "machineID":x.machine_id,
            "result":x.result,
            "probability":x.prob
        },device.query.all()))
    })


