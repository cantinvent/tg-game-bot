import sqlite3

conn = sqlite3.connect("trans_id.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE users
					(trans_id INTEGER)
				""")


conn.commit()


conn.close()

