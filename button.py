from telebot import TeleBot, types


def but_start():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # растяни по ширине экрана и добавь две кнопк
    but_1 = types.KeyboardButton('/start')
    markup.add(but_1)
    return markup


def but_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # растяни по ширине экрана и добавь две кнопк
    button_menu = types.KeyboardButton('/menu')
    markup.add(button_menu)
    return markup


def but_calc():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # растяни по ширине экрана и добавь две кнопк
    but_1 = types.KeyboardButton('/complex_number')
    but_2 = types.KeyboardButton('/rational_numbers')
    markup.add(but_1, but_2)
    return markup


def but_complex_calc():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    but_1 = types.KeyboardButton('/complex_number')
    but_2 = types.KeyboardButton('/menu')
    markup.add(but_1, but_2)
    return markup


def but_operation():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    but_1 = types.KeyboardButton('+')
    but_2 = types.KeyboardButton('-')
    but_3 = types.KeyboardButton('*')
    but_4 = types.KeyboardButton('/')
    but_5 = types.KeyboardButton('/menu')
    markup.add(but_1, but_2, but_3, but_4, but_5)
    return markup
