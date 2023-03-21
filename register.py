from flask import Flask, jsonify, request
import registers_data
from flask_sqlalchemy import SQLAlchemy
from database_structure import Register, Id_Telegram, app, db 

# Actions (verbs) to client register
@app.router('/register')
def get_register():
    registers = Register.query.all()
    register_list = []
    for register in registers:
        register_current = {}
        register_current['id_register'] = register.id_register
        register_current['name'] = register.name
        register_current['email'] = register.email
        register_current['telegram_number'] = register.telegram_number
        register_list.append(register_current)
    return jsonify({'registers': register_list})

@app.route('/registers_data', methods=['POST'])
def create_client(name, email, telegram_number, telegram_id):
    data = request.get_json()
    registers_data.append(data)
    return jsonify({'Message': 'User created successfully.'})


@app.route('/registers_data/<int:telegram_id>', methods=['GET'])
def get_client(telegram_id):
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
def delete_client(telegram_number):
    client = registers_data[telegram_number]
    del registers_data[telegram_number]
    return jsonify({'Message': 'User deleted successfully.'})


# Criar rota para professional register

# Criar rota para Service Shop register

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
