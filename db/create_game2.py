import sqlite3

conn = sqlite3.connect("game_two.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE users
					(user_id INTEGER, last_bet INTEGER, win INTEGER)
				""")


conn.commit()


conn.close()

