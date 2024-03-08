from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
  keyboard = [
    [
      KeyboardButton("Mantiqiy savollar"),
      KeyboardButton("Boshqotirmalar"),

    ],
    [
      KeyboardButton("Bot haqida"),
    ],
    
  ],
  resize_keyboard=True
)