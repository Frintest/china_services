import asyncio
from aiogram import Bot, Dispatcher
from config import API_TOKEN
from app.handlers import router

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
