from aiogram.dispatcher.filters import Text
from aiogram import types
from aiogram.types import Message, CallbackQuery, message
from loader import dp
from keyboards.default.back import back
from keyboards.inline.questions import categoryMenu
from data.config import count_entry


lst = [
  "1.png",
  "2.png",
  "3.png",
  "4.png",
  "5.png",
  "6.png"]

photo_path = '1.png'


@dp.message_handler(text="Boshlang'ich")
async def bot_start(message: Message):

    await message.answer(f"Savollar boshlandi.", reply_markup=back)
    await message.answer_photo(types.InputFile(photo_path), caption="Rasmning tavsifi", reply_markup=categoryMenu)

