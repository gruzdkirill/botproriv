import telebot

bot = telebot.TeleBot("1501412197:AAHzd30QMMu2UQ5GP2NMbCWurH9ryHLnTD4")

@bot.route('/start')
def start_message(message):
    bot.send_message(message['chat']['id'], 'Привет, это /start')

@bot.route('Оло')
def olo_message(message):
    bot.send_message(message['chat']['id'], 'Привет, ты написал мне ' + message['text'])

bot.config['api_key'] = '1501412197:AAHzd30QMMu2UQ5GP2NMbCWurH9ryHLnTD4'
bot.poll()
