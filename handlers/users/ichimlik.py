
from aiogram.types import Message, CallbackQuery

from keyboards.inline.ichimliklar import ichimliklarMenu
from keyboards.inline.klaviaturaKeyboard import klaviaturaMenu

from loader import dp

@dp.message_handler(text_contains="Ichimliklar")
async def select_category(message:Message):
    await message.answer(f"<b><i>š  Ajoyib! Keling birgalikda tanlaymiz!</i></b>", reply_markup=ichimliklarMenu)



    @dp.callback_query_handler(text="coca")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
         "<b><i>š Ajoyib! Siz COCACOLA 0,5 lt tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>",
                reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="cocal")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>š Ajoyib! Siz COCACOLA 1 lt tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>",
                reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="cocala")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>š Ajoyib! Siz COCACOLA 1,5 lt tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>",
                reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pepsi5")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
         "<b><i>š Ajoyib! Siz PEPSI 0,5 lt tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>",
                reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pepsi2")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
          "<b><i>š Ajoyib! Siz PEPSI 1 lt tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>",
                reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pepsi3")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
                "<b><i>š Ajoyib! Siz PEPSI 1,5 lt tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>",
                reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="fanta5")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>š Ajoyib! Siz FANTA 0,5 lt tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>",
            reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="fanta2")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>š Ajoyib! Siz FANTA 1 lt tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>",
            reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="fanta3")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>š Ajoyib! Siz FANTA 1,5 lt tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>",
            reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="bliss1")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>š Ajoyib! Siz BLISS tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>",
            reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="dena1")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>š Ajoyib! Siz DENA tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>",
            reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="rich1")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>š Ajoyib! Siz RICH tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>",
            reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="flashbig")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>š Ajoyib! Siz FLASH BIG tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>",
            reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="flashmini")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>š Ajoyib! Siz FLASH MINI tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>",
            reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)


    @dp.callback_query_handler(text="nistle2")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>š Ajoyib! Siz NISTLE 0,5 lt tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="nistle3")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>š Ajoyib! Siz NISTLE 1 lt tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="nistle4")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>š Ajoyib! Siz NISTLE 1,5 lt tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="sprite2")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>š Ajoyib! Siz SPRITE 0,5 lt tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="sprite3")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>š Ajoyib! Siz SPRITE 1 lt tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="sprite4")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>š Ajoyib! Siz SPRITE 1,5 lt tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="sprite5")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>š Ajoyib! Siz SPRITE CAN tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="family2")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>š Ajoyib! Siz FAMILY 0,5 lt tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="family3")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>š Ajoyib! Siz FAMILY 1 lt tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="family4")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>š Ajoyib! Siz FAMILY 1,5 lt tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="kokchoy")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>š Ajoyib! Siz KO'K  CHOY tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="qorachoy")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>š Ajoyib! Siz QORA  CHOY tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="limonchoy")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>š Ajoyib! Siz LIMON  CHOY tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="maccoffe")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>š Ajoyib! Siz MACCOFFE  tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="nescafegold")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>š Ajoyib! Siz NESCAFE  GOLD tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="nescafeclassic")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>š Ajoyib! Siz NESCAFE  CLASSIC tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="jacobs")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>š Ajoyib! Siz JACOBS tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)