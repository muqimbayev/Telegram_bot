from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menukey import menu
from loader import dp
from keyboards.default.savollarkey import menuSavol


@dp.message_handler(text="Mantiqiy savollar")
@dp.message_handler(text="🔙 Ortga")
async def savollar(message: Message):
    await message.answer(text="Savollar darajasini tanlang:", reply_markup=menuSavol)


@dp.message_handler(text="Bot haqida")
async def savollar(message: Message):
    await message.answer(text="Bot haqida ma'lumot")


