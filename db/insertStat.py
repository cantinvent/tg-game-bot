import sqlite3

id = 10078
conn = sqlite3.connect("trans_id.db")
cursor = conn.cursor()
cursor.execute("INSERT INTO users (trans_id)"
                   " VALUES (?)", (
                    id,))
conn.commit()
conn.close()