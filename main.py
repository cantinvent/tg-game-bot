import telebot
import misc
import db
import keyboards
import games
import time
import pay
import re
import rules.rule
import info
import description

token = misc.token
bot = telebot.TeleBot(token)
bot.remove_webhook()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if db.check_row(message) == False:
        db.insert_to_db(message)
        bot.send_message(message.chat.id, "Добро пожаловать " + message.chat.first_name,
                     reply_markup = keyboards.start_keyboard())
    else:
        bot.send_message(message.chat.id, "С возвращением " + message.chat.first_name,
                         reply_markup=keyboards.start_keyboard())

@bot.message_handler(func = lambda message: message.text == "\U0000274C" + " " + 'Cancel')
def cancel(message):
    db.update_status_db(message, 0)
    bot.send_message(message.chat.id, "\U0001F4D1" + " " + "Главное меню", reply_markup=keyboards.start_keyboard())

@bot.message_handler(func = lambda message: db.get_status_id(message) == 1)
def withdrawal_hanlder_amount(message):
    if not message.text.isdigit():
        bot.send_message(message.chat.id, "Пожалуйста, вводите только цифры")
    else:
        if message.text == "0":
            bot.send_message(message.chat.id, "Вы не можете вывести 0 монет")
        else:
            if int(message.text) <= db.get_balance(message.chat.id):
                db.update_amount_trans(message)
                bot.send_message(message.chat.id, "Введите номер кошелька")
                db.update_status_db(message, 2)
            else:
                bot.send_message(message.chat.id, "Недостаточно монет на балансе")

@bot.message_handler(func = lambda message: db.get_status_id(message) == 2)
def withdrawal_hanlder_number(message):
    if re.match(r'[7]{1}[9]{1}[0-9]{9}', message.text) and len(message.text) == 11:
        db.update_phone_number(message)
        bot.send_message(message.chat.id, "Пожалуйста, проверьте Ваш запрос", reply_markup= keyboards.remover_keyboard())
        bot.send_message(message.chat.id, "Номер кошелька: " + db.get_number_last_trans(message.chat.id)
                         + "\n" + "Количество монет: " + str(db.get_amount_last_trans(message.chat.id))
                         , reply_markup=keyboards.withdrawal_keyboard())
        db.update_status_db(message, 0)
    else:
        bot.send_message(message.chat.id, "Пожалуйста, проверьте Ваш номер кошелька")

@bot.message_handler(content_types=["text"])
def comm_handler(message):
    select = ""
    if(message.text == "Первая игра"):
        bot.send_message(message.chat.id, description.game_one,
                         reply_markup=keyboards.game_one_keyboard())
    elif (message.text == "Вторая игра"):
        bot.send_message(message.chat.id, description.game_two,
                         reply_markup=keyboards.game_two_bet_keyboard())
    elif (message.text == "Третья игра"):
        bot.send_message(message.chat.id, description.game_three,
                         reply_markup=keyboards.game_three_keyboard())
    elif (message.text == "\U0001F4C3" + " " + 'Правила'):
        bot.send_message(message.chat.id, rules.rule.first_page, reply_markup=keyboards.rules_keyboard_first())
    elif (message.text == "\U00002753" + " " + 'Инфо'):
        bot.send_message(message.chat.id, "Информация", reply_markup=keyboards.info_keyboard())
     #   pay.send_money(5, 79535780551)
      #  print(db.get_values_game3_db(message.chat.id))
    elif(message.text == "\U0001F4C4" + " " + 'Дополнительная информация'):
        bot.send_message(message.chat.id, info.inform)
    elif (message.text == "\U0001F464" + " " + 'Партнерская программа'):
        bot.send_message(message.chat.id, "Скоро!")
    elif(message.text == "\U0001F4B0" + " " + 'Кошелек'):
        select == message.text
        bot.send_message(message.chat.id, "Выберите: ", reply_markup=keyboards.purse_keyboard())
    elif (message.text == "\U0001F4B2" + " " + 'Проверить баланс'):
        bot.send_message(message.chat.id, "\U0001F4B2" + " " + "Ваш баланс: " + str(db.get_balance(message.chat.id)))
    elif (message.text == "\U0001F4B5" + " " + 'Пополнить баланс'):
        trans_id = db.new_trans_id(message)
        bot.send_message(message.chat.id, "Ваш комментарий к переводу: " + str(trans_id),
                         reply_markup=keyboards.payment_keyboard())
    elif (message.text == "\U0001F4B8" + " " + 'Вывести монеты'):
        bot.send_message(message.chat.id, "Введите количество монет для вывода: ",
                         reply_markup=keyboards.cancel_keyboard())
        db.update_status_db(message, 1)
    elif (message.text == "\U000021A9" + " " + 'Назад'):
        bot.send_message(message.chat.id, "\U0001F4D1" + " " + "Главное меню", reply_markup=keyboards.start_keyboard())
    else:
        bot.send_message(message.chat.id, "Пожалуйста, используйте клавиатуру")

@bot.callback_query_handler(func = lambda call: True)
def callback_inline(call):
    id = call.from_user.id
    set1 = 0; set2 = 0; set3 = 0
    ###game one###
    if call.data == "set50":
        set1 = check_bet(call, id, 50)
    elif call.data == "set100":
        set1 = check_bet(call, id, 100)
    elif call.data == "set150":
        set1 = check_bet(call, id, 150)
    elif call.data == "set500":
        set1 = check_bet(call, id, 500)

    if(set1 != 0):
        db.sub_balance(id, set1)
        db.stat_game(id, 1)
        res = games.game_one()
        db.add_balance(id, res)
        bot.edit_message_text(chat_id=id, message_id=call.message.message_id,
                              text="It's the first game!!! Good luck !!! Have fun!!! You win: " + str(res),
                              reply_markup=keyboards.game_one_restart_button())

    ###game two###
    if call.data == "g2_50":
        set2 = check_bet(call, id, 50)
    elif call.data == "g2_100":
        set2 = check_bet(call, id, 100)
    elif call.data == "g2_150":
        set2 = check_bet(call, id, 150)
    elif call.data == "g2_500":
        set2 = check_bet(call, id, 500)

    if (set2 != 0):
        db.sub_balance(id, set2)
        db.update_last_bet_game2_db(id, set2)
        bot.edit_message_text(chat_id=id, message_id=call.message.message_id,
                              text="Орел или Решка?",
                              reply_markup=keyboards.game_two_keyboard())

    if call.data == "0" or call.data == "1":
        db.stat_game(id, 2)
        set2 = db.get_last_bet_game2_db(id)
        res = games.game_two()
        if(res == 1):
            db.add_balance(id, set2*2)
            bot.edit_message_text(chat_id=id, message_id=call.message.message_id,
                                  text="It's the second game!!! Good luck !!! Have fun!!! You win: " + str(set2*2),
                                  reply_markup=keyboards.game_two_restart_button())
        else:
            db.add_balance(id, 0)
            bot.edit_message_text(chat_id=id, message_id=call.message.message_id,
                                  text="It's the second game!!! Good luck !!! Have fun!!! You win: " + str(0),
                                  reply_markup=keyboards.game_two_restart_button())
        db.reset_last_bet_game2_db(id)

    ###game three###
    if call.data == "g3_50":
        set3 = check_bet(call, id, 50)
    elif call.data == "g3_100":
        set3 = check_bet(call, id, 100)
    elif call.data == "g3_150":
        set3 = check_bet(call, id, 150)
    elif call.data == "g3_500":
        set3 = check_bet(call, id, 500)

    if(set3 != 0):
        db.sub_balance(id, set3)
        db.update_last_bet_game3_db(id, set3)
        db.stat_game(id, 3)
        bot.edit_message_text(chat_id=id, message_id=call.message.message_id,
                              text="Откройте три коробки и найдите три звезды",
                              reply_markup=games.game_three(id))

    if call.data == "box1":
        if db.get_counter_game3_db(id) == 2:
            games.update_game_three(id, 0)
            game3_message(call, id)
        else:
            bot.edit_message_text(chat_id=id, message_id=call.message.message_id,
                                  text="Откройте три коробки и найдите три звезды",
                                  reply_markup=games.update_game_three(id, 0))
    if call.data == "box2":
        if db.get_counter_game3_db(id) == 2:
            games.update_game_three(id, 1)
            game3_message(call, id)
        else:
            bot.edit_message_text(chat_id=id, message_id=call.message.message_id,
                                  text="Откройте три коробки и найдите три звезды",
                                  reply_markup=games.update_game_three(id, 1))
    if call.data == "box3":
        if db.get_counter_game3_db(id) == 2:
            games.update_game_three(id, 2)
            game3_message(call, id)
        else:
            bot.edit_message_text(chat_id=id, message_id=call.message.message_id,
                                  text="Откройте три коробки и найдите три звезды",
                                  reply_markup=games.update_game_three(id, 2))
    if call.data == "box4":
        if db.get_counter_game3_db(id) == 2:
            games.update_game_three(id, 3)
            game3_message(call, id)
        else:
            bot.edit_message_text(chat_id=id, message_id=call.message.message_id,
                                  text="Откройте три коробки и найдите три звезды",
                                  reply_markup=games.update_game_three(id, 3))
    if call.data == "box5":
        if db.get_counter_game3_db(id) == 2:
            games.update_game_three(id, 4)
            game3_message(call, id)
        else:
            bot.edit_message_text(chat_id=id, message_id=call.message.message_id,
                                  text="Откройте три коробки и найдите три звезды",
                                  reply_markup=games.update_game_three(id, 4))
    if call.data == "box6":
        if db.get_counter_game3_db(id) == 2:
            games.update_game_three(id, 5)
            game3_message(call, id)
        else:
            bot.edit_message_text(chat_id=id, message_id=call.message.message_id,
                                  text="Откройте три коробки и найдите три звезды",
                                  reply_markup=games.update_game_three(id, 5))
    if call.data == "box7":
        if db.get_counter_game3_db(id) == 2:
            games.update_game_three(id, 6)
            game3_message(call, id)
        else:
            bot.edit_message_text(chat_id=id, message_id=call.message.message_id,
                                  text="Откройте три коробки и найдите три звезды",
                                  reply_markup=games.update_game_three(id, 6))
    if call.data == "box8":
        if db.get_counter_game3_db(id) == 2:
            games.update_game_three(id, 7)
            game3_message(call, id)
        else:
            bot.edit_message_text(chat_id=id, message_id=call.message.message_id,
                                  text="Откройте три коробки и найдите три звезды",
                                  reply_markup=games.update_game_three(id, 7))
    if call.data == "box9":
        if db.get_counter_game3_db(id) == 2:
            games.update_game_three(id, 8)
            game3_message(call, id)
        else:
            bot.edit_message_text(chat_id=id, message_id=call.message.message_id,
                                  text="Откройте три коробки и найдите три звезды",
                                  reply_markup=games.update_game_three(id, 8))


    if (call.data=="restart_one"):
        bot.edit_message_text(chat_id=id, message_id=call.message.message_id,
                              text="It's the first game!!! Good luck !!! Have fun!!!",
                              reply_markup=keyboards.game_one_keyboard())

    if (call.data=="restart_two"):
        bot.edit_message_text(chat_id=id, message_id=call.message.message_id,
                              text="It's the second game!!! Good luck !!! Have fun!!!",
                              reply_markup=keyboards.game_two_bet_keyboard())

    if (call.data=="restart_three"):
        bot.edit_message_text(chat_id=id, message_id=call.message.message_id,
                              text="It's the third game!!! Good luck !!! Have fun!!!",
                              reply_markup=keyboards.game_three_keyboard())

    if(call.data=="check_payment"):
        #comment = "Пополнение или возврат по QVC (QVP)"
        comment = db.get_lt_id(id)
        amount = pay.qiwi_amount(str(comment))
        if(amount <= 0 or amount == None):
            bot.edit_message_text(chat_id=id, message_id=call.message.message_id,
                                  text="Пожалуйста, проверьте правильность перевода и нажмите снова!",
                                  reply_markup=keyboards.payment_keyboard())
        else:
            db.add_balance(id, amount)
            db.erase_trans_id(id)
            balance = db.get_balance(id)
            bot.edit_message_text(chat_id=id, message_id=call.message.message_id,
                                  text="Пополнение совершено. Ваш баланс: " + str(balance))

    if(call.data=="cancel_payment"):
        db.update_last_trans(id, 0, 0)
        bot.edit_message_text(chat_id=id, message_id=call.message.message_id,
                              text="Вы отменили запрос")
        bot.send_message(id, "\U0001F4D1" + " " + "Главное меню", reply_markup=keyboards.start_keyboard())

    if(call.data=="accept_payment"):
        amount = db.get_amount_last_trans(id)
        bot.edit_message_text(chat_id=id, message_id=call.message.message_id,
                              text="Вы подтвердили запрос")
       # pay.test_send(amount, db.get_number_last_trans(id))
        pay.send_money(amount, db.get_number_last_trans(id))
        db.sub_balance(id, amount)
        db.update_last_trans(id, 0, 0)
        bot.send_message(id, "\U0001F4D1" + " " + "Главное меню", reply_markup=keyboards.start_keyboard())


    if(call.data == "page_next"):
        bot.edit_message_text(chat_id=id, message_id=call.message.message_id, text=rules.rule.second_page,
                              reply_markup=keyboards.rules_keyboard_second())

    if (call.data == "page_last"):
        bot.edit_message_text(chat_id=id, message_id=call.message.message_id, text=rules.rule.third_page,
                              reply_markup=keyboards.rules_keyboard_third())

    if (call.data == "page_back"):
        bot.edit_message_text(chat_id=id, message_id=call.message.message_id, text=rules.rule.first_page,
                              reply_markup=keyboards.rules_keyboard_first())

    if (call.data == "page_back_two"):
        bot.edit_message_text(chat_id=id, message_id=call.message.message_id, text=rules.rule.second_page,
                              reply_markup=keyboards.rules_keyboard_second())

def game3_message(call, id):
    stars = db.get_stars_counter_game3_db(id)
    if stars == 0:
        amount = db.get_last_bet_game3_db(id) * 0.2
    else:
        amount = db.get_last_bet_game3_db(id) * stars * 0.75
    db.add_balance(id, amount)
    db.reset_counter_game3_db(id)
    db.reset_values_game3_db(id)
    db.reset_stars_counter_game3_db(id)

    if stars == 0:
        bot.edit_message_text(chat_id=id, message_id=call.message.message_id,
                              text="Вы нашли " + str(stars) + " звезд" + "\n" + " Win " + str(amount),
                              reply_markup=keyboards.game_three_restart_button())
    if stars == 1:
        bot.edit_message_text(chat_id=id, message_id=call.message.message_id,
                              text="Вы нашли " + str(stars) + " звезду" + "\n" + " Win " + str(amount),
                              reply_markup=keyboards.game_three_restart_button())
    if stars > 1:
        bot.edit_message_text(chat_id=id, message_id=call.message.message_id,
                              text="Вы нашли " + str(stars) + " звезды" + "\n" + " Win " + str(amount),
                              reply_markup=keyboards.game_three_restart_button())

def check_bet(call, id, amount):
    if db.get_balance(id) >= amount:
        return amount
    else:
        bot.edit_message_text(chat_id=id, message_id=call.message.message_id,
                              text="Недостаточно монет. Ваш баланс: " + str(db.get_balance(id)))
        return 0

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(15)


# if __name__ == '__main__':
# 	app.run(host= '0.0.0.0', port='443', debug=True)

