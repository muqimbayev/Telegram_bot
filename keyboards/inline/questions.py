from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Kategoriya menyusi
categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Avvalgi", callback_data="back"),
            InlineKeyboardButton(text="Keyingi ➡️", callback_data="next"),
        ],
    ],
)
