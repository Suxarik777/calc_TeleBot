from telebot import TeleBot, types

from Token_id import TOKEN_ID
from bot_mess import start_mess, menu_mess, complex_digit_1_mess, complex_digit_2_mess, operation_mess, \
                    result_mess, rational_digit_1_mess, rational_digit_2_mess
from button import but_start, but_menu, but_calc, but_complex_calc, but_operation
from calculation import calc_operation_complex, calc_operation_rational
from loger import result_logger

TOKEN = TOKEN_ID

bot = TeleBot(TOKEN)


# step save data_user in list: [0] - digit_1, [1] - digit_2, [2] - operation, [3] - result
dct = {}    # создаём словарик в котором будем по id пользователя хранить введёные им значение ещё и в lst
what_calc = {}


@bot.message_handler(commands=['start'])
def start_program(msg: types.Message):
    dct[msg.from_user.id] = []  # и при старте по его айди словарика кладём пустой список
    what_calc[msg.from_user.id] = ''  # создаём пустую строку по ID чтобы потом в логи вывести значение калькулятора

    bot.send_message(chat_id=msg.chat.id, text=start_mess(msg), parse_mode='html', reply_markup=but_menu())


@bot.message_handler(commands=['menu'])
def menu(msg: types.Message):
    bot.send_message(chat_id=msg.chat.id, text=menu_mess(msg), parse_mode='html', reply_markup=but_calc())


# Работа с комплексными числами
@bot.message_handler(commands=['complex_number'])
def complex_calc(msg: types.Message):
    what_calc[msg.from_user.id] = 'complex_number'

    bot.send_message(chat_id=msg.chat.id, text=complex_digit_1_mess(msg), parse_mode='html', reply_markup=but_menu())
    bot.register_next_step_handler(msg, complex_calc_step_2)


@bot.message_handler(commands=['rational_numbers'])
def rational_calc(msg: types.Message):
    what_calc[msg.from_user.id] = 'rational_numbers'

    bot.send_message(chat_id=msg.chat.id, text=rational_digit_1_mess(msg), parse_mode='html', reply_markup=but_menu())
    bot.register_next_step_handler(msg, rational_calc_step_2)


@bot.message_handler(content_types=['text'])
def complex_calc_step_2(msg: types.Message):
    id_ = msg.from_user.id  # этой переменной просто кладём его id в сокращённую переменную
    text = msg.text

    if text == '':  # если пользователь ничего не написал
        bot.send_message(chat_id=msg.from_user.id, text=f'Ошибка! Нет числа!!! \nЧто делаем?',
                         reply_markup=but_complex_calc())
    elif text.count('j') != 1:
        bot.send_message(chat_id=msg.from_user.id, text=f'Ошибка! неправильный формат!!! \nЧто делаем?',
                         reply_markup=but_complex_calc())
    else:
        dct[id_].append(text)
        bot.send_message(chat_id=msg.from_user.id, text=complex_digit_2_mess(msg), parse_mode='html',
                         reply_markup=but_menu())
        bot.register_next_step_handler(msg, complex_calc_operation)


def complex_calc_operation(msg: types.Message):
    id_ = msg.from_user.id
    text = msg.text

    if len(dct[id_]) < 1:  # если пользователь не написал второе число
        bot.send_message(chat_id=msg.from_user.id, text=f'Ошибка! Нет второго числа!!! \nЧто делаем?',
                         reply_markup=but_complex_calc())
    elif text.count('j') != 1:
        bot.send_message(chat_id=msg.from_user.id, text=f'Ошибка! неправильный формат!!! \nЧто делаем?',
                         reply_markup=but_complex_calc())
    else:
        dct[id_].append(text)
        bot.send_message(chat_id=msg.from_user.id, text=operation_mess(msg), parse_mode='html',
                         reply_markup=but_operation())
        bot.register_next_step_handler(msg, complex_calc_result)

def complex_calc_result(msg: types.Message):
    id_ = msg.from_user.id
    text = msg.text

    dct[id_].append(text)
    result = calc_operation_complex(dct[id_])
    dct[id_].append(result)

    result_logger(msg, dct[id_], what_calc[id_])

    bot_mess = result_mess(msg, dct[id_])
    bot.send_message(chat_id=msg.from_user.id, text=bot_mess, parse_mode='html',
                     reply_markup=but_start())


# Работа с рациональными числами


@bot.message_handler(content_types=['text'])
def rational_calc_step_2(msg: types.Message):
    id_ = msg.from_user.id  # этой переменной просто кладём его id в сокращённую переменную
    text = msg.text

    if text == '':  # если пользователь ничего не написал
        bot.send_message(chat_id=msg.from_user.id, text=f'Ошибка! Нет числа!!! \nЧто делаем?',
                         reply_markup=but_complex_calc())
    elif text.count('/') != 1:
        bot.send_message(chat_id=msg.from_user.id, text=f'Ошибка! неправильный формат!!! \nЧто делаем?',
                         reply_markup=but_complex_calc())
    else:
        dct[id_].append(text)
        bot.send_message(chat_id=msg.from_user.id, text=rational_digit_2_mess(msg), parse_mode='html',
                         reply_markup=but_menu())
        bot.register_next_step_handler(msg, rational_calc_operation)


def rational_calc_operation(msg: types.Message):
    id_ = msg.from_user.id
    text = msg.text

    if len(dct[id_]) < 1:  # если пользователь не написал второе число
        bot.send_message(chat_id=msg.from_user.id, text=f'Ошибка! Нет второго числа!!! \nЧто делаем?',
                         reply_markup=but_complex_calc())
    elif text.count('/') != 1:
        bot.send_message(chat_id=msg.from_user.id, text=f'Ошибка! неправильный формат!!! \nЧто делаем?',
                         reply_markup=but_complex_calc())
    else:
        dct[id_].append(text)
        bot.send_message(chat_id=msg.from_user.id, text=operation_mess(msg), parse_mode='html',
                         reply_markup=but_operation())
        bot.register_next_step_handler(msg, rational_calc_result)


def rational_calc_result(msg: types.Message):
    id_ = msg.from_user.id
    text = msg.text

    dct[id_].append(text)
    result = calc_operation_rational(dct[id_])
    dct[id_].append(result)

    result_logger(msg, dct[id_], what_calc[id_])

    bot_mess = result_mess(msg, dct[id_])
    bot.send_message(chat_id=msg.from_user.id, text=bot_mess, parse_mode='html',
                     reply_markup=but_start())

bot.polling(none_stop=True)