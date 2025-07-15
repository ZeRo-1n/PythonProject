from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
import asyncio


bot = Bot(
    token='токен',
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()

@dp.message(Command("store"))
async def cmd_store(message: Message):
    await message.answer(f"{message.from_user.first_name}, добро пожаловать в магазин WordLet!")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
