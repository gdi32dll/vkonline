import sqlite3

db_connector = sqlite3.connect('sqlite/vk_status.db')

cursor = db_connector.cursor()

for line in cursor.execute("SELECT * FROM users"):
	print line

db_connector.commit()

db_connector.close()