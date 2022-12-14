from aiogram.types import Message
from keyboards.default.MenyularKeyboard import menyularKeyboard
from keyboards.default.UzbekKeyboard import menuUzbek
from keyboards.default.savatKeyboard import savatMenu, tulovMenu

from loader import  dp

@dp.message_handler(text="š Savat")
async def send_menyu(message: Message):
    await message.answer("<b>š  Ajoyib!  Birgalikda tanlaymizmi?</b>", reply_markup=savatMenu)


@dp.message_handler(text="š Buyurtmani tasdiqlash")
async def send_menu(message: Message):
    await message.answer("<b>š  Ajoyib!  Birgalikda tanlaymizmi?</b>", reply_markup=tulovMenu)


@dp.message_handler(text="š Qo'ng'iroq qilish")
async def send_menu(message: Message):
    await message.answer("<b><i>Bizning telefon raqamimiz:\n\nš  +998(97) 076 00 01\nš  +998(93) 609 01 23</i></b>")


@dp.message_handler(text="š Yana buyurtma tanlash")
async def send_menu(message: Message):
    await message.answer("<b><i>š  Ajoyib!  Birgalikda buyurtma beramizmi?</i></b>", reply_markup=menyularKeyboard)


@dp.message_handler(text="š Asosiy menyu")
async def send_menu(message: Message):
    await message.answer("<b><i>š  Ajoyib!  Qaysi bo'limni tanlaymiz?</i></b>", reply_markup=menuUzbek)


@dp.message_handler(text="š  Ortga qaytish")
async def back_link(message: Message):
    await message.answer("<b><i>š  Ajoyib!  Birgalikda buyurtma beramizmi?</i></b>", reply_markup=menyularKeyboard)


