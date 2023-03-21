from flask import  Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False
app.config['SECRET_KEY'] = 'P0R7U6AL$2@2E'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///register.db'


db = SQLAlchemy(app)
db: SQLAlchemy

class Final_Client(db.Model): # Register client
    __tablename__ = 'Final Client'
    name = db.Column(db.String)
    email = db.Column(db.String)
    telegram_number = db.Column(db.Integer, primary_key=True)
    Id_Telegram = db.Column(db.Integer, db.ForeignKey('telegram.id_telegram'))

class Id_Telegram(db.Model): # ID Telegram Chat Bot
    __tablename__ = 'ID Telegram'
    id_telegram = db.Column(db.Integer, primary_key=True)
    id_chat = db.Column(db.Integer)
    talking = db.relationship('Final_Client')

class Service_Shop(db.Model): # Service Shop
    __tablename__ = 'Service Shop'
    shop_name = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.Integer)
    telegram_number = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String)
    service_name = db.Column(db.String)
    service_description = db.Column(db.String)
    service_price = db.Column(db.Integer)
    professional = db.Column(db.String)

def start_database():
    db.drop_all()
    db.create_all()

    user_admin = Final_Client(name='Anderson Pimenta', email='andersonpimenta@email.com', password='123456', admin=True)
    db.session.add(user_admin)
    db.session.commit()

if __name__ == '__main__':
    start_database()