import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import CommandStart
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, CallbackQuery,InlineKeyboardButton
from Data import post_instagram_video
from aiogram.filters.command import Command

Token = ""

bot = Bot(Token)
dp = Dispatcher()
# Example usage



@dp.message(CommandStart())
async def starts(msg: Message):
    await msg.answer(f"""Assalomu Alaykum Botimizga Xush Kelibsiz 😇 

Bizning Botda 🕹 Siz Instagramdagi Videolani Sifatli Qilib ✨
    
    
Va Tez ⚡️ ... Yuklab Olasiz ✅
    
    
 {msg.from_user.full_name}!""", reply_markup=keyboard)


btn = [
    [KeyboardButton(text="Video Yuklash 📥"), KeyboardButton(text="Info")]
]

keyboard = ReplyKeyboardMarkup(keyboard=btn, resize_keyboard=True)



# inline buttons
check = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Obuna Bo'ldim ✅ ", callback_data="tek")],  # noqa
    [InlineKeyboardButton(text="Kanalga O'tish ♻️ ", url="https://t.me/+o5zJbvejpTI2ZjQy")],  # noqa
])

@dp.callback_query(F.data == "tek")
async def check_btn(call: CallbackQuery, bot: Bot):
    users_status = await bot.get_chat_member(chat_id=-1002215546240, user_id=call.from_user.id)
    if users_status.status != 'left':
        await bot.send_message(chat_id=call.from_user.id, text="""Rahmat 😇, Siz Kanalimizga Obuna Bo'ldingiz ✅



Videoni 🎥 Yuklash Uchun Linkni ⛓ Yuboring 🚀•••""")  # noqa

    else:
        await bot.send_message(chat_id=call.from_user.id, text="Siz Kanalga A'zo Bo'lmadingzi ❗️ Iltimos Qaytadan Urining 🔴",
                               reply_markup=check)
        text = "Guruhga obuna bo'ling !"  # noqa
        await call.answer(text, show_alert=True)

@dp.message(F.text == "Video Yuklash 📥")
async def start_cmd(msg: Message):
    await msg.answer(f"Bizning Kanalga Obuna Bo'lib Qo'ying 😉 👇🏻 {msg.from_user.full_name}!", reply_markup=check)


    @dp.message()
    async def sendvid(msg: Message):
        response_data = post_instagram_video(msg.text)

        await msg.answer_video(video=response_data['contents'][0].get('media'), caption="""Marhamat Videongiz 🎥 Tayyor ✅ 
•
•
•
Do’staringgizga Ulashing 🚀

@Diosavevideoyuklash_bot""")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
