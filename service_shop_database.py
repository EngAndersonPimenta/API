from flask import  Flask
from flask_sqlalchemy import SQLAlchemy
from database_structure import app

app.config['JSON_SORT_KEYS'] = False
app.config['SECRET_KEY'] = 'P0R7U6AL$2@2E'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///register.db'


db = SQLAlchemy(app)
db: SQLAlchemy

class Services(db.Model):
    __tablename__ = 'service'
    shop_name = db.Column(db.String)
    email = db.Column(db.String, primary_key=True)
    phone = db.Column(db.Integer)
    telegram_number = db.Column(db.Integer)
    address = db.Column(db.String)
    service_name = db.Column(db.String)
    service_description = db.Column(db.String)
    service_price = db.Column(db.Integer)
    professional = db.Column(db.String)
