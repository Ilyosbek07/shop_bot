
from aiogram.types import Message, CallbackQuery

from keyboards.inline.klaviaturaKeyboard import klaviaturaMenu
from keyboards.inline.pitsaKeyboard import pitsaMenu
from loader import dp

@dp.message_handler(text_contains="Pitsa")
async def select_category(message:Message):
    await message.answer(f"<b><i>Ajoyib! Keling birgalikda tanlaymiz!</i></b>", reply_markup=pitsaMenu)

    @dp.callback_query_handler(text="pitsa1")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>š Ajoyib! Siz MARGARITA pitsasini tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa2")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>š Ajoyib! Siz GRIBNAYA pitsasini tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa3")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>š Ajoyib! Siz OVOSHNOY pitsasini tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa4")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>š Ajoyib! Siz HALOL PITSA tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa5")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>š Ajoyib! Siz KURINNAYA GRUDINKA pitsasini tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa6")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>š Ajoyib! Siz PEPPERONI pitsasini tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa7")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>š Ajoyib! Siz MEKSIKANO pitsasini tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa8")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>š Ajoyib! Siz DRAKON pitsasini tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa9")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>š Ajoyib! Siz VETCHINA S GRIBAMI pitsasini tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa10")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>š Ajoyib! Siz BERBEKYU pitsasini tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa11")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>š Ajoyib! Siz FIRMENNAYA pitsasini tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa12")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>š Ajoyib! Siz MYASNAYA pitsasini tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa13")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>š Ajoyib! Siz 4-MYASO pitsasini tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa14")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>š Ajoyib! Siz AMERICANO pitsasini tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa15")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>š Ajoyib! Siz SUPER ASSORTI pitsasini tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa16")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>š Ajoyib! Siz MIKS pitsasini tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa17")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>š Ajoyib! Siz DON KARLEONE pitsasini tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa18")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>š Ajoyib! Siz MAFIA pitsasini tanladingiz! \nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)