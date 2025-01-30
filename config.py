from decouple import config
from aiogram import  Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


token = config('TOKEN')
bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

Admins = [992671114, ]



class Staff:
    def __init__(self, name, user_id, role):
        self.name = name
        self.user_id = user_id
        self.role = role

STAFF = [
    Staff( 'user_id_1', 'Jahen','Администратор'),
    Staff('user_id_2', 'Han Nam', 'Специалист'),
    Staff('user_id_3', 'Kaneshiro', 'Предприниматель')
]

