from flask import Flask, jsonify, request
import users_data



app = Flask(__name__)

app.config['SECRET_KEY'] = 'segredo2030'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

#db = SQLAlchemy(app)
#db: SQLAlchemy

@app.route('/users_data', methods=['POST'])
def create_client(name, email, telegram_number, telegram_id):
    data = request.get_json()
    users_data.append(data)
    return jsonify({'Message': 'User created successfully.'})


@app.route('/users_data/<int:telegram_id>', methods=['GET'])
def get_user(telegram_id):
    return jsonify(users_data[telegram_id])


@app.route('/users_data/<int:telegram_number>', methods=['PUT'])
def change_telegram_number(name, email, telegram_number):
    result = request.get_json
    users_data[telegram_number].update(result)
    return jsonify(users_data[telegram_number]), 200


@app.route('/users_data/<name>', methods=['PUT'])
def change_name(name, email, telegram_number):
    result = request.get_json
    users_data[name].update(result)
    return jsonify(users_data[name]), 200


@app.route('/users_data/<email>', methods=['PUT'])
def change_email(name, email, telegram_number):
    result = request.get_json
    users_data[email].update(result)
    return jsonify(users_data[email]), 200


@app.route('/users_data/<int:telegram_number>', methods=['DELETE'])
def delete_user(telegram_number):
    client = users_data[telegram_number]
    del users_data[telegram_number]
    return jsonify({'Message': 'User deleted successfully.'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)