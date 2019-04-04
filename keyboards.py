import telebot
from telebot import types
#from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton


def start_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = types.KeyboardButton("Первая игра")
    itembtn2 = types.KeyboardButton('Вторая игра')
    itembtn3 = types.KeyboardButton('Третья игра')
    itembtn4 = types.KeyboardButton("\U0001F4B0" + " " + 'Кошелек')
    itembtn5 = types.KeyboardButton("\U00002753" + " " + 'Инфо')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)
    return markup

def info_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = types.KeyboardButton("\U0001F4C3" + " " + 'Правила')
    itembtn2 = types.KeyboardButton("\U0001F4C4" + " " + 'Дополнительная информация')
    itembtn3 = types.KeyboardButton("\U0001F464" + " " + 'Партнерская программа')
    itembtn4 = types.InlineKeyboardButton("\U000021A9" + " " + 'Назад')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    return markup

def purse_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = types.KeyboardButton("\U0001F4B2" + " " + 'Проверить баланс')
    itembtn2 = types.KeyboardButton("\U0001F4B5" + " " + 'Пополнить баланс')
    itembtn3 = types.KeyboardButton("\U0001F4B8" + " " + 'Вывести монеты')
    itembtn4 = types.KeyboardButton("\U000021A9" + " " + 'Назад')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    return markup

def game_one_keyboard():
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text="50", callback_data='set50')
    item2 = types.InlineKeyboardButton(text="100", callback_data='set100')
    item3 = types.InlineKeyboardButton(text="150", callback_data='set150')
    item4 = types.InlineKeyboardButton(text="500", callback_data='set500')
    markup.add(item1, item2, item3, item4)
    return markup

def game_two_bet_keyboard():
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text="50", callback_data='g2_50')
    item2 = types.InlineKeyboardButton(text="100", callback_data='g2_100')
    item3 = types.InlineKeyboardButton(text="150", callback_data='g2_150')
    item4 = types.InlineKeyboardButton(text="500", callback_data='g2_500')
    markup.add(item1, item2, item3, item4)
    return markup

def game_two_keyboard():
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text="Орел", callback_data='0')
    item2 = types.InlineKeyboardButton(text="Решка", callback_data='1')
    markup.add(item1, item2)
    return markup

def game_three_keyboard():
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text="50", callback_data='g3_50')
    item2 = types.InlineKeyboardButton(text="100", callback_data='g3_100')
    item3 = types.InlineKeyboardButton(text="150", callback_data='g3_150')
    item4 = types.InlineKeyboardButton(text="500", callback_data='g3_500')
    markup.add(item1, item2, item3, item4)
    return markup

def game_one_restart_button():
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text="Заново", callback_data='restart_one')
    markup.add(item1)
    return markup

def game_two_restart_button():
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text="Заново", callback_data='restart_two')
    markup.add(item1)
    return markup

def game_three_restart_button():
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text="Заново", callback_data='restart_three')
    markup.add(item1)
    return markup

def payment_keyboard():
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text="Проверить перевод", callback_data='check_payment')
    markup.add(item1)
    return markup

def cancel_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton("\U0000274C" + " " + 'Отмена')
    markup.add(item)
    return markup

def withdrawal_keyboard():
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text="\U00002716" + " " + "Отмена", callback_data="cancel_payment")
    item2 = types.InlineKeyboardButton(text="\U00002714" + " " + "Подтвердить", callback_data="accept_payment")
    markup.add(item1, item2)
    return markup

def remover_keyboard():
    return types.ReplyKeyboardRemove()

def rules_keyboard_first():
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text="\U000025B6" + " " + "Далее", callback_data="page_next")
    markup.add(item1)
    return markup

def rules_keyboard_second():
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text="\U000025C0" + " " + "Назад", callback_data="page_back")
    item2 = types.InlineKeyboardButton(text="\U000025B6" + " " + "Далее", callback_data="page_last")
    markup.add(item1, item2)
    return markup

def rules_keyboard_third():
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text="\U000025C0" + " " + "Назад", callback_data="page_back_two")
    markup.add(item1)
    return markup




