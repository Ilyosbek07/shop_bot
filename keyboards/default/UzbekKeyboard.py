from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuUzbek=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="đŊ Menyu"),
        ],
        [
            KeyboardButton(text="âšī¸ Ma'lumot"),
            KeyboardButton(text="đ  Aloqa"),
        ],
        # [
        #     KeyboardButton(text="đ Manzil"),
        # ],
        [
            KeyboardButton(text="âī¸ Fikr bildirish"),
            KeyboardButton(text="âī¸ Sozlamalar"),
        ],
    ],
    resize_keyboard=True
)