import telebot
from replacement_space import replacement_space
from replacement_space import get_stiker_afte_scrining
from parser import parser

bot = telebot.TeleBot('здесь должен быть токен бота')


# ответ на команду /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAL8j2BRXMX6spQ_r1uWZ6IPH-pRc5tUAAJVAQACMNSdEelRJRHujObYHgQ')
    bot.send_message(message.chat.id, 'Привет!')


# поиск статьи и её вывод в сообщения
@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_sticker(message.chat.id, get_stiker_afte_scrining())
    bot.send_message(message.chat.id, 'Вот что нашел!')
    bot.send_message(message.chat.id, parser(replacement_space(message.text))[0])
    bot.send_message(message.chat.id, parser(replacement_space(message.text))[1])
    bot.send_message(message.chat.id, parser(replacement_space(message.text))[2])
    bot.send_message(message.chat.id, parser(replacement_space(message.text))[3])
    bot.send_message(message.chat.id, 'Мне найти ещё что-нибудь?')

# ожидание сообщения от пользователя
bot.polling()