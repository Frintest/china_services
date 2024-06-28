import telebot
from telebot import types
import config
from services.navigation import services_nav
from services.buyer.index import buyer
from services.cargo.index import cargo

bot = telebot.TeleBot(config.API_TOKEN)
description = (
    "Привет! Мы предоставляем полный спектр услуг по работе с Китаем. "
    "Этот бот поможет быстро и просто сделать заказ из Китая, просчитать логистику, "
    "а также помочь с другими вопросами. Что тебя интересует?"
)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, description)
    bot.send_message(message.chat.id, '1', reply_markup=services_nav)


@bot.message_handler(content_types="text")
def message_reply(message):
    if message.text == "Услуги байера (опт)":
        text = buyer()
        bot.send_message(message.chat.id, text, parse_mode="HTML")

    elif message.text == "Карго (самовыкуп) - от 5 кг":
        text = cargo()
        bot.send_message(message.chat.id, text, parse_mode="HTML")

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да")
        back_btn = types.KeyboardButton("Мне нужна другая услуга")
        markup.add(btn1, back_btn)
        bot.send_message(message.chat.id, "", reply_markup=markup)


bot.infinity_polling()
