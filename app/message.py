__author__ = 'gauri'

from flask import Flask
from flask import make_response
from flask import jsonify
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/test'
db = SQLAlchemy(app)

#message model
class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(100))

db.create_all()

#controller
@app.route('/')
def index():
    print "inside index()"
    resp = make_response()
    data = {'message': "Hi!"}
    resp = jsonify(data)
    return resp

#messages controller

@app.route('/messages/<id>', methods=['GET'])
def get_message_by_id(id):
    m = Messages.query.get(id)
    print m.message
    data = {'message': m.message}
    resp = make_response()
    resp = jsonify(data)
    return resp

@app.route('/messages', methods=['GET'])
def get_all_messages():
    messageList = Messages.query.all()
    list = []
    for msg in messageList:
        list.append({msg.id:msg.message})
    resp = make_response()
    resp = jsonify(msgs = list)
    return resp

@app.route('/messages', methods=['POST'])
def message():
    print request.headers
    print request.data
    m = Messages()
    m.message = request.json.get('message')
    db.session.add(m)
    db.session.commit()
    resp = make_response()
    data = {'message': "Success!"}
    resp = jsonify(data)
    return resp

@app.route('/messages/<id>', methods=['PUT'])
def edit_messages(id):
    m = Messages.query.get(id)
    print request.json
    m.message = request.json.get('message')
    db.session.commit()
    resp = make_response()
    return resp

app.run(debug=True)