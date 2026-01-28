import asyncio
from aiogram.types import Message

async def get_animation(status: Message, stop: asyncio.Event):
    dots = [".", "..", "...", ".."]
    i = 0
    while not stop.is_set():
        await status.edit_text(status.text + dots[i % len(dots)])
        i += 1
        await asyncio.sleep(0.15)