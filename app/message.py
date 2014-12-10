__author__ = 'gauri'

from flask import Flask
from flask import make_response
from flask import jsonify
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/test'
db = SQLAlchemy(app)

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(100))

db.create_all()

@app.route('/')
def index():
    print "inside index()"
    resp = make_response()
    data = {'message': "Hi!"}
    resp = jsonify(data)
    return resp

@app.route('/message', methods=['POST'])
def message():
    print "inside message()"
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

@app.route('/messages/<id>', methods=['GET'])
def messages(id):
    print "inside messages()"
    m = Messages.query.get(id)
    print m.message
    resp = make_response()
    data = {'message': m.message}
    resp = jsonify(data)
    return resp

app.run(debug=True)
