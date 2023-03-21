from flask import Flask, jsonify, request
import client_registers
import shopName_registers
from flask_sqlalchemy import SQLAlchemy
from database_structure import Final_Client, Service_Shop, app, db

# Creating route to Final Client
# Actions (verbs) to Final Client Register
@app.router('/client_registers')
def get_register():
    registers = Final_Client.query.all()
    register_list = []
    for register in registers:
        register_current = {}
        register_current['id_register'] = register.id_register
        register_current['name'] = register.name
        register_current['email'] = register.email
        register_current['telegram_number'] = register.telegram_number
        register_list.append(register_current)
    return jsonify({'registers': register_list})

@app.route('/client_registers', methods=['POST'])
def create_client(name, email, telegram_number, telegram_id):
    data = request.get_json()
    client_registers.append(data)
    return jsonify({'Message': 'User created successfully.'})


@app.route('/client_registers/<int:telegram_id>', methods=['GET'])
def get_client(telegram_id):
    return jsonify(client_registers[telegram_id])


@app.route('/client_registers/<int:telegram_number>', methods=['PUT'])
def update_telegramNumber(name, email, telegram_number):
    result = request.get_json
    client_registers[telegram_number].update(result)
    return jsonify(client_registers[telegram_number]), 200


@app.route('/client_registers/<name>', methods=['PUT'])
def update_name(name, email, telegram_number):
    result = request.get_json
    client_registers[name].update(result)
    return jsonify(client_registers[name]), 200


@app.route('/client_registers/<email>', methods=['PUT'])
def update_email(name, email, telegram_number):
    result = request.get_json
    client_registers[email].update(result)
    return jsonify(client_registers[email]), 200


@app.route('/client_registers/<int:telegram_number>', methods=['DELETE'])
def delete_client(telegram_number):
    client = client_registers[telegram_number]
    del client_registers[telegram_number]
    return jsonify({'Message': 'User deleted successfully.'})

#===============================================================
# Creating route to Service Shop
# Actions (verbs) to Service Shop Register
@app.route('/shopName_registers')
def get_serviceShop():
    services = Service_Shop.query.all()
    services_list = []
    for service in services:
        service_current = {}
        service_current['shop_name'] = service.shop_name
        service_current['email'] = service.email
        service_current['phone'] = service.phone
        service_current['telegram_number'] = service.telegram_number
        service_current['address'] = service.address
        service_current['service_name'] = service.service_name
        service_current['service_description'] = service.service_description
        service_current['service_price'] = service.service_price
        service_current['professional'] = service.professional

# POST
@app.route('/shopName_registers', methods=['POST'])
def create_serviceShop(shop_name, email, phone, telegram_number, address, service_name, service_description, service_price, professional):
    data = request.get_json()
    shopName_registers.append(data)
    return jsonify({'Message': 'Service Shop created successfully.'})

# GET
@app.route('/shopName_registers/<shop_name>', methods=['GET'])
def get_shopName(shop_name):
    return jsonify(client_registers[shop_name])

@app.route('/shopName_registers/<email>', methods=['GET'])
def get_email(email):
    return jsonify(client_registers[email])

@app.route('/shopName_registers/<int:phone>', methods=['GET'])
def get_phone(phone):
    return jsonify(client_registers[phone])

@app.route('/shopName_registers/<int:telegram_number>', methods=['GET'])
def get_telegramNumber(telegram_number):
    return jsonify(client_registers[telegram_number])

@app.route('/shopName_registers/<address>', methods=['GET'])
def get_address(address):
    return jsonify(client_registers[address])

@app.route('/shopName_registers/<service_name>', methods=['GET'])
def get_serviceName(service_name):
    return jsonify(client_registers[service_name])

@app.route('/shopName_registers/<service_description>', methods=['GET'])
def get_serviceDescription(service_description):
    return jsonify(client_registers[service_description])

@app.route('/shopName_registers/<int:service_price>', methods=['GET'])
def get_servicePrice(service_price):
    return jsonify(client_registers[service_price])

@app.route('/shopName_registers/<professional>', methods=['GET'])
def get_professional(professional):
    return jsonify(client_registers[professional])

#PUT
@app.route('/shopName_registers/<shop_name>', methods=['PUT'])
def update_shopName(shop_name, email, phone, telegram_number, address, service_name, service_description, service_price, professional):
    result = request.get_json()
    shopName_registers[shop_name].update(result)
    return jsonify({'Message': 'Shop Name updated successfully.'}), 200

@app.route('/shopName_registers/<email>', methods=['PUT'])
def update_email(shop_name, email, phone, telegram_number, address, service_name, service_description, service_price, professional):
    result = request.get_json
    shopName_registers[email].update(result)
    return jsonify({'Message': 'Email updated successfully.'}), 200

@app.route('/shopName_registers/<int:phone>', methods=['PUT'])
def update_phone(shop_name, email, phone, telegram_number, address, service_name, service_description, service_price, professional):
    result = request.get_json
    shopName_registers[phone].update(result)
    return jsonify({'Message': 'Phone updated successfully.'}), 200

@app.route('/shopName_registers/<int:telegram_number>', methods=['PUT'])
def update_telegramNumber(shop_name, email, phone, telegram_number, address, service_name, service_description, service_price, professional):
    result = request.get_json
    shopName_registers[telegram_number].update(result)
    return jsonify({'Message': 'Telegram Number updated successfully.'}), 200

@app.route('/shopName_registers/<address>', methods=['PUT'])
def update_address(shop_name, email, phone, telegram_number, address, service_name, service_description, service_price, professional):
    result = request.get_json
    shopName_registers[address].update(result)
    return jsonify({'Message': 'Address updated successfully.'}), 200

@app.route('/shopName_registers/<service_name>', methods=['PUT'])
def update_serviceName(shop_name, email, phone, telegram_number, address, service_name, service_description, service_price, professional):
    result = request.get_json
    shopName_registers[service_name].update(result)
    return jsonify({'Message': 'Service Name updated successfully.'}), 200

@app.route('/shopName_registers/<service_description>', methods=['PUT'])
def update_serviceDescription(shop_name, email, phone, telegram_number, address, service_name, service_description, service_price, professional):
    result = request.get_json
    shopName_registers[service_description].update(result)
    return jsonify({'Message': 'Service Description updated successfully.'}), 200

@app.route('/shopName_registers/<int:service_price>', methods=['PUT'])
def update_servicePrice(shop_name, email, phone, telegram_number, address, service_name, service_description, service_price, professional):
    result = request.get_json
    shopName_registers[service_price].update(result)
    return jsonify({'Message': 'Service Price updated successfully.'}), 200

@app.route('/shopName_registers/<professional>', methods=['PUT'])
def update_professional(shop_name, email, phone, telegram_number, address, service_name, service_description, service_price, professional):
    result = request.get_json
    shopName_registers[professional].update(result)
    return jsonify({'Message': 'Professional updated successfully.'}), 200

# DELETE
@app.route('/shopName_registers/<int:telegram_number>', methods=['DELETE'])
def delete_serviceShop(telegram_number):
    serviceShop = client_registers[telegram_number]
    del shopName_registers[telegram_number]
    return jsonify({'Message': 'Service Shop deleted successfully.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    