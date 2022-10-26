import os
import logging 

from aiogram import Bot, Dispatcher, executor, types


TOKEN = os.getenv('TOKEN')  #найти в окружении такую переменную


file_log = logging.FileHandler('Log.log')
console_out = logging.StreamHandler()

logging.basicConfig(handlers=(file_log, console_out), 
                    format='[%(asctime)s | %(levelname)s]: %(message)s', 
                    datefmt='%m.%d.%Y %H:%M:%S',
                    level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

trans_dict = {'А':	'A',
	'Б':	'B',
	'В':    'V',
	'Г':	'G',
	'Д':	'D',
	'Е':	'E',
	'Е':	'E',
	'Ж':	'ZH',
	'З':	'Z',
	'И':	'I',
	'Й':	'I',
    'К':	'К',
    'Л':	'L',
	'М':	'М',
	'Н':	'N',
	'О':	'O',
	'П':	'P',
	'Р':	'R',
	'С':	'S',
	'Т':	'T',
	'У':	'U',
	'Ф':	'F',
	'Х':	'KH',
	'Ц':	'TS',
	'Ч':	'CH',
	'Ш':	'SH',
	'Щ':	'SHCH',
	'Ы':	'Y',
    'Ь':    '',
	'Ъ':	'IE',
	'Э':	'E',
	'Ю':	'IU',
	'Я':	'IA'}



@dp.message_handler(commands = ['start'])
async def send_welcome(message: types.Message): 
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'''Привет, {user_name}!
    Введите ФИО кириллицей'''
    logging.info(f'{user_name=} {user_id=}sent message: {message.text}')
    await message.reply(text)  

@dp.message_handler()
async def send_echo(message: types.Message):   #async для асинхронного выполнения функций
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    for char in trans_dict.keys():
        text = text.upper().replace(char,trans_dict.get(char)).title()
    logging.info(f'{user_name=} {user_id=} received message: {message.text} \nsent message: {text}')
    await bot.send_message(user_id, text)   #Вместо rerurn используется await т.к. функция асинхронная
                                             #в асинхронных функциях можно делать несколько await (в отличие от ретёрнов в обычных)

if __name__ == '__main__':
    executor.start_polling(dp)
