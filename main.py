from instapy2 import InstaPy2
from instapy2.types import LikeType
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5909192602:AAFweB-rh0-IMkTO6Ere6Fq_YDtmoMRsqAI'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dictLogins = {'mincyvystupakpj': 'Piperf8B', 'akhtarvtstokescp': 'HopeJHb5FmEa' }
session = InstaPy2()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
        await message.reply("Привет! Укажи свой логин в инстаграмм для накрутки?")

@dp.message_handler()
async def send_letsgo(message: types.Message):
        print(message.text)
        await message.reply("Процесс запущен. Когда все будет готово, я тебе сообщу")
        for key, value in dictLogins.items():
            session.login(username=key, password=value)
            session.like(amount=10, iterable=[message.text], type=LikeType.Users)
        await message.reply("Готово!")



if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)