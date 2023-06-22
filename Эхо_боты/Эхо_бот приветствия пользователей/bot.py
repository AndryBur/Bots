import asyncio
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State
from config import TOKEN

################### ИНИЦИИРУЕМ БОТА И ДИСПЕТЧЕРА ##########################################

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#################################### ИНСТРУКЦИЯ ########################################
text='''
Привет! Я простой эхо-бот .
Напиши мне что-нибудь!
<b>/start - А я буду внимательно тебя слушать и запоминать. Все что запомню - расскажу.</b>

Если будет непонятно нажимай:
<b>/help - я объясню</b>

Если надоест:
<b>/cancel - выход</b>
'''

#################################### СТАРТ ########################################
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, text, parse_mode='html')
   
#################################### HELP ########################################
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply('Напиши мна что-нибудь и я отправлю этот текст тебе в ответ.')

# #################################### ВЫХОД ###########################################
@dp.message_handler(commands=['cancel']) #, state= '*'
async def cancel_command(message: types.Message, state: FSMContext): 
    await bot.send_message(message.from_user.id, "Выход. Пока!!!\n")
    await state.finish()
    return False

#################################### ОБРАБОТКА ТЕКСТОВОГО СООБЩЕНИЯ ########################################
@dp.message_handler()                                       # по умолчанию библиотека делает обработку только текстовых сообщений (если скобки оставить пустыми)
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

# Параметр msg это всё то же сообщение, как и в предыдущих пунктах.
# В данном случае на последней строчке мы отправляем пользователю сообщение не ответом, а простым сообщением. 
# Для этого мы воспользовались методом send_message и передали в него два обязательных параметра - id чата, 
# куда отправляем, и сам текст сообщения. Их мы взяли из объекта msg, который является представителем класса 
# Message. Параметр from_user ссылается на ещё один объект - данный параметр имеет класс User. У него есть 
# параметр id - уникальный идентификатор для чатов и каналов в телеграме. Ну и текст полученного сообщения мы получили из поля text.

#################################### ОБРАБОТКА ТЕКСТОВОГО СООБЩЕНИЯ ########################################
if __name__=='__main__':
    executor.start_polling(dp)