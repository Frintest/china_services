from telebot import types

btn1 = types.KeyboardButton("Розница", )
btn2 = types.KeyboardButton("Карго (самовыкуп) - от 5 кг")
btn3 = types.KeyboardButton("Услуги байера (опт)")
btn4 = types.KeyboardButton("Инспекция товара / производства в Китае")
btn5 = types.KeyboardButton("Организация бизнес поездки в Китай под ключ")
btn6 = types.KeyboardButton("Об авторе",)
btn7 = types.KeyboardButton("Денежные переводы в Китай")
btn8 = types.KeyboardButton("Официальные поставки")
btn9 = types.KeyboardButton("Услуги переводчика / сопровождение в поездке в Китай")

services_nav = types.ReplyKeyboardMarkup(resize_keyboard=True)
services_nav.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
# services_nav.add(btn1, btn2, btn3)
