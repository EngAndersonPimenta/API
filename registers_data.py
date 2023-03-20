import sqlite3

with sqlite3.connect('register.db') as connection:
    sql = connection.cursor()
    sql.execute('create table user(name txt, email txt, telegram_number integer, telegram_id intereger)')
    sql.execute('insert into user (name, email, telegram_number, telegram_id) values ("Martim Pimenta", "martim@gmail.com", 935654876, 5583)')
    name = input('Type your name: ')
    email = input('Type your e-mail: ')
    telegram_number = int(input('Type your Telegram number: '))
    telegram_id = int(input('Type your Telegram ID: '))
    sql.execute('insert into user values(?, ?, ?, ?)',[name, email, telegram_number, telegram_id])

    connection.commit()