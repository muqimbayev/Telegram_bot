from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuSavol = ReplyKeyboardMarkup(
  keyboard = [
    [
      KeyboardButton("Boshlang'ich"),
      KeyboardButton("O'rta"),
      KeyboardButton("Yuqori"),
    ],
    [
      KeyboardButton("⬅️ Ortga"),
    ]
  ],
  resize_keyboard=True
)
