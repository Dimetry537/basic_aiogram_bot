from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from src.db.config import TOKEN
from src.handlers.start import router as start

async def main() -> None:

    bot = Bot(TOKEN, parse_mode=ParseMode.HTML) # type: ignore
    dp = Dispatcher()
    dp.include_router(start)
    await dp.start_polling(bot)