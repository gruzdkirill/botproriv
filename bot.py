import telebot
from telebot import types

bot = telebot.TeleBot("1501412197:AAHzd30QMMu2UQ5GP2NMbCWurH9ryHLnTD4")
key_M =types.ReplyKeyboardMarkup(True)
key_M.row('Привет',  'Пока',  'Оло')

@bot.route('/start')
def start_message(message):
    bot.send_message(message['chat']['id'], 'Привет, это /start',  reply_markup=key_M)

@bot.route('Оло')
def OLO_message(message):
    bot.send_message(message['chat']['id'], 'Привет, ты написал мне ' + message['text'])

bot.config['api_key'] = '1501412197:AAHzd30QMMu2UQ5GP2NMbCWurH9ryHLnTD4'
bot.poll()
