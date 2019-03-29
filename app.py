from flask import Flask, render_template, request, jsonify, session

from flask_sqlalchemy import SQLAlchemy
import json
import MySQLdb
from json import dumps
app=Flask(__name__)


app.debug = True
# app.config['SQLALCHEMY_ECHO'] = True
app.secret_key = "some_secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/mydb'
# mysql://scott:tiger@localhost/mydatabase
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(180))
    last_name = db.Column(db.String(80))
    roll_number = db.Column(db.String(10))
    mobile_number = db.Column(db.String(80))
    
    def __init__(self, first_name, last_name, roll_number, mobile_number):
        self.first_name = name
        self.last_name = first_name
        self.roll_number = roll_number
        self.mobile_number = mobile_number

    def __repr__(self):
        return str(self.first_name)



@app.route('/')
def index():
	count=db.session.query(Users.id).all()
	return render_template('index.html', users_count=count)

@app.route('/userdetails/<id_user>',methods=['GET'])
def userDetails(id_user):
	users=Users.query.filter_by(id=id_user).all()
	data = {}
	data['first_name'] = users[0].first_name
	data['last_name'] = users[0].last_name
	data['roll_number'] = users[0].roll_number
	data['mobile_number'] = users[0].mobile_number
	data = json.dumps(data);
	return data

if __name__=='__main__':
	db.create_all()
	app.run(debug=True)