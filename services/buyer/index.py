def format_text(service):
    title = ""
    content = ""

    if service["title"] == "":
        title = "Название отсутствует"
    else:
        title = service["title"]

    if service["content"] == "":
        content = "Описание отсутствует"
    else:
        content = service["content"]

    text = f"<strong>{title}</strong>\n{content}"
    return text


def buyer():
    services = [
        {

            "title": "Стандартный пакет",
            "content": "10 % входит выкуп, проверка качества, фото /"
                       "видео отчет, доставка до конечного пункта, аванс 1000 юх или 15 000 ру"
        },
        {
            "title": "Поиск товара / фабрики",
            "content": "1000 ю, 2-3 позиции, сроки: 2-3 дня, в сложных случаях - 7 дней"
        },
        {
            "title": "Производство под заказ",
            "content": "производство по требованиям, под собственным брендом,"
                       "контроль всего процесса, фото / видео отчеты, доставка,"
                       "10-20% от стоимости закупа, зависит от сложности, от $1000, аванс 1000 юх или 15 000 руб"
        },
        {
            "title": "Выкуп образцов - 1000 юх / 15 000 руб",
            "content": "",
        },
    ]

    text = list(map(format_text, services))
    text = '\n\n\n'.join(text)

    return text
