from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from src.handlers.start import router as start

load_dotenv()

TOKEN = getenv("TELEGRAM_BOT_TOKEN")

async def main() -> None:

    bot = Bot(TOKEN, parse_mode=ParseMode.HTML) # type: ignore
    dp = Dispatcher()
    dp.include_router(start)
    await dp.start_polling(bot)