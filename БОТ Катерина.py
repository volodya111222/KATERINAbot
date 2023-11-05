import telebot
from telebot import types

bot = telebot.TeleBot('6067582776:AAG976rQM2tmpxW17x0VkdQCa89KAFulqvk')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('ГЕО')
    btn2 = types.KeyboardButton('ЭЛЕКТРО')
    btn3 = types.KeyboardButton('ГИДРО')
    btn4 = types.KeyboardButton('ДЕНДРО')
    btn5 = types.KeyboardButton('КРИО')
    btn6 = types.KeyboardButton('ПИРО')
    btn7 = types.KeyboardButton('АНЕМО')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

    bot.send_message(message.from_user.id, 'Привет! Меня зовут Катерина и я помогу тебе c материалами для прокачки персонажей!', reply_markup=markup)
    bot.register_next_step_handler(message, txt)



@bot.message_handler(content_types=['text'])
def txt(message):
    markup = types.InlineKeyboardMarkup()
    markup2 = types.InlineKeyboardMarkup()
    markup3 = types.InlineKeyboardMarkup()
    markup4 = types.InlineKeyboardMarkup()
    markup5 = types.InlineKeyboardMarkup()
    markup6 = types.InlineKeyboardMarkup()
    markup2 = types.InlineKeyboardMarkup()

    #гео
    pers1 = types.InlineKeyboardButton(text='Чжун Ли', callback_data='send_photo')
    pers2 = types.InlineKeyboardButton(text='Нин Гуан', callback_data='send_photo2')
    pers3 = types.InlineKeyboardButton(text='Альбедо', callback_data='send_photo3')
    pers4 = types.InlineKeyboardButton(text='Ноэлль', callback_data='send_photo4')
    pers5 = types.InlineKeyboardButton(text='Итто', callback_data='send_photo5')
    pers6 = types.InlineKeyboardButton(text='Горо', callback_data='send_photo6')
    pers7 = types.InlineKeyboardButton(text='Юнь Цзинь', callback_data='send_photo7')
    #электро
    pers8 = types.InlineKeyboardButton(text='Ке Цин', callback_data='send_photo8')
    pers9 = types.InlineKeyboardButton(text='Яэ Мико',  callback_data='send_photo9')
    pers10 = types.InlineKeyboardButton(text='Райден', callback_data='send_photo10')
    pers11 = types.InlineKeyboardButton(text='Бэй Доу', callback_data='send_photo11')
    pers12 = types.InlineKeyboardButton(text='Дори', callback_data='send_photo12')
    pers13 = types.InlineKeyboardButton(text='Куки Синобу', callback_data='send_photo13')
    pers14 = types.InlineKeyboardButton(text='Лиза', callback_data='send_photo14')
    pers15 = types.InlineKeyboardButton(text='Рейзор', callback_data='send_photo15')
    pers16 = types.InlineKeyboardButton(text='Сайно', callback_data='send_photo16')
    pers17 = types.InlineKeyboardButton(text='Сара', callback_data='send_photo17')
    pers18 = types.InlineKeyboardButton(text='Фишль', callback_data='send_photo18')
    #гидро
    pers19 = types.InlineKeyboardButton(text='Аято', callback_data='send_photo19')
    pers20 = types.InlineKeyboardButton(text='Барбара', callback_data='send_photo20')
    pers21 = types.InlineKeyboardButton(text='Е Лань', callback_data='send_photo21')
    pers22 = types.InlineKeyboardButton(text='Мона', callback_data='send_photo22')
    pers23 = types.InlineKeyboardButton(text='Кандакия', callback_data='send_photo23')
    pers24 = types.InlineKeyboardButton(text='Кокоми', callback_data='send_photo24')
    pers25 = types.InlineKeyboardButton(text='Нилу', callback_data='send_photo25')
    pers26 = types.InlineKeyboardButton(text='Син Цю', callback_data='send_photo26')
    pers27 = types.InlineKeyboardButton(text='Тарталья', callback_data='send_photo27')
    #дендро
    pers28 = types.InlineKeyboardButton(text='Аль Хайтам', callback_data='send_photo28')
    pers29 = types.InlineKeyboardButton(text='Бай Чжу', callback_data='send_photo29')
    pers30 = types.InlineKeyboardButton(text='Кавех', callback_data='send_photo30')
    pers31 = types.InlineKeyboardButton(text='Кирара', callback_data='send_photo31')
    pers32 = types.InlineKeyboardButton(text='Коллеи', callback_data='send_photo32')
    pers33 = types.InlineKeyboardButton(text='Нахида', callback_data='send_photo33')
    pers34 = types.InlineKeyboardButton(text='Тигнари', callback_data='send_photo34')
    pers35 = types.InlineKeyboardButton(text='Яо Яо', callback_data='send_photo35')
    #крио
    pers36 = types.InlineKeyboardButton(text='Аяка', callback_data='send_photo36')
    pers37 = types.InlineKeyboardButton(text='Гань Юй', callback_data='send_photo37')
    pers38 = types.InlineKeyboardButton(text='Диона', callback_data='send_photo38')
    pers39 = types.InlineKeyboardButton(text='Кейа', callback_data='send_photo39')
    pers40 = types.InlineKeyboardButton(text='Лайла', callback_data='send_photo40')
    pers41 = types.InlineKeyboardButton(text='Мика', callback_data='send_photo41')
    pers42 = types.InlineKeyboardButton(text='Розария', callback_data='send_photo42')
    pers43 = types.InlineKeyboardButton(text='Ци Ци', callback_data='send_photo43')
    pers44 = types.InlineKeyboardButton(text='Чунь Юнь', callback_data='send_photo44')
    pers45 = types.InlineKeyboardButton(text='Шень Хе', callback_data='send_photo45')
    pers46 = types.InlineKeyboardButton(text='Элой', callback_data='send_photo46')
    pers47 = types.InlineKeyboardButton(text='Эола', callback_data='send_photo47')
    #пиро
    pers48 = types.InlineKeyboardButton(text='Ёимия', callback_data='send_photo48')
    pers49 = types.InlineKeyboardButton(text='Беннет', callback_data='send_photo49')
    pers50 = types.InlineKeyboardButton(text='Дилюк', callback_data='send_photo50')
    pers51 = types.InlineKeyboardButton(text='Дэхья', callback_data='send_photo51')
    pers52 = types.InlineKeyboardButton(text='Кли', callback_data='send_photo52')
    pers53 = types.InlineKeyboardButton(text='Синь Янь', callback_data='send_photo53')
    pers54 = types.InlineKeyboardButton(text='Сян Лин', callback_data='send_photo54')
    pers55 = types.InlineKeyboardButton(text='Тома', callback_data='send_photo55')
    pers56 = types.InlineKeyboardButton(text='Ху Тао', callback_data='send_photo56')
    pers57 = types.InlineKeyboardButton(text='Эмбер', callback_data='send_photo57')
    pers58 = types.InlineKeyboardButton(text='Янь Фей', callback_data='send_photo58')
    #анемо
    pers59 = types.InlineKeyboardButton(text='Венти', callback_data='send_photo59')
    pers60 = types.InlineKeyboardButton(text='Джинн', callback_data='send_photo60')
    pers61 = types.InlineKeyboardButton(text='Кадзуха', callback_data='send_photo61')
    pers62 = types.InlineKeyboardButton(text='Сахароза', callback_data='send_photo62')
    pers63 = types.InlineKeyboardButton(text='Саю', callback_data='send_photo63')
    pers64 = types.InlineKeyboardButton(text='Хэйдзо', callback_data='send_photo64')
    pers65 = types.InlineKeyboardButton(text='Странник', callback_data='send_photo765')
    pers66 = types.InlineKeyboardButton(text='Сяо', callback_data='send_photo66')
    pers67 = types.InlineKeyboardButton(text='Фарузан', callback_data='send_photo67')


    markup.add(pers1, pers2, pers3, pers4, pers5, pers6, pers7)

    if message.text == 'ГЕО':
        bot.send_message(message.chat.id, "выбери персонажа", reply_markup=markup)

    elif message.text == 'ЭЛЕКТРО':
        markup2.add(pers8, pers9, pers10, pers11, pers12, pers13, pers14, pers15, pers16, pers17, pers18)
        bot.send_message(message.chat.id, "выбери персонажа", reply_markup=markup2)

    elif message.text == 'ГИДРО':
        markup3.add(pers19, pers20, pers21, pers22, pers23, pers24, pers25, pers26, pers27)
        bot.send_message(message.chat.id, 'выбери персонажа', reply_markup=markup3)

    elif message.text == 'ДЕНДРО':
        markup4.add(pers28, pers29, pers30, pers31, pers32, pers33, pers34, pers35)
        bot.send_message(message.chat.id, 'выбери персонажа', reply_markup=markup4)

    elif message.text == 'КРИО':
        markup5.add(pers36, pers37, pers38, pers39, pers40, pers41, pers42, pers43, pers44, pers45, pers46, pers47)
        bot.send_message(message.chat.id, 'выбери персонажа', reply_markup=markup5)

    elif message.text == 'ПИРО':
        markup6.add(pers48, pers49, pers50, pers51, pers52, pers53, pers54, pers55, pers56, pers57, pers58)
        bot.send_message(message.chat.id, 'выбери персонажа', reply_markup=markup6)

    elif message.text == 'АНЕМО':
        markup6.add(pers59, pers60, pers61, pers62, pers63, pers64, pers65, pers66, pers67)
        bot.send_message(message.chat.id, 'выбери персонажа', reply_markup=markup6)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
#гео

    if call.data == 'send_photo':
        file = open('чжун ли.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file)

    elif call.data == 'send_photo2':
        file2 = open('нингуан.jpg.', 'rb')
        bot.send_photo(call.message.chat.id, file2)

    elif call.data == 'send_photo3':
        file3 = open('албюедо.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file3)

    elif call.data == 'send_photo4':
        file4 = open('ноэль.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file4)

    elif call.data == 'send_photo5':
        file5 = open('итто.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file5)

    elif call.data == 'send_photo6':
        file6 = open('ujhj.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file6)

    elif call.data == 'send_photo7':
        file7 = open('юнь цзынь.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file7)
#электро

    elif call.data == 'send_photo8':
        file8 = open('кека.png', 'rb')
        bot.send_photo(call.message.chat.id, file8)

    elif call.data == 'send_photo9':
        file9 = open('яэ.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file9)

    elif call.data == 'send_photo10':
        file10 = open('эи.png', 'rb')
        bot.send_photo(call.message.chat.id, file10)

    elif call.data == 'send_photo11':
        file11 = open('бэйдоу.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file11)

    elif call.data == 'send_photo12':
        file12 = open('дори.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file12)

    elif call.data == 'send_photo13':
        file13 = open('куки.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file13)

    elif call.data == 'send_photo14':
        file14 = open('лиза.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file14)

    elif call.data == 'send_photo15':
        file15 = open('рейзор.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file15)

    elif call.data == 'send_photo16':
        file16 = open('сайно.png', 'rb')
        bot.send_photo(call.message.chat.id, file16)

    elif call.data == 'send_photo17':
        file17 = open('сара.png', 'rb')
        bot.send_photo(call.message.chat.id, file17)

    elif call.data == 'send_photo18':
        file18 = open('фишль.png', 'rb')
        bot.send_photo(call.message.chat.id, file18)
#гидро

    elif call.data == 'send_photo19':
        file19 = open('аято.jpeg', 'rb')
        bot.send_photo(call.message.chat.id, file19)

    elif call.data == 'send_photo20':
        file20 = open('барбара.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file20)

    elif call.data == 'send_photo21':
        file21 = open('елань.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file21)

    elif call.data == 'send_photo22':
        file22 = open('мона.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file22)

    elif call.data == 'send_photo23':
        file23 = open('кандакия.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file23)

    elif call.data == 'send_photo24':
        file24 = open('кокоми.png', 'rb')
        bot.send_photo(call.message.chat.id, file24)

    elif call.data == 'send_photo25':
        file25 = open('нилу.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file25)

    elif call.data == 'send_photo26':
        file26 = open('син цю.png', 'rb')
        bot.send_photo(call.message.chat.id, file26)

    elif call.data == 'send_photo27':
        file27 = open('торт.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file27)

#дендро

    elif call.data == 'send_photo28':
        file28 = open('хайтам.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file28)

    elif call.data == 'send_photo29':
        file29 = open('байчжу.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file29)

    elif call.data == 'send_photo30':
        file30 = open('кавех.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file30)

    elif call.data == 'send_photo31':
        file31 = open('кирара.png', 'rb')
        bot.send_photo(call.message.chat.id, file31)

    elif call.data == 'send_photo32':
        file32 = open('колеи.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file32)

    elif call.data == 'send_photo33':
        file33 = open('нахида.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file33)

    elif call.data == 'send_photo34':
        file34 = open('тигнари.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file34)

    elif call.data == 'send_photo35':
        file35 = open('яояо.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file35)

#крио

    elif call.data == 'send_photo36':
        file36 = open('аяка.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file36)

    elif call.data == 'send_photo37':
        file37 = open('коза.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file37)

    elif call.data == 'send_photo38':
        file38 = open('диона.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file38)

    elif call.data == 'send_photo39':
        file39 = open('кэйа.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file39)

    elif call.data == 'send_photo40':
        file40 = open('лайла.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file40)

    elif call.data == 'send_photo41':
        file41 = open('мика.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file41)

    elif call.data == 'send_photo42':
        file42 = open('розария.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file42)

    elif call.data == 'send_photo43':
        file43 = open('чича.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file43)

    elif call.data == 'send_photo44':
        file44 = open('чугун.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file44)

    elif call.data == 'send_photo45':
        file45 = open('шеньхэ.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file45)

    elif call.data == 'send_photo46':
        file46 = open('элой.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file46)

    elif call.data == 'send_photo47':
        file47 = open('эола.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file47)

#пиро

    elif call.data == 'send_photo48':
        file48 = open('ёми.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file48)

    elif call.data == 'send_photo49':
        file49 = open('бени.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file49)

    elif call.data == 'send_photo50':
        file50 = open('дюлюк.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file50)

    elif call.data == 'send_photo51':
        file51 = open('дэхья.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file51)

    elif call.data == 'send_photo52':
        file52 = open('кли.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file52)

    elif call.data == 'send_photo53':
        file53 = open('синьянь.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file53)

    elif call.data == 'send_photo54':
        file54 = open('сянлин.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file54)

    elif call.data == 'send_photo55':
        file55 = open('тома.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file55)

    elif call.data == 'send_photo56':
        file56 = open('тава.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file56)

    elif call.data == 'send_photo57':
        file57 = open('эмбер.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file57)

#анемо

    elif call.data == 'send_photo58':
        file58 = open('яньфей.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file58)

    elif call.data == 'send_photo59':
        file59 = open('венти.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file59)

    elif call.data == 'send_photo60':
        file60 = open('джин.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file60)

    elif call.data == 'send_photo61':
        file61 = open('казах.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file61)

    elif call.data == 'send_photo62':
        file62 = open('сахароза.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file62)

    elif call.data == 'send_photo63':
        file63 = open('саю.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file63)

    elif call.data == 'send_photo64':
        file64 = open('хэйдзо.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file64)

    elif call.data == 'send_photo65':
        file65 = open('скара.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file65)

    elif call.data == 'send_photo66':
        file66 = open('сяо.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file66)

    elif call.data == 'send_photo67':
        file67 = open('фапузан.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file67)


bot.polling(none_stop=True, interval=0)