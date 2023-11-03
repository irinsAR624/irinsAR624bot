#библиотеки, которые загружаем из вне
import telebot
TOKEN = '6602636866:AAHKp9Wm-86YA9it0UsaT2CTVirpnA3Qlvg'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🧡 Совет дня")
	item2 = types.KeyboardButton("😋 Погода в Штате Кентукки")
	item3 = types.KeyboardButton(" — Пингвинам можно, а мне что, нельзя да?")
	markup.add(item1, item2, item3)

	bot.send_message(message.chat.id, "Привет тебе от Мелмана, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🧡 Совет дня':
			bot.send_message(message.chat.id,'Ты можешь всё!Главное верь в себя')
		elif message.text == '😋 Погода в Штате Кентукки':
			bot.send_message(message.chat.id, 'Погода в Кентукки на сегодня По ощущениям +12°C Ясно, без осадков')
		elif message.text == '— Пингвинам можно, а мне что, нельзя да?':
			bot.send_message(message.chat.id, '— Пингвины, они же психи!')
		else:
			bot.send_message(message.chat.id, 'Не знаю что ответить😢')
bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods
