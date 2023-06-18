import asyncio
from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN

################### ИНИЦИИРУЕМ БОТА И ДИСПЕТЧЕРА ##########################################

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#################################### СТАРТ ########################################
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привет!\n Напиши мна что-нибудь!')

#################################### HELP ########################################
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply('Напиши мна что-нибудь и я отправлю этот текст тебе в ответ.')

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