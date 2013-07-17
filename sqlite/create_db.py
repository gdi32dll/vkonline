import sqlite3

db_connector = sqlite3.connect('vk_status.db')

cursor = db_connector.cursor()

cursor.execute('CREATE TABLE users (username TEXT, time TEXT, status INTEGER)')


db_connector.commit()

db_connector.close()