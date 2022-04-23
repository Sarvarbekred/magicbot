import telebot
from telebot import types
bot = telebot.TeleBot("5389627105:AAGihACq2sg8ECSCzAWm_CfzfR9NRkwXIZI")

@bot.message_handler(commands=['start'])



def get_text_messages(message):
    b=message.from_user.first_name
    s=message.from_user.username
    print(b)
    print('@'+str(s),'\nStart ni bosdi')
    global keyboard
    keyboard = types.InlineKeyboardMarkup()
    key_ps = types.InlineKeyboardButton(text="📖Kurslar Haqida📖", callback_data='kh')
    keyboard.add(key_ps)
    key_max = types.InlineKeyboardButton(text="🗺Magical Study qayerda joylashgan🗺", callback_data='mj')
    keyboard.add(key_max)
    key_max = types.InlineKeyboardButton(text="👩‍🏫O'qtuvchilar haqida👨‍🏫", callback_data='oh')
    keyboard.add(key_max)
    key_max = types.InlineKeyboardButton(text="💰Kurs narxlari qanday?💰", callback_data='kq')
    keyboard.add(key_max)
    bot.send_message(message.from_user.id, text="O'zingizni qiziqtirgan savolni tanlang", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data=="kh":
    	bot.send_message(call.message.chat.id,"""Bizning o'quv markazimizda 28ta umumiy yo'nalishda o'quv kurslari mavjud\njumladan:\nIngliz tili \nRus tili\nArab tili\nMental arifmetika\nKampyuter savodhonligi\nHamshiralik\nTikuvchilik\nOliy Tort\nO'gil bolalar uchun oshpazlik kursi\nMarketing\nMatematika(ingliz va o'zbek tillarida)\nTikuvchilik\nElita pardachilik\nDieta(nutretologiya)\nAniq Fanlar va ijtimoiy fanlar(7ta kurs)\nKosmetologiya\nModellashtirish(mato va kampyuter bilan)\nOila psixologiyasi\nFizika\nKimyo\n\nBizdan sizga sovg'a yangi loyiha\nMalikalar Maktabi""",reply_markup=keyboard)
    elif call.data=="mj":
    	bot.send_message(call.message.chat.id,"https://maps.google.com/maps?q=40.187661,67.869069&ll=40.187661,67.869069&z=16",reply_markup=keyboard)
    elif call.data=="oh":
    	bot.send_message(call.message.chat.id,"Bizning O'qtuvchilarimiz barchasi oliy ma'lunotl va xalqaro\nsertifikatlarga ega",reply_markup=keyboard)
    elif call.data=="kq":
    	bot.send_message(call.message.chat.id,"Magical Study kurslari narxlari standard:\n150 ming so'mdan 460 ming gacha",reply_markup=keyboard)

print('bot ishlamoqda....')
bot.infinity_polling()