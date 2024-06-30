from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import app.keyboards as keyboards

from services.buyer.index import buyer

router = Router()


class Cargo(StatesGroup):
    price = State()
    price_per_kilogram = State()
    package = State()  # todo


class Help(StatesGroup):
    text = State()
    contact = State()


class Retail(StatesGroup):
    expected_price = State()
    calc_price = State()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        f"Привет {message.from_user.first_name}! Мы предоставляем полный спектр услуг по работе с Китаем. "
        "Этот бот поможет быстро и просто сделать заказ из Китая, просчитать логистику, "
        "а также помочь с другими вопросами. Что тебя интересует?", reply_markup=keyboards.main
    )


@router.message(F.text == "Розница")
async def route(message: Message):
    text = (
        'В этом разделе можно оформить небольшие посылки.\n\n🚫 <strong>Важно!!!</strong> 🚫\n'
        'Небольшими посылками НЕ ОТПРАВЛЯЕМ:\n'
        '<b>-</b> Хрупкие, легко-воспламеняющиеся грузы\n'
        '<b>-</b> 📱 Электронику\n'
        '<b>-</b> 🧴 Порошки\n'
        '<b>-</b> 🧪 Химию\n'
        '<b>-</b> 💧 Жидкости\n\n'
        'Электронику можно отправить через разделы <strong>"Карго (самовыкуп) - от 5 кг"</strong> '
        'или <strong>"Услуги байера (опт)"</strong>.\n'
        'Минимальная сумма заказа - всего 1000 р.'
    )
    await message.answer(text, reply_markup=keyboards.retail1, parse_mode="html")


@router.callback_query(F.data == "retail/1/countinue")
async def route(callback: CallbackQuery):
    text = (
        "Стоимость заказа рассчитывается по формуле: <b>Стоимость товара + доставка</b>.\n\n"
        "Стоимость доставки из Китая 600 руб за 1 кг.\nПример: вес шарфа 150 грамм значит:  0,150 * 600 = 90 руб. "
        "за шарф.\n\n<strong>Важно</strong> ☝🏻 🛑\nФинально корректные данные по весу мы получаем когда "
        "товар приходит ко мне: я его взвешиваю и сообщаю сколько к оплате за вес Доставка по РФ оплачивается "
        "отдельно по тарифам СДЕК."
    )
    await callback.message.answer(text, reply_markup=keyboards.retail2, parse_mode="html")


@router.callback_query(F.data == "retail/2/price")
async def route(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Retail.expected_price)
    text = (
        '<b>Введите сумму планируемой покупки (в юанях)</b>.\nПример: стоимость товара 150 ¥, значит вам нужно '
        'отправить сообщение "150". Далее бот рассчитает конечную стоимость с % 🙌'
    )
    await callback.message.answer(text, parse_mode="html")
    await state.set_state(Retail.expected_price)


@router.message(Retail.expected_price)
async def route(message: Message, state: FSMContext):
    await state.update_data(expected_price=message.text)
    text = f"Стоимость товара <i>(без доставки)</i>: {2222} ₽"
    await message.answer(text, reply_markup=keyboards.retail3, parse_mode="html")


@router.callback_query(F.data == "retail/3/delivery")
async def route(callback: CallbackQuery):
    text = (
        "Стоимость доставки из Китая 600 руб за 1 кг.\nПример: вес шарфа 150 грамм значит:  0,150 * 600 = 90 руб. "
        "за шарф.\n\n<strong>Важно</strong> ☝🏻 🛑\nФинально корректные данные по весу мы получаем когда "
        "товар приходит ко мне: я его взвешиваю и сообщаю сколько к оплате за вес Доставка по РФ оплачивается "
        "отдельно по тарифам СДЕК."
    )
    await callback.message.answer(text, parse_mode="html")


@router.callback_query(F.data == "retail/3/all")
async def route(callback: CallbackQuery):
    text = (
        "Отлично! Заказ уходит в работу после 100% предоплаты на карту.\n\nЧтобы сделать заказ, ответным "
        "сообщением пришли, пожалуйста <b>- ссылку на товар с китайского сайта</b> ИЛИ <b>- ссылку на мой пост с "
        "товаром в инстаграме или тг</b>.\n\nТАКЖЕ не забудь прислать информацию о характеристиках товара к заказу: "
        "<b>ЦВЕТ/РАЗМЕР/КОЛИЧЕСТВО</b>."
    )
    await callback.message.answer(text, reply_markup=keyboards.retail4, parse_mode="html")


@router.callback_query(F.data == "retail/4/link")
async def route(callback: CallbackQuery):
    text = (
        "На каждой китайской площадке есть такая кнопка в карточке товара, жми на нее, выбирай «скрепку» "
        "и отправляй мне 🙌."
    )
    await callback.message.answer(text, parse_mode="html")


@router.callback_query(F.data == "retail/2/delivery")
async def route(callback: CallbackQuery):
    text = (
        "Стоимость доставки из Китая 600 руб за 1 кг.\nПример: вес шарфа 150 грамм значит:  0,150 * 600 = 90 руб. "
        "за шарф.\n\n<strong>Важно</strong> ☝🏻 🛑\nФинально корректные данные по весу мы получаем когда "
        "товар приходит ко мне: я его взвешиваю и сообщаю сколько к оплате за вес Доставка по РФ оплачивается "
        "отдельно по тарифам СДЕК."
    )
    await callback.message.answer(text, parse_mode="html")


@router.message(F.text == "Услуги байера (опт)")
async def route(message: Message):
    text = buyer()
    await message.answer(text, reply_markup=keyboards.main, parse_mode="html")


@router.message(F.text == "Карго (самовыкуп) - от 5 кг")
async def route(message: Message):
    text = (
        "При самовыкупе вы <b>САМОСТОЯТЕЛЬНО</b> покупаете товары у китайских поставщиков или на китайских "
        "маркетплейсах (1688, Made-In-China, taobao, pingduoduo и тд) и организуете доставку груза до склада карго "
        "в г Иу или  Гуанчжоу (на выбор)."
        "\n\nРешение ВСЕХ вопросов с продавцом (почему ваш товар еще не отправлен / еще не доехал /"
        "вернулся обратно к продавцу и тд) лежит полностью на вашей стороне."
        "\n\nСо своей стороны мы отвечаем только за доставку груза из Китая до РФ."
        "\n\n<b>Продолжаем?</b>"
    )
    await message.answer(text, reply_markup=keyboards.cargo1, parse_mode="html")


@router.callback_query(F.data == "cargo/1/yes")
async def route(callback: CallbackQuery):
    text = (
        "Ну что ж, давай рассчитаем стоимость доставки. Тариф зависит от категории товара, "
        "количества килограмм, плотности груза. Также возможны дополнительные издержки"
    )
    await callback.message.answer(text, reply_markup=keyboards.cargo2)


@router.callback_query(F.data == "cargo/2/costs")
async def route(callback: CallbackQuery):
    text = (
        "<b>1.</b> Страховка - 2% от стоимости груза <i>(оформляется по желанию)</i>. Например, если объявленная "
        "вами стоимость 10.000 юаней, то страховка обойдется всего в 200 юаней.\n\n"
        "<b>2.</b> При стоимости груза от $50 до $99 за килограмм, страховка составляет 2.5% от стоимости.\n\n"
        "<b>3.</b> Товар, стоимостью от $100 за килограмм к страхованию не принимается!\n\n"
        "<b>4.</b> Страховка покрывает потерю, кражу, конфискацию груза.\n\n"
        "<b>5.</b> Если ваш товар не застрахован, то стоимость груза не компенсируется.\n\n"
        "<strong>Делаем страховку?</strong>"
    )
    await callback.message.answer(text, reply_markup=keyboards.cargo3, parse_mode="html")


@router.callback_query(F.data == "cargo/3/yes")
async def route(callback: CallbackQuery):
    text = "Известна ли финальная стоимость груза?"
    await callback.message.answer(text, reply_markup=keyboards.cargo4)


@router.callback_query(F.data == "cargo/4/yes")
async def route(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Cargo.price)
    await callback.message.answer("Пожалуйста, напиши, стоимость груза.")


@router.message(Cargo.price)
async def route(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await state.set_state(Cargo.price_per_kilogram)
    await message.answer("Пожалуйста, напиши, примерную стоимость груза на килограмм.")


@router.message(Cargo.price_per_kilogram)
async def route(message: Message, state: FSMContext):
    await state.update_data(price_per_kilogram=message.text)
    await state.set_state(Cargo.price_per_kilogram)

    # data = await state.get_data()  #
    # await state.clear()  #

    text1 = (
        "Обрешетка - 150 юаней за квадратный метр груза. Обрешетка считается от 2 квадратных метров "
        "(то есть ее минимальная стоимость - 300 юаней).\n\n"
        "<b>Обрешетка груза</b> – это метод упаковки, при котором груз закрепляется внутри деревянного каркаса "
        "<i>(обрешетки)</i>, чтобы обеспечить его безопасность во время транспортировки.\nОбрешетка используется "
        "для защиты хрупких, тяжелых или негабаритных грузов от повреждений, воздействий внешней среды "
        "и механических нагрузок.\n\n"
    )
    await message.answer(text1, parse_mode="html")

    text2 = "<b>Скотч</b> - дополнительно заскотчить коробку сверху - 10 юаней / коробка.\n\n"
    await message.answer(text2, parse_mode="html")

    text3 = (
        "Дополнительную упаковку мы делаем только по просьбе клиента.\n\nЕсли от Вас не было просьбы и при "
        "транспортировке ваш груз сломался, помялся, разбился, претензии мы не принимаем.\n\n<b>Что делаем?</b>"
    )
    await message.answer(text3, parse_mode="html", reply_markup=keyboards.cargo5)


@router.callback_query(lambda c: c.data in ["cargo/3/no", "cargo/4/no"])
async def route(callback: CallbackQuery):
    text1 = (
        "Обрешетка - 150 юаней за квадратный метр груза. Обрешетка считается от 2 квадратных метров "
        "(то есть ее минимальная стоимость - 300 юаней).\n\n"
        "<b>Обрешетка груза</b> – это метод упаковки, при котором груз закрепляется внутри деревянного каркаса "
        "<i>(обрешетки)</i>, чтобы обеспечить его безопасность во время транспортировки.\nОбрешетка используется "
        "для защиты хрупких, тяжелых или негабаритных грузов от повреждений, воздействий внешней среды "
        "и механических нагрузок.\n\n"
    )

    await callback.message.answer(text1, parse_mode="html")

    text2 = "<b>Скотч</b> - дополнительно заскотчить коробку сверху - 10 юаней / коробка.\n\n"
    await callback.message.answer(text2, parse_mode="html")

    text3 = (
        "Дополнительную упаковку мы делаем только по просьбе клиента.\n\nЕсли от Вас не было просьбы и при "
        "транспортировке ваш груз сломался, помялся, разбился, претензии мы не принимаем.\n\n<b>Что делаем?</b>"
    )
    await callback.message.answer(text3, parse_mode="html", reply_markup=keyboards.cargo5)


@router.callback_query(lambda c: c.data in ["cargo/5/box", "cargo/5/scotch", "cargo/5/also"])
async def route(callback: CallbackQuery):
    text = (
        "С какой категорией товара работаем?\n\nВнимание!!! товары разных типов смешивать нельзя!\nТовары разных "
        "типов считаются отдельно!\nМы не несем ответственность за сохранность товара, если была указаны "
        "неверная категория или товары из разных категорий были смешаны!"
    )
    await callback.message.answer(text, parse_mode="html")

    categories = [
        {
            "title": "Категория 1",
            "content": "Универсальные товары",
        },
        {
            "title": "Категория 2",
            "content": [
                "Электронные весы 📊",
                "Пылесосы 🧹",
                "Электрические бритвы 🪒",
                "Электрические утюги 🧺",
                "Микроволновые печи 🍲",
                "Электрические духовки и другие электронагревательные приборы 🍞",
                "Фены 💨",
                "Плойки 💇‍♀️",
                "Кулеры для воды 🚰",
                "Веб-камеры 📷",
                "Автоматические диспенсеры для мыла 🧼",
                "Роутеры 📡",
                "Принтеры 🖨️",
                "Wi-Fi роутеры 🌐",
                "Фитнес-браслеты ⌚",
                "Электрические зубные щетки",
                "Дата-кабели 🔌",
                "Зарядные устройства 🔋",
                "Игровые контроллеры 🎮",
                "Игровые приставки 🕹️",
                "Автомобильные зарядные устройства 🚗🔌",
                "ТВ-приставки 📺",
                "Сушилки 🌬️",
                "Электрические точилки для ножей 🔪",
                "Вентиляторы для вытяжки 🌪️",
                "Радиаторы 🔥",
                "Пульты дистанционного управления 🎛️",
                "Массажёры 💆",
                "Мониторы 🖥️",
                "Электрические чайники ☕",
                "Лазерные дальномеры для дома 📏",
                "Термометры 🌡️",
                "DVD-плееры 📀",
                "Другие мелкие бытовые приборы 🏠",
            ],
        },
        {
            "title": "Категория 3",
            "content": [
                "Сумки и аксессуары для сумок 👜",
                "Шляпы 🎩",
                "Косметика 💄",
                "Парфюмерия 🌸",
                "Средства по уходу за кожей 🧴",
                "Декоративная косметика 💅",
                "Аксессуары для мобильных телефонов 📱",
                "Чехлы для автомобилей 🚗",
                "Накрытия для автомобилей 🚙",
                "Автомобильные аксессуары 🛠️",
                "Подшипники ⚙️",
                "Колесные диски 🚘",
                "Комплектующие для обуви 👟",
                "Садовые инструменты 🌿",
                "Керамическая посуда 🍽️",
            ],
        },
        {
            "title": "Категория 4",
            "content": [
                "Носки 🧦",
                "Колготки 🩲",
                "Чулки 🧦",
                "Канцелярские товары 📎",
                "Зонты ☂️",
                "Постельные принадлежности 🛏️",
                "Мебель 🛋️",
                "Электрические велосипеды 🚲",
                "Рабочие перчатки 🧤",
                "Светильники 💡",
                "Палатки ⛺",
                "Кухонные принадлежности 🍽️",
                "Самокаты 🛴",
                "Игрушки 🎲",
            ],
        },
    ]

    def category_format(items):
        if type(items) is list:
            items_out = "\n".join(items)
            return items_out
        else:
            return items

    categories_out = list(map(
        lambda category: f'<strong>{category["title"]}</strong>\n' + category_format(category["content"]), categories
    ))
    categories_out = "\n\n".join(categories_out)
    await callback.message.answer(categories_out, parse_mode="html")

    info = (
        "цена от ... до ... за кг. Более точную стоимость можно проверить  по таблице плотности. "
        "Плотность груза высчитывается по формуле Вес/Объём . Чем выше плотность , тем дешевле тариф."
    )
    await callback.message.answer(info, parse_mode="html", reply_markup=keyboards.cargo6)


@router.callback_query(F.data == "cargo/6/help")
async def route(callback: CallbackQuery, state: FSMContext):
    text = "Пожалуйста, опиши товары, которые нужно доставить."
    await state.set_state(Help.text)
    await callback.message.answer(text, parse_mode="html")


@router.message(Help.text)
async def route(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    await state.set_state(Help.contact)
    await message.answer("Как с тобой лучше связаться?")


@router.message(Help.contact)
async def route(message: Message):
    text = "Спасибо! мы вернемся с ответом в ближайшее время!"
    await message.answer(text)
