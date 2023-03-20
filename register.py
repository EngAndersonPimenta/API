from flask import Flask, jsonify, request
import registers_data
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False
app.config['SECRET_KEY'] = 'P0R7U6AL$2@2!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///register.db'


db = SQLAlchemy(app)
db: SQLAlchemy

class Register(db.Model):
    __tablename__ = 'registers'
    name = db.Column(db.String, primary_key=True)
    email = db.Column(db.String)
    telegram_number = db.Column(db.Integer)
    Id_Telegram = db.Column(db.Integer, db.ForeignKey('telegram.id_telegram'))

class Id_Telegram(db.Model):
    __tablename__ = 'telegram'
    id_telegram = db.Column(db.Integer, primary_key=True)
    id_chat = db.Column(db.Integer)
    talking = db.relationship('Register')

db.drop_all()
db.create_all()

user_admin = Register(name='Anderson Pimenta', email='andersonpimenta@email.com', password='123456', admin=True)
db.session.add(user_admin)
db.session.commit()

@app.route('/registers_data', methods=['POST'])
def create_client(name, email, telegram_number, telegram_id):
    data = request.get_json()
    registers_data.append(data)
    return jsonify({'Message': 'User created successfully.'})


@app.route('/registers_data/<int:telegram_id>', methods=['GET'])
def get_user(telegram_id):
    return jsonify(registers_data[telegram_id])


@app.route('/registers_data/<int:telegram_number>', methods=['PUT'])
def change_telegram_number(name, email, telegram_number):
    result = request.get_json
    registers_data[telegram_number].update(result)
    return jsonify(registers_data[telegram_number]), 200


@app.route('/registers_data/<name>', methods=['PUT'])
def change_name(name, email, telegram_number):
    result = request.get_json
    registers_data[name].update(result)
    return jsonify(registers_data[name]), 200


@app.route('/registers_data/<email>', methods=['PUT'])
def change_email(name, email, telegram_number):
    result = request.get_json
    registers_data[email].update(result)
    return jsonify(registers_data[email]), 200


@app.route('/registers_data/<int:telegram_number>', methods=['DELETE'])
def delete_user(telegram_number):
    client = registers_data[telegram_number]
    del registers_data[telegram_number]
    return jsonify({'Message': 'User deleted successfully.'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
