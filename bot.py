import telebot as telebot

bot = telebot.TeleBot("1501412197:AAHzd30QMMu2UQ5GP2NMbCWurH9ryHLnTD4")
keyM = telebot.types.ReplyKeyboardMarkup(row_width=2)
keyM.row('Презентация')
keyM.row('Алгоритм действий')
keyM.row('Текст объявлений',  'Приглашение знакомых')
keyM.row('Текст голосовых',  'Чат на 3-их')
keyM.row('Переписка с незнакомцами',  'Инстаграмм')
keyM.row('Дожималки',  'Возражения')
keyM.row('Дисконт')

key1 = telebot.types.ReplyKeyboardMarkup(row_width=2)
key1.row('После добавления в друзья')
key1.row('Способ "Визитка"')
key1.row('Способ "Пост-рекомендация"')
key1.row('Назад')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, это /start',  reply_markup=keyM)

@bot.message_handler(content_types=['text'])
def olo_message(message):
    if message.text == 'Презентация':
        bot.send_message(message.chat.id, 'Раздел "Презентация"')
    if message.text == 'Алгоритм действий':
        bot.send_message(message.chat.id, 'Раздел "Алгоритм действий"')
    if message.text == 'Текст объявлений':
        bot.send_message(message.chat.id, 'Раздел "Текст объявлений"')
    if message.text == 'Приглашение знакомых':
        bot.send_message(message.chat.id, 'Раздел "Приглашение знакомых"')
    if message.text == 'Текст голосовых':
        bot.send_message(message.chat.id, 'Раздел "Текст голосовых"')
    if message.text == 'Чат на 3-их':
        bot.send_message(message.chat.id, 'Раздел "Чат на 3-их"')
    if message.text == 'Переписка с незнакомцами':
        bot.send_message(message.chat.id, 'Раздел "Переписка с незнакомцами"')
    if message.text == 'Инстаграмм':
        bot.send_message(message.chat.id, 'Раздел "Инстаграмм"',  reply_markup=key1)
    if message.text == 'Дожималки':
        bot.send_message(message.chat.id, 'Раздел "Дожималки"')
    if message.text == 'Возражения':
        bot.send_message(message.chat.id, 'Раздел "Возражения"')
    if message.text == 'Дисконт':
        bot.send_message(message.chat.id, 'Раздел "Дисконт"')
    if message.text == 'После добавления в друзья':
        bot.send_message(message.chat.id, 'Раздел "После добавления в друзья"')
    if message.text == 'Способ "Визитка"':
        bot.send_message(message.chat.id, 'Раздел "Способ "Визитка"')
    if message.text == 'Способ "Пост-рекомендация"':
        bot.send_message(message.chat.id, 'Раздел "Способ "Пост-рекомендация"')
    if message.text == 'Назад':
        bot.send_message(message.chat.id, 'Назад',  reply_markup=keyM)

bot.polling()
