from aiogram.types import Message
from aiogram import Bot, Dispatcher, executor

bottoken = '7101094041:AAFayJzvcfeYNlgX0rI257IHXGf9agzhcNw'
bot = Bot(bottoken)
dp = Dispatcher(bot)
CHANNEL = '@my_favoritestobe'


sozlar = ['ahmoq', 'jinni', 'tentak', 'mol', 'garang', 'tupoy', 'eshshak', 'sotak', 'iplos', ]

@dp.message_handler(commands='start')
async def start(message: Message):
    userid = message.from_user.id
    chekbot = Bot.get_current()
    check = await chekbot.get_chat_member(user_id=userid, chat_id=CHANNEL)
    member = check.status
    if member == 'left':
        await bot.send_message(chat_id=userid, text=f'Siz kanalga azo emassiz. {CHANNEL}')
    else:
        await bot.send_message(chat_id=userid, text='Xush kelibsiz')


@dp.message_handler()
async def getword(message: Message):

    text = message.text
    chatid = message.chat.id
    messageid= message.message_id
    fullname = message.from_user.full_name

    forward = message.forward_from
    if forward:
        await bot.send_message(chat_id=chatid, text=f'Uzatilgan xabar jonatish mumkin emas {fullname}')
        await bot.delete_message(chat_id=chatid, message_id=messageid)


    for soz in sozlar:
        if soz in text.lower():
            await bot.send_message(chat_id=chatid, text=f'Sokinish mumkin emas. {fullname}')
            await bot.delete_message(chat_id=chatid, message_id=messageid)



    if '@' in text or 'https:/':
        await bot.send_message(chat_id=chatid, text=f'Raklama tarqatish mumkin emas. {fullname}')
        await bot.delete_message(chat_id=chatid, message_id=messageid)



executor.start_polling(dp, skip_updates=True)