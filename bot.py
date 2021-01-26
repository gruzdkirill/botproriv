import telebot as telebot

bot = telebot.TeleBot("1501412197:AAHzd30QMMu2UQ5GP2NMbCWurH9ryHLnTD4")
keyM = telebot.types.ReplyKeyboardMarkup(row_width=2)
keyM.row('Оло', 'ща')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, это /start',  reply_markup=keyM)

@bot.message_handler(content_types=['text'])
def olo_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне ' + message.text)

bot.polling()
