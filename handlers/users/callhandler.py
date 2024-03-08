from aiogram import types
from loader import dp
import logging

@dp.callback_query_handler(text = 'next')
async def next_question(call: types.CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data}")
    await call.message.answer("Salom nimaadur kimdir")

@dp.callback_query_handler()
async def back_question(callback: types.CallbackQuery):
  if callback.data == 'back':
      print("ISHLADI")
      callback_data = callback.data
      logging.info(f"{callback_data}")
      return await callback.message.answer(text="Salom nimadur kimdir")


