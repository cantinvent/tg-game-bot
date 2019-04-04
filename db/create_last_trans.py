import sqlite3

conn = sqlite3.connect("last_trans.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE users
					(user_id INTEGER, phone_number VARCHAR, amount INTEGER)
				""")


conn.commit()


conn.close()

