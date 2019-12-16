import telebot

bot = telebot.TeleBot("990108992:AAG1kxwFJpgcJZVgTlTAxgTVQYEZfjrzYS0")
keyb = telebot.types.ReplyKeyboardMarkup(True)
keyb.row("❗️ Важно ❗")
keyb.row("Тёплые контакты", "Холодные контакты")
keyb.row("Утепление", "Возражения")
keybt = telebot.types.ReplyKeyboardMarkup(True)
keybt.row("1 сообщение")
keybt.row("2 сообщение")
keybt.row("Главное меню")


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте', reply_markup=keyb)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Холодные контакты':
        bot.send_message(message.chat.id, '_')
    elif message.text == 'Тёплые контакты':
        bot.send_message(message.chat.id, '_', reply_markup=keybt)
    elif message.text == '❗️Важно❗️':
        bot.send_message(message.chat.id, 'Ребята добро пожаловать в раздел “Рекрутинг искусство приглашения”!!!')
        bot.send_message(message.chat.id, 'Прежде чем приглашать своих знакомых или не '
                                          'знакомых ознакомьтесь с этим разделом:')
        bot.send_message(message.chat.id, '1) Прочтите книгу “Работа с Возражениями” \n'
                                          '2) Посмотрите вебинары, посещайте текущие вебинары. '
                                          'https://www.youtube.com/playlist?list=PL7dKispi5SZ2FsIrWKentQ-h8LuD0Tg8b \n'
                                          '3) Выберите свои методы рекрутинга, составьте план действий, '
                                          'постоянно будьте на связи со спонсором. \n'
                                          '4) Используйте активный и пассивный рекрутинг.')
        bot.send_message(message.chat.id, 'Для успешного старта количество личных регистраций (мин):\n'
                                          '0-3% - 3 рег.        3-6% - 6 рег       6-9% - 9 рег        '
                                          '9-12% - 12 рег       12-18% - 18 рег       18-22% - 22 рег.')
        bot.send_message(message.chat.id, 'Вы встретите тысячи возражений на пути к цели… Важно одеть «бронежилет». \n'
                                          '"Бронежилет" это умение отвечать на возражения, понимать, что это нормально.'
                                          '\nЗачем? \nВы четко знаете свою цель в бизнесе и возражения и глупости от '
                                          'кандидатов не должны Вас сбивать с нее! \nВы - человек с умом и готовой '
                                          'почвой в голове для достижения и открытия новых возможностей, но не все люди'
                                          ' такие... ПОЙМИТЕ и примите это!  Вы с опытом все больше и больше будете это'
                                          ' осознавать.\nНаша работа учиться работать с возражениями, уметь донести до '
                                          'человека истинную СУТЬ бизнеса.')
        bot.send_message(message.chat.id, 'Если Вы общаетесь с людьми, но "НИКОМУ НИЧЕГО НЕ НАДО" - тут 2 варианта - '
                                          'либо у человека не готова "Почва" к новым открытиям, либо у него есть мозг, '
                                          'но он не умеет им пользоваться, либо Вы не научились преподносить информацию'
                                          '.\nЧто делать в этих случаях? \n1. Перебирать людей \n2. Обучаться и '
                                          'оттачивать навыки!')
        bot.send_message(message.chat.id, 'До Вас это делали, делают и будут делать миллионы людей в мире, получая в '
                                          'итоге реализацию своих мечт. И Вы, ничем их не хуже, много практикуясь с '
                                          'каждым днем будете иметь все больше и больше успехов! ')
    elif message.text == '1 сообщение':
        bot.send_message(message.chat.id, 'Имя, привет 😊, ты, наверное, уже знаешь, что я сотрудничаю с компанией '
                                          'Орифлейм. На моей страничке много упоминаний об этом 😅 \nЯ раньше не верила'
                                          ', что здесь можно зарабатывать большие деньги, а теперь моё мнение '
                                          'изменилось. Хочешь узнать подробнее, чем я занимаюсь? ')
        bot.send_message(message.chat.id, 'Имя, привет! Сколько лет, сколько зим 😄. Шикарно выглядишь. Искала тебя '
                                          'целенаправленно, так как развиваю сейчас свой бизнес и хотела бы чтобы рядом'
                                          ' были только знакомые и надёжные люди. Хочешь узнать подробности? 😁 ')
        bot.send_message(message.chat.id, 'Имя, привет 😉. Пишу тебе, так как считаю, что ты серьёзный человек - '
                                          'сможешь оценить моё предложение. Заключается оно в развитии своего бизнеса '
                                          'на интернет площадках. Интересно это направление? Рассказать подробнее? ')
        bot.send_message(message.chat.id, 'Имя, привет! Я к тебе с предложением. Давно искала для себя варианты '
                                          'заработать столько денег, чтобы хватало и пожить, и отдохнуть. Вот наконец '
                                          'нашла и хочу тебе тоже рассказать об этой возможности. Нужны деньги?')
        bot.send_message(message.chat.id, 'Привет, Имя. А я сейчас в интернете работаю) Развиваю свой бизнес. Интернет-'
                                          'магазин товаров повседневного спроса (шампуни, мыло, зуб.паста, косметика и '
                                          'др.) График свободный, работа удаленная. Мне как раз нужен партнер) Тебе '
                                          'нужен доп. доход? ')
        bot.send_message(message.chat.id, 'Привет, Имя, дополнительный доход рассматриваешь? График свободный, удаленно'
                                          ', официально) ')
        bot.send_message(message.chat.id, 'Привет, Имя, я по делу). Есть интересное предложение по работе, рассматрива'
                                          'ешь варианты? Работать в интернете, так что легко можно совмещать. Давай я '
                                          'свяжу тебя с менеджером, он расскажет, что и как. Когда тебе удобно? ')
        bot.send_message(message.chat.id, 'Имя, привет)) я присоединилась к бизнес-команде "Прорыв".  Может, слышала? '
                                          'Давно хотела свое дело начать. Искала-искала себя и вот оно))))  \nУ нас, '
                                          'кстати, много девчонок с маленькими детками, зарабатывают удаленно. Мы пока '
                                          'преимущественно по знакомству зовем. Рассказать тебе о проекте? ')
    elif message.text == '2 сообщение':
        bot.send_message(message.chat.id, 'Отлично! Когда тебе удобно созвониться, мой директор - человек, который уже '
                                          'получает хорошие доходы, я с ней/ним знаком лично, она тебе расскажет, что и'
                                          ' как нужно делать, когда удобнее? ')
        bot.send_message(message.chat.id, 'Меня сюда позвала моя знакомая, предложила доход. Фишка в том, что можно раб'
                                          'отать в любое свободное время. Фактически нужен только смартфон и интернет. '
                                          'Всему обучают! Давай я тебя с ней познакомлю, она как-раз нас всех обучает и'
                                          ' все тебе расскажет голосом? А ты мне потом скажешь зацепила тебя идея или'
                                          ' нет! ')
        bot.send_message(message.chat.id, 'Знаешь, у нас в коллективе все роли и обязанности распределены, я оповещаю '
                                          'людей о вакансиях, директор проводит собеседования, менеджеры предоставляют '
                                          'подробную информацию и т.п.')
        bot.send_message(message.chat.id, 'Я занимаюсь своим делом) Короче, я свяжу тебя с менеджером, он тебе все '
                                          'объяснит, ок?')
        bot.send_message(message.chat.id, 'Если не удобно созвониться, то мы можем создать чат на троих и там будет вся'
                                          ' информация. Как удобнее? ')
        bot.send_message(message.chat.id, 'Хорошо, Маш) давай я добавлю в наш чат менеджера, который даст всю '
                                          'информацию? Я пока человек новый и могу что-нибудь напутать. ')
    elif message.text == 'Главное меню':
        bot.send_message(message.chat.id, 'Главное меню', reply_markup=keyb)


bot.polling()
