import random
from telebot import types
import db
import gen_arr
import keyboards
def game_one():
   res = random.randint(0, 5)
   if(res == 0 or res == 1):
       return 50
   elif (res == 2 or res == 3 or res == 4):
       return 100
   else:
       return 150


def game_two():
    res = random.randint(0, 1)
    return res


def game_three(id):
    db.fill_arr_values_game3_db(id, gen_arr.gen_array())
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text="\U0001F381", callback_data="box1")
    item2 = types.InlineKeyboardButton(text="\U0001F381", callback_data="box2")
    item3 = types.InlineKeyboardButton(text="\U0001F381", callback_data="box3")
    item4 = types.InlineKeyboardButton(text="\U0001F381", callback_data="box4")
    item5 = types.InlineKeyboardButton(text="\U0001F381", callback_data="box5")
    item6 = types.InlineKeyboardButton(text="\U0001F381", callback_data="box6")
    item7 = types.InlineKeyboardButton(text="\U0001F381", callback_data="box7")
    item8 = types.InlineKeyboardButton(text="\U0001F381", callback_data="box8")
    item9 = types.InlineKeyboardButton(text="\U0001F381", callback_data="box9")
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
  #  db.update_counter_game3_db(id)
    return markup

def update_game_three(id, boxIndex):
    t1 = "\U0001F381"; t2 = "\U0001F381"; t3 = "\U0001F381"; t4 = "\U0001F381"; t5 = "\U0001F381"; t6 = "\U0001F381";
    t7 = "\U0001F381"; t8 = "\U0001F381"; t9 = "\U0001F381";
    itemText = [t1, t2, t3, t4, t5, t6, t7, t8, t9]
    c1 = "box1"; c2 = "box2"; c3 = "box3"; c4 = "box4"; c5 = "box5"; c6 = "box6"; c7 = "box7"; c8 = "box8"; c9 = "box9";
    itemCallData = [c1, c2, c3, c4, c5, c6, c7, c8, c9]

    arr = db.get_values_game3_db(id)

    if arr[boxIndex] == 1:
        itemText[boxIndex] = "\U00002B50"; itemCallData[boxIndex] = "-"
        db.update_stars_counter_game3_db(id)
        db.update_values_game3_db(id, boxIndex, 2)
    else:
        itemText[boxIndex] = "\U0001F344"; itemCallData[boxIndex] = "-"
        db.update_values_game3_db(id, boxIndex, 3)
    ind = 0;
    while ind <= 8:
        if arr[ind] == 2:
            itemText[ind] = "\U00002B50"; itemCallData[ind] = "-"
        if arr[ind] == 3:
            itemText[ind] = "\U0001F344"; itemCallData[ind] = "-"
        ind = ind + 1

    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text=itemText[0], callback_data=itemCallData[0])
    item2 = types.InlineKeyboardButton(text=itemText[1], callback_data=itemCallData[1])
    item3 = types.InlineKeyboardButton(text=itemText[2], callback_data=itemCallData[2])
    item4 = types.InlineKeyboardButton(text=itemText[3], callback_data=itemCallData[3])
    item5 = types.InlineKeyboardButton(text=itemText[4], callback_data=itemCallData[4])
    item6 = types.InlineKeyboardButton(text=itemText[5], callback_data=itemCallData[5])
    item7 = types.InlineKeyboardButton(text=itemText[6], callback_data=itemCallData[6])
    item8 = types.InlineKeyboardButton(text=itemText[7], callback_data=itemCallData[7])
    item9 = types.InlineKeyboardButton(text=itemText[8], callback_data=itemCallData[8])
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
    db.update_counter_game3_db(id)
    return markup
