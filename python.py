from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters.command import Command
from aiogram.filters import Command
import asyncio
import logging


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="7020085710:AAFT7vHXhb0NzAXTKMDyxksVqu2ZmFudDKo")
# Диспетчер
dp = Dispatcher()
router = Router()



@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="/start"),
            types.KeyboardButton(text="/joke"),
            types.KeyboardButton(text="/news_NSK"),
            types.KeyboardButton(text="/smotre"),
            types.KeyboardButton(text="/watch_pubg")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи"
        )
    await message.answer("Привет\nМожет тебе расказать анекдот или же новости Новосибирска или же может...\nХочешь посмотреть фильмы или мультфильм, можешь посмотреть прохождение игры pubg('metro royale или обычный') на ютуб-канале", reply_markup=keyboard)


@dp.message(Command("joke"))
async def cmd_smex(message: types.Message):
    await message.answer("Маленький сын спрашивает отца: "
                         "\n— папа, а почему ты повесил конфеты на ёлку так высоко?"
                         "\n— Для того чтобы ты не достал их до Нового Года!"
                         "\n— Так мне что, теперь дождик жрать?!")


@dp.message(Command("news_NSK"))
async def cmd_nsk(message: types.Message):
    await message.answer("Https://t.me/nsknewsinfo")
    
    
@dp.message(Command("smotre"))
async def cmd_films(message: types.Message):
    await message.answer("https://www.afisha.ru/movie/")
    
    
@dp.message(Command("watch_pubg"))
async def cmd_pubg(message: types.Message):
    await message.answer("https://www.youtube.com/watch?v=MykfN-dlbUM"
                         "/nhttps://youtu.be/mXiLqo0Sj4o")
        
    
    
# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)
    
    
    
if __name__ == "__main__":
    asyncio.run(main())
    
    
if __name__ == "__main__":
    asyncio.run(main())
