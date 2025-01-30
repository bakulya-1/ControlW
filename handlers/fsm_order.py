from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import  Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from config import STAFF
from db import main_db
import buttons



class OrderFSM(StatesGroup):
    size = State()
    products_id = State()
    quantity = State()
    contact = State()
    submit = State()


async def start_fsm_order(message: types.Message):
    await message.answer('Введите размер товара: ', reply_markup=buttons.cancel)
    await OrderFSM.size.set()

async def size_order (message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await OrderFSM.next()
    await message.answer('Введите количество товара: ')

async def quantity_order(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['quantity'] = message.text

    await OrderFSM.next()
    await message.answer('Введите артикул товара: ')

async def product_id_order (message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_id'] = message.text

    await OrderFSM.next()
    await message.answer('Введите ваш контактный номер: ')

async def contact_order(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['contact'] = message.text

    await OrderFSM.next()
    await message.answer('Верные ли данные?', reply_markup=buttons.submit)
    await message.answer_contact(contact=data['contact'],
                                 caption=f'размер товара - {data["size"]}\n'
                                         f'количество  - {data["quantity"]}\n'
                                         f'артикул - {data["product_id"]}\n'
                                         f'ваш контактный номер - {data["contact"]}\n')

async def submit_order(message: types.Message, state: FSMContext):
    if message.text == 'да':
        async with state.proxy() as data:
            await main_db.sql_insert_store(
                size=data['size'],
                product_id=data['product_id'],
                quantity=data['quantity'],
                contact=data['contact']
            )

            await message.answer('Ваш заказ отправлен!', reply_markup=buttons.remove_keyboard)
            await state.finish()

    elif message.text == 'нет':
        await message.answer('Хоршо, отменено! ', reply_markup=buttons.remove_keyboard)
        await state.finish()

    else:
        await message.answer('Выберите да или нет')


async def send_order_to_staff(message: types.Message, state: FSMContext):
    for staff_id in STAFF:
        await message.answer(staff_id, f'Новый заказ: ')



def register_handlers_order(dp: Dispatcher):
    dp.register_message_handler(start_fsm_order, commands=['order'])
    dp.register_message_handler(size_order, state=OrderFSM.size)
    dp.register_message_handler(quantity_order, state=OrderFSM.quantity)
    dp.register_message_handler(product_id_order, state=OrderFSM.products_id)
    dp.register_message_handler(contact_order, state=OrderFSM.contact)
    dp.register_message_handler(submit_order, state=OrderFSM.submit)


