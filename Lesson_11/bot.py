from config import TOKEN
from telebot import TeleBot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import json
import random

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = KeyboardButton('Привет', request_contact=True)
    button2 = KeyboardButton('Хай', request_location=True)
    button3 = KeyboardButton('Салют')

    kb.add(button1, button2, button3)

    bot.send_message(
        message.chat.id,
        'Hello!',
        reply_markup=kb
    )


@bot.message_handler(func=lambda m: m.text in {'Привет', 'Хай', 'Салют'})
def handle_hello(message):
    greetings = ['Hola', 'Hello', 'Hi', 'Здравствуй']
    kb = InlineKeyboardMarkup()

    json_data = json.dumps({
        'tag': 'Hi',
        'id': '1234'
    })
    print(json_data)
    button1 = InlineKeyboardButton('Привет', callback_data=json_data)

    json_data = json.dumps(
        {
            'tag': 'Bye',
            'id': '5678'
        }
    )
    button2 = InlineKeyboardButton('Пока', callback_data=json_data)
    kb.add(button1, button2)
    bot.send_message(
        message.chat.id,
        random.choice(greetings),
        reply_markup=kb
    )


@bot.message_handler(content_types=['text'])
def handle_text(message):
    text = f'Ты написал мне следующее: {message.text}'
    bot.send_message(
        message.chat.id,
        text
    )


@bot.message_handler(commands=['whoami'])
def handle_whoami(message):
    user_info = f'Твоё имя: {message.from_user.first_name}\n' \
                f'Никнейм: @{message.from_user.username}\nid: {message.from_user.id}'
    bot.send_message(message.chat.id, user_info)


@bot.callback_query_handler(func=lambda c: json.loads(c.data).get('tag') == 'Hi')
def handle_inline(call):
    bot.send_message(
        call.message.chat.id,
        'HI!'
    )


@bot.callback_query_handler(func=lambda c: json.loads(c.data).get('tag') == 'Bye')
def handle_inline(call):
    bot.send_message(
        call.message.chat.id,
        'BYE!'
    )

# import time
# for i in range(10):
#     bot.send_message(392635953, 'Привет')
#     time.sleep(0.5)

bot.polling()