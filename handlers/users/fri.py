from aiogram import types
from keyboards.inline.klaviaturaKeyboard import klaviaturaMenu
from loader import dp

@dp.message_handler(text_contains="š FRI")
async def select_category(message:types.Message):
    await message.answer(f"<b><i>š Ajoyib! Siz FRI tanladingiz!</i></b>")
    photo_id="AgACAgIAAxkBAAIHX2Lg3mz8tAQFlzf9U6ncPnpbTJQdAAI0vzEbh_EJS8LrF-a4ateGAQADAgADeQADKQQ"
    await message.answer_photo(
        photo_id, caption=f"<b><i>š Ajoyib! Siz FRI tanladingiz!\nšµ Narxi - <i>11 000 so'm</i>\nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)