from telebot import TeleBot, types
from datetime import datetime
from time import time



def result_logger(msg, dct_lst_user_id, what_calc):
    digit_1, digit_2, operation, result = dct_lst_user_id
    data_str = f'{str(digit_1)} {operation} {str(digit_2)} = {result}'

    time = datetime.now().strftime('%H:%M')

    with open('log.csv', 'a', encoding='UTF-8') as file:
        file.write(f'Пользователь: {msg.from_user.id} {msg.from_user.username} {msg.from_user.first_name} '
                   f'{msg.from_user.last_name} {msg.from_user.language_code}'
                   f'\nСтатус телеграмм premium: {msg.from_user.is_premium}'
                   f'\nПараметры чата: {msg.chat.id}, {msg.chat.type}'
                   f'\n---------------------------------------------'
                   f'\nВид калькулятора: {what_calc}'
                   f'\n---------------------------------------------'
                   f'\nОперация: {data_str}'
                   f'\n---------------------------------------------'
                   f'\nВремя: {time}'
                   f'\n=============================================\n')
