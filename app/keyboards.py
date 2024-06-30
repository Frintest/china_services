from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text="Услуги байера (опт)"),
    KeyboardButton(text="Карго (самовыкуп) - от 5 кг"),
    KeyboardButton(text="Розница"),
]], resize_keyboard=True)

cargo1 = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="Да", callback_data="cargo/1/yes"),
    InlineKeyboardButton(text="Мне нужна другая услуга", callback_data="cargo/1/another"),  # todo
]])

cargo2 = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="Какие доп издержки?", callback_data="cargo/2/costs"),
]])

cargo3 = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="Да", callback_data="cargo/3/yes"),
    InlineKeyboardButton(text="Нет", callback_data="cargo/3/no"),
]])

cargo4 = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="Да", callback_data="cargo/4/yes"),
    InlineKeyboardButton(text="Нет", callback_data="cargo/4/no"),
]])

cargo5 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Делаем обрешетку", callback_data="cargo/5/box"),
        InlineKeyboardButton(text="Делаем доп. скотч", callback_data="cargo/5/scotch"),
    ],
    [
        InlineKeyboardButton(text="Не делаем доп. упаковку", callback_data="cargo/5/null"),
    ]
])

cargo6 = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="Я не уверен, помогите!", callback_data="cargo/6/help"),
]])

retail1 = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="Продолжаем", callback_data="retail/1/countinue"),
]])

retail2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Рассчитать стоимость товара", callback_data="retail/2/price")],
    [InlineKeyboardButton(text="Рассчитать доставку", callback_data="retail/2/delivery")]
])

retail3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Рассчитать доставку", callback_data="retail/3/delivery")],
    [InlineKeyboardButton(text="Я просчитал(а) стоимость товара и доставки и готов(а) делать заказ",
                          callback_data="retail/3/all")]
])

retail4 = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="КАК ПРИСЛАТЬ ССЫЛКУ?", callback_data="retail/4/link"),
]])

