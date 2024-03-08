from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menukey import menu
from aiogram.dispatcher.filters import Command
from loader import dp
import logging

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}!\nQBrain botiga xush kelibsiz. Bu bot sizga mantiqiy savollar, qiziqarli boshqotirmalar, hamda boshqa intellektual muhokamalarni taklif etadi.", reply_markup=menu)

@dp.message_handler(text="⬆️ Bosh menuga")
@dp.message_handler(text="⬅️ Ortga")
async def bot_start(message: types.Message):
  await message.answer(f"Bosh menu", reply_markup=menu)

