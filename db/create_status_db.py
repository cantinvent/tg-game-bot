import sqlite3

conn = sqlite3.connect("status_base.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE users
					(user_id INTEGER, status_id INTEGER)
				""")


conn.commit()


conn.close()

