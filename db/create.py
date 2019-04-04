import sqlite3

conn = sqlite3.connect("base.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE users
					(user_id INTEGER, user_name VARCHAR, first_name VARCHAR, balance INTEGER, 
					stat_one INTEGER, stat_two INTEGER, stat_three INTEGER, lt_id INTEGER)
				""")


conn.commit()


conn.close()

