import telebot
import constants

TOKEN = '469246545:AAGzBxtH7ovEEzwWnyvrPkLe8atMKDKO3go'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Как тебя зовут, сектант?')
    bot.register_next_step_handler(sent, hello)

def hello(message):
	bot.send_message(message.chat.id,
	'Привет, {name}. Рад тебя видеть!'.format(name=message.text))
	
@bot.message_handler(commands=['teacher'])
def start(message):
	sent = bot.send_message(message.chat.id, 'Напиши мне имя этой псины!')
	bot.register_next_step_handler(sent, teacher)
	
def teacher(message):
	bot.send_message(message.chat.id,
	'{teacher} <----Сосёт хуи как твоя мамаша!'.format(teacher=message.text))
	
@bot.message_handler(commands=['manka'])
def start(message):
	sent = bot.send_message(message.chat.id,'Фу бля, рот помой! Весь в ман..ой, в говне!')
	
@bot.message_handler(commands=['euro'])
def start(message):
	sent = bot.send_message(message.chat.id, 'heir nen euro! https://goo.gl/SCi9kb')
	
@bot.message_handler(commands=['mq'])
def start(message):
	sent = bot.send_message(message.chat.id, 'Кто?')
	bot.register_next_step_handler(sent, mamka)
	
def mamka(message):
	bot.send_message(message.chat.id,
	'{mamka} - ниже твоя мамка! https://goo.gl/6Zp5U9'.format(mamka=message.text))

@bot.message_handler(commands=['ghost'])
def start(message):
	sent = bot.send_message(message.chat.id,'@GhOs1T, ты обосрался! https://goo.gl/sg1WJr')	
	
@bot.message_handler(commands=['foma'])
def start(message):
	sent = bot.send_message(message.chat.id,'@d3fau17, я нашёл применение твоему анусу https://goo.gl/8EJ8j8')

@bot.message_handler(commands=['aa'])
def start(message):
	sent = bot.send_message(message.chat.id,'АЛЛАХ АКБАР! https://gph.is/2d7X42q')

@bot.message_handler(commands=['soap'])
def start(message):
	sent = bot.send_message(message.chat.id,'Эй, новичок! Подними мыло! https://imgur.com/gallery/2NESQ')

@bot.message_handler(commands=['trig'])
def start(message):
	sent = bot.send_message(message.chat.id,'УУУУУУ ЖОПА ГОРИИИИТ!!!! https://imgur.com/gallery/kYpzMGs ')

bot.polling()
