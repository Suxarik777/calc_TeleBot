from telebot import TeleBot, types
from Token_id import TOKEN_ID

TOKEN = TOKEN_ID

bot = TeleBot(TOKEN)
@bot.message_handler(commands=['complex_number'])
def menu(msg: types.Message):
    bot_mess = 'проверка'
    bot.send_message(chat_id=msg.chat.id, text=bot_mess, parse_mode='html')