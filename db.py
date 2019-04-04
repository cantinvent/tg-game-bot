import sqlite3

# status
# 0 - base mode
# 1 - enter amount
# 2 - enter number

def insert_to_db(message):
    id = message.chat.id
    user_name = message.chat.username
    first_name = message.chat.first_name
    bal = 0
    stat_one = 0
    stat_two = 0
    stat_three = 0
    lt_id = 0

    conn = sqlite3.connect("db/base.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (user_id, user_name, first_name, balance, stat_one, stat_two, stat_three, lt_id)"
                   " VALUES (?,?,?,?,?,?,?,?)", (
                    id, user_name, first_name, bal, stat_one, stat_two, stat_three, lt_id))
    conn.commit()
    conn.close()
    insert_to_status_db(message)
    insert_to_last_trans_db(message)
    insert_to_game2_db(message)
    insert_to_game3_db(message)

##########
def insert_to_game2_db(message):
    id = message.chat.id
    conn = sqlite3.connect("db/game_two.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (user_id, last_bet, win) VALUES (?, ?, ?)",
                   (id, 0, 0))
    conn.commit()
    conn.close()

##########
def update_last_bet_game2_db(id, bet):
   # id = message.chat.id
    conn = sqlite3.connect("db/game_two.db")
    cursor = conn.cursor()
    sql = "UPDATE users SET last_bet=:BET WHERE user_id=:ID"
    task = {'BET': bet, 'ID': id}
    cursor.execute(sql, task)
    conn.commit()
    conn.close()

##########
def update_win_game2_db(message, amount):
    id = message.chat.id
    conn = sqlite3.connect("db/game_two.db")
    cursor = conn.cursor()
    sql = "UPDATE users SET win=:WIN WHERE user_id=:ID"
    task = {'WIN': amount, 'ID': id}
    cursor.execute(sql, task)
    conn.commit()
    conn.close()

##########
def get_last_bet_game2_db(id):
   # id = message.chat.id
    conn = sqlite3.connect("db/game_two.db")
    cursor = conn.cursor()
    cursor.execute("SELECT last_bet FROM users WHERE user_id = ?", (id,))
    last_bet = cursor.fetchall()[0][0]
    conn.close()
    return last_bet

##########
def reset_last_bet_game2_db(id):
   # id = message.chat.id
    conn = sqlite3.connect("db/game_two.db")
    cursor = conn.cursor()
    sql = "UPDATE users SET last_bet=:BET WHERE user_id=:ID"
    task = {'BET': 0, 'ID': id}
    cursor.execute(sql, task)
    conn.commit()
    conn.close()

##########
def insert_to_game3_db(message):
    id = message.chat.id
    conn = sqlite3.connect("db/game_three.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (user_id, counter, box1, box2, box3, box4, box5,"
                   "box6, box7, box8, box9, stars_counter, last_bet, win) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (id, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    conn.commit()
    conn.close()
##########
def get_stars_counter_game3_db(id):
    conn = sqlite3.connect("db/game_three.db")
    cursor = conn.cursor()
    cursor.execute("SELECT stars_counter FROM users WHERE user_id = ?", (id,))
    counter = cursor.fetchall()[0][0]
    conn.close()
    return counter
##########
def update_stars_counter_game3_db(id):
    conn = sqlite3.connect("db/game_three.db")
    cursor = conn.cursor()
    cursor.execute("SELECT stars_counter FROM users WHERE user_id = ?", (id,))
    counter = cursor.fetchall()[0][0]
    sql = "UPDATE users SET stars_counter=:COUNTER WHERE user_id=:ID"
    task = {'COUNTER': counter + 1, 'ID': id}
    cursor.execute(sql, task)
    conn.commit()
    conn.close()
##########
def reset_stars_counter_game3_db(id):
    conn = sqlite3.connect("db/game_three.db")
    cursor = conn.cursor()
    sql = "UPDATE users SET stars_counter=:COUNTER WHERE user_id=:ID"
    task = {'COUNTER': 0, 'ID': id}
    cursor.execute(sql, task)
    conn.commit()
    conn.close()
##########
def get_last_bet_game3_db(id):
    conn = sqlite3.connect("db/game_three.db")
    cursor = conn.cursor()
    cursor.execute("SELECT last_bet FROM users WHERE user_id = ?", (id,))
    counter = cursor.fetchall()[0][0]
    conn.close()
    return counter
##########
def update_last_bet_game3_db(id, bet):
    conn = sqlite3.connect("db/game_three.db")
    cursor = conn.cursor()
    sql = "UPDATE users SET last_bet=:BET WHERE user_id=:ID"
    task = {'BET': bet, 'ID': id}
    cursor.execute(sql, task)
    conn.commit()
    conn.close()
##########
def reset_last_bet_game3_db(id):
    conn = sqlite3.connect("db/game_three.db")
    cursor = conn.cursor()
    sql = "UPDATE users SET last_bet=:BET WHERE user_id=:ID"
    task = {'BET': 0, 'ID': id}
    cursor.execute(sql, task)
    conn.commit()
    conn.close()
##########
def update_counter_game3_db(id):
    conn = sqlite3.connect("db/game_three.db")
    cursor = conn.cursor()
    cursor.execute("SELECT counter FROM users WHERE user_id = ?", (id,))
    counter = cursor.fetchall()[0][0]
    sql = "UPDATE users SET counter=:COUNTER WHERE user_id=:ID"
    task = {'COUNTER': counter + 1, 'ID': id}
    cursor.execute(sql, task)
    conn.commit()
    conn.close()
##########
def get_counter_game3_db(id):
    conn = sqlite3.connect("db/game_three.db")
    cursor = conn.cursor()
    cursor.execute("SELECT counter FROM users WHERE user_id = ?", (id,))
    return cursor.fetchall()[0][0]
##########
def get_values_game3_db(id):
    conn = sqlite3.connect("db/game_three.db")
    cursor = conn.cursor()
    cursor.execute("SELECT box1, box2, box3, box4, box5, box6, box7, box8, box9 FROM users WHERE user_id = ?", (id,))
    arr = cursor.fetchall()[0]
    conn.close()
    return arr
##########
def reset_values_game3_db(id):
    conn = sqlite3.connect("db/game_three.db")
    cursor = conn.cursor()
    sql = "UPDATE users SET box1=:BOX1, box2=:BOX2, box3=:BOX3, box4=:BOX4, box5=:BOX5, box6=:BOX6, " \
          "box7=:BOX7, box8=:BOX8, box9=:BOX9 WHERE user_id=:ID"
    task = {'ID': id, 'BOX1': 0, 'BOX2': 0, 'BOX3': 0, 'BOX4': 0, 'BOX5': 0, 'BOX6': 0, 'BOX7': 0, 'BOX8': 0, 'BOX9': 0}
    cursor.execute(sql, task)
    conn.commit()
    conn.close()
##########
def reset_counter_game3_db(id):
    conn = sqlite3.connect("db/game_three.db")
    cursor = conn.cursor()
    sql = "UPDATE users SET counter=:COUNT WHERE user_id=:ID"
    task = {'ID': id, 'COUNT': 0}
    cursor.execute(sql, task)
    conn.commit()
    conn.close()
##########
def fill_arr_values_game3_db(id, arr):
    conn = sqlite3.connect("db/game_three.db")
    cursor = conn.cursor()
    sql = "UPDATE users SET box1=:BOX1, box2=:BOX2, box3=:BOX3, box4=:BOX4, box5=:BOX5, box6=:BOX6, " \
          "box7=:BOX7, box8=:BOX8, box9=:BOX9 WHERE user_id=:ID"
    task = {'ID': id, 'BOX1': arr[0], 'BOX2': arr[1], 'BOX3': arr[2], 'BOX4': arr[3], 'BOX5': arr[4], 'BOX6': arr[5],
            'BOX7': arr[6], 'BOX8': arr[7], 'BOX9': arr[8]}
    cursor.execute(sql, task)
    conn.commit()
    conn.close()
##########
def fill_values_game3_db(id):
    conn = sqlite3.connect("db/game_three.db")
    cursor = conn.cursor()
    sql = "UPDATE users SET box1=:BOX1, box2=:BOX2, box3=:BOX3, box4=:BOX4, box5=:BOX5, box6=:BOX6, " \
          "box7=:BOX7, box8=:BOX8, box9=:BOX9 WHERE user_id=:ID"
    task = {'ID': id, 'BOX1': 0, 'BOX2': 1, 'BOX3': 0, 'BOX4': 0, 'BOX5': 1, 'BOX6': 0, 'BOX7': 0, 'BOX8': 1, 'BOX9': 0}
    cursor.execute(sql, task)
    conn.commit()
    conn.close()
##########
def update_values_game3_db(id, index, val):
    conn = sqlite3.connect("db/game_three.db")
    cursor = conn.cursor()
    setArr = ["box1", "box2", "box3", "box4", "box5", "box6", "box7", "box8", "box9"]
    sql = "UPDATE users SET "+setArr[index]+"=:VAL WHERE user_id=:ID"
    task = {'VAL': val, 'ID': id}
    cursor.execute(sql, task)
    conn.commit()
    conn.close()

##########
 #cursor.execute("UPDATE users SET box1=:BOX1, box1=:BOX1, box1=:BOX1, box1=:BOX1, box1=:BOX1, box1=:BOX1,"
  #                 "box1=:BOX1, box1=:BOX1, box1=:BOX1 WHERE user_id=:ID")

def insert_to_last_trans_db(message):
    id = message.chat.id
    conn = sqlite3.connect("db/last_trans.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (user_id, phone_number, amount) VALUES (?, ?, ?)", (id, 0, 0))
    conn.commit()
    conn.close()

def update_phone_number(message):
    id = message.chat.id
    phone_number = message.text
    conn = sqlite3.connect("db/last_trans.db")
    cursor = conn.cursor()
    sql = "UPDATE users SET phone_number=:PHONE WHERE user_id=:ID"
    task = {'PHONE': phone_number, 'ID': id}
    cursor.execute(sql, task)
    conn.commit()
    conn.close()

def update_amount_trans(message):
    id = message.chat.id
    amount = int(message.text)
    conn = sqlite3.connect("db/last_trans.db")
    cursor = conn.cursor()
    sql = "UPDATE users SET amount=:AMOUNT WHERE user_id=:ID"
    task = {'AMOUNT': amount, 'ID': id}
    cursor.execute(sql, task)
    conn.commit()
    conn.close()

def update_last_trans(id, phone_number, amount):
    conn = sqlite3.connect("db/last_trans.db")
    cursor = conn.cursor()
    sql = "UPDATE users SET phone_number=:PHONE, amount=:AMOUNT WHERE user_id=:ID"
    task = {'PHONE': phone_number, 'AMOUNT': amount, 'ID': id}
    cursor.execute(sql, task)
    conn.commit()
    conn.close()

def get_number_last_trans(id):
    conn = sqlite3.connect("db/last_trans.db")
    cursor = conn.cursor()
    cursor.execute("SELECT phone_number FROM users WHERE user_id = ?", (id,))
    phone = cursor.fetchall()[0][0]
    conn.close()
    return phone

def get_amount_last_trans(id):
    conn = sqlite3.connect("db/last_trans.db")
    cursor = conn.cursor()
    cursor.execute("SELECT amount FROM users WHERE user_id = ?", (id,))
    amount = cursor.fetchall()[0][0]
    conn.close()
    return amount
###########
def insert_to_status_db(message):
    id = message.chat.id
    conn = sqlite3.connect("db/status_base.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (user_id, status_id) VALUES (?, ?)", (id, 0))
    conn.commit()
    conn.close()

def update_status_db(message, status_id):
    id = message.chat.id
    conn = sqlite3.connect("db/status_base.db")
    cursor = conn.cursor()
    sql = "UPDATE users SET status_id=:STATUS WHERE user_id=:ID"
    task = {'STATUS': status_id, 'ID': id}
    cursor.execute(sql, task)
    conn.commit()
    conn.close()

def get_status_id(message):
    id = message.chat.id
    conn = sqlite3.connect("db/status_base.db")
    cursor = conn.cursor()
    cursor.execute("SELECT status_id FROM users WHERE user_id = ?", (id,))
    status = cursor.fetchall()[0][0]
    conn.close()
    return status
##########
def check_row(message):
    id = message.chat.id
    conn = sqlite3.connect("db/base.db")
    cursor = conn.cursor()
    cursor.execute("SELECT user_name FROM users WHERE user_id = ?", (id,))
    if (cursor.fetchall() == []):
        conn.close()
        return False
    else:
        conn.close()
        return True

def add_balance(id, number):
    #id = message.chat.id
    conn = sqlite3.connect("db/base.db")
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM users WHERE user_id = ?", (id,))
    n = cursor.fetchall()[0][0]
    bal = n + number
    sql = "UPDATE users SET balance=:BAL WHERE user_id=:ID"
    task = {'BAL': bal, 'ID': id}
    cursor.execute(sql, task)
    conn.commit()
    conn.close()

def sub_balance(id, number):
    #id = message.chat.id
    conn = sqlite3.connect("db/base.db")
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM users WHERE user_id = ?", (id,))
    n = cursor.fetchall()[0][0]
    bal = n - number
    sql = "UPDATE users SET balance=:BAL WHERE user_id=:ID"
    task = {'BAL': bal, 'ID': id}
    cursor.execute(sql, task)
    conn.commit()
    conn.close()

def get_balance(id):
   # id = message.chat.id
    conn = sqlite3.connect("db/base.db")
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM users WHERE user_id = ?", (id,))
    n = cursor.fetchall()[0][0]
    conn.close()
    return n

def stat_game(id, game):
    if(game == 1):
        col = "stat_one"
    if(game == 2):
        col = "stat_two"
    if(game == 3):
        col = "stat_three"
    conn = sqlite3.connect("db/base.db")
    cursor = conn.cursor()
    sql = "SELECT "+col+" FROM users WHERE user_id =:ID"
    cursor.execute(sql, (id,))
    val = cursor.fetchall()[0][0] + 1
    sql_up = "UPDATE users SET "+col+"=:VAL WHERE user_id=:ID"
    task = {'VAL': val, 'ID': id}
    cursor.execute(sql_up, task)
    conn.commit()
    conn.close()

def trans_id():
    conn = sqlite3.connect("db/trans_id.db")
    cursor = conn.cursor()
    cursor.execute("SELECT trans_id FROM users")
    n = cursor.fetchall()[0][0]
    cursor.execute("UPDATE users SET trans_id = ?", (n+1,))
    conn.commit()
    cursor.execute("SELECT trans_id FROM users")
    n = cursor.fetchall()[0][0]
    conn.close()
    return n

def new_trans_id(message):
    id = message.chat.id
    conn = sqlite3.connect("db/base.db")
    cursor = conn.cursor()
    n = trans_id()
    sql = "UPDATE users SET lt_id=:N WHERE user_id=:ID"
    task = {'N': n, 'ID': id}
    cursor.execute(sql, task)
    conn.commit()
    conn.close()
    return n

def get_lt_id(id):
    conn = sqlite3.connect("db/base.db")
    cursor = conn.cursor()
    cursor.execute("SELECT lt_id FROM users WHERE user_id = ?", (id,))
    res = cursor.fetchall()[0][0]
    conn.close()
    return res

def erase_trans_id(id):
    conn = sqlite3.connect("db/base.db")
    cursor = conn.cursor()
    sql = "UPDATE users SET lt_id=:N WHERE user_id=:ID"
    task = {'N': 0, 'ID': id}
    cursor.execute(sql, task)
    conn.commit()
    conn.close()
