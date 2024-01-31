from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
import pymysql
pymysql.install_as_MySQLdb()

app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['FLASK_ENV'] = 'development'
app.config['SECRET_KEY'] = 'ItShouldBeALongStringOfRandomCharacters'
app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql://root:Welcome@123localhost:3306/new_device_mgmt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class DeviceCategory(db.Model):
    id = db.Column(db.integer, primary_key=True)
    category_name = db.Column(db.String(128))
    devices = db.relationship('Device', backref='devicecategory', lazy=True)

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String(128))
    device_description = db.Column(db.String(512))
    inventory = db.Column(db.Integer)
    device_category = db.Column(db.Integer, db.ForeignKey('device_category.id'), nullable=False)

    def __str__(self):
        return f"{self.device_name} - {self.inventory} in stock at present"

db.create_all()


# pip install pymysql

import pandas as pd

@app.route('/')
def hello():
    return "<h1>Welcome to Python_graded Project 3</h1>"

@app.route("/get_data")
def getdata():
    return "Your data"

if __name__ == "__main__":
    app.run()