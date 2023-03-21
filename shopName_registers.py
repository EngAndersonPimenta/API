import sqlite3

with sqlite3.connect('register.db') as connection:
    sql = connection.cursor()
    table_created = sql.execute('create table user(name txt, email txt, telegram_number integer, telegram_id intereger)')
    # sql.execute('insert into user (name, email, telegram_number, telegram_id) values ("Martim Pimenta", "martim@gmail.com", 935654876, 5583)') # Retirar 'values' e testar os inputs abaixo no 'values'.
    shop_name = input('Type the shop name: ')
    email = input('Type the shop e-mail: ')
    phone = int(input('Type the shop phone: '))
    telegram_number = int(input('Type the shop Telegram number: '))
    address = input('Type the shop address: ')
    service_name = input('Type the service name: ')
    service_description = input('Type the service description: ')
    service_price = int(input('Type the service price: '))
    telegram_id = int(input('Type your Telegram ID: '))
    sql.execute('insert into user values(?, ?, ?, ?, ?, ?, ?, ?, ?)', [shop_name, email, phone, telegram_number, address, service_name, service_description, service_price, telegram_id])

    connection.commit()