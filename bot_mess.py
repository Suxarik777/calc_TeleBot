from telebot import TeleBot, types


def start_mess(msg):
    bot_mess: str = f'''Привет, <b>{msg.from_user.first_name} {msg.from_user.last_name}</b>
Я создан студентом GeekBrains и я калькулятор
ЖМИ на команду  \n<b>/menu</b>'''
    return bot_mess


def menu_mess(msg):
    bot_mess: str = 'С какими числами будем работать?' \
                    '\n<b>/complex_number</b> ' \
                    '\n<b>/rational_numbers</b>'
    return bot_mess


def complex_digit_1_mess(msg):
    bot_mess: str = 'Введите первое число' \
                    '\n<i>(используйте формат: "5+3j")</i>' \
                    '\n<i><u>без пробелов!</u></i>'
    return bot_mess


def complex_digit_2_mess(msg):
    bot_mess: str = 'Введите второе число' \
                    '\n<i>(используйте формат: "5+3j")</i>' \
                    '\n<i><u>без пробелов!</u></i>'
    return bot_mess


def operation_mess(msg):
    bot_mess: str = 'выберите операцию:' \
                    '\n<i>+   summa</i>' \
                    '\n<i>-   sub</i>' \
                    '\n<i>*  mult</i>' \
                    '\n<i>/   div</i>'
    return bot_mess


def result_mess(msg, dct_lst_user_id):
    digit_1, digit_2, operation, result = dct_lst_user_id
    bot_mess: str = 'Результат:' \
                    f'\n<i>{digit_1} {operation} {digit_2}</i>' \
                    f'\n<i>= {result}</i>' \

    return bot_mess

def rational_digit_1_mess(msg):
    bot_mess: str = 'Введите первое число' \
                    '\n<i>(используйте формат: "5/11")</i>'
    return bot_mess

def rational_digit_2_mess(msg):
    bot_mess: str = 'Введите второе число' \
                    '\n<i>(используйте формат: "5/11")</i>'
    return bot_mess