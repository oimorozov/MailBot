import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.formatting import Text, Bold
from config import BOT_TOKEN
from mail import get_mail
from helper import get_animation

dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hello, world!")

@dp.message(Command("get_mail"))
async def cmd_get_mail(message: Message):
    stop = asyncio.Event()
    status = await message.answer("Собираю письма")
    animation_task = asyncio.create_task(get_animation(status, stop))
    mails = await asyncio.to_thread(get_mail)
    stop.set()
    await animation_task
    await status.edit_text(**Text(Bold("Писем собрано: "), str(len(mails))).as_kwargs())
    try:
        if not mails:
            await message.answer("Писем не найдено или произошла ошибка.")
        else:
            for mail in mails:
                await message.answer(**Text(Bold('From: '), mail[0], '\n', Bold('Subject: '), mail[1]).as_kwargs())
    except Exception as e:
        print(f"Error: {e}")
        await message.answer("Произошла ошибка при получении писем.")

@dp.message()
async def other(message: Message):
    await message.answer("Напишите /get_mail для получения писем.")

async def main():
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())