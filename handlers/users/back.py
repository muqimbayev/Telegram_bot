from loader import dp
from aiogram.types import Message
from keyboards.default.savollarkey import menuSavol

@dp.message_handler(text="Ortga")
async def bot_start(message: types.Message):
  await message.answer(f"Bosh menu", reply_markup=menuSavol)