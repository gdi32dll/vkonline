import sqlite3

db_connector = sqlite3.connect('example.db')

cursor = db_connector.cursor()

cursor.execute("INSERT INTO users VALUES (1,'Johan','Moscow_1')")

db_connector.commit()

db_connector.close()