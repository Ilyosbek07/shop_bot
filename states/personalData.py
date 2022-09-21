

from aiogram.dispatcher.filters.state import StatesGroup, State


# Shaxsiy ma'lumotlarni yig'sih uchun PersonalData holatdan yaratamiz
class PersonalData(StatesGroup):
    # Foydalanuvchi buyerda 3 ta holatdan o'tishi kerak
    fullName = State() # ism
    phoneNum = State() # Tel raqam
    byurtma = State() # Byurtma turi
    tulov = State() # to'lov turi