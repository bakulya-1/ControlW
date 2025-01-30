from turtledemo.penrose import start
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


start = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton('/start'),
    KeyboardButton('/cat'),
    KeyboardButton('/info_bot'),
    KeyboardButton('/products'),
    KeyboardButton('/order'))



submit = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True).add(KeyboardButton('да'), KeyboardButton('нет'))

cancel = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2,
                             one_time_keyboard=True).add(KeyboardButton('отмена'))



#удаление кнопки из интерфейса
remove_keyboard = ReplyKeyboardRemove()

