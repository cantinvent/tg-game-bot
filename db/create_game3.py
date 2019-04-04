import sqlite3

conn = sqlite3.connect("game_three.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE users
					(user_id INTEGER, counter INTEGER, box1 INTEGER, box2 INTEGER, box3 INTEGER,
					box4 INTEGER, box5 INTEGER, box6 INTEGER, box7 INTEGER, box8 INTEGER, box9 INTEGER, 
					stars_counter INTEGER, last_bet INTEGER, win INTEGER)
				""")


conn.commit()


conn.close()

