from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAIp9mBtwBBZGywWEmV-WC8gcMArjusuAAKMAgACTp1xV6m-mtC1YTfoHgQ")
    await message.reply_text(
        f"""<b>مرحبا يا  {message.from_user.first_name}!
\nاستطيع تشغيل الاغاني في المحادثات الصوتيه بالمجموعه
\nقناه تحديثات البوت @sourcejokes1.
\nاضغط /help للاوامر المتاحه
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌍 BOT CH", url="https://t.me/sourcejokes1",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 DEV", url="https://t.me/Mr_Code2"
                    ),
                    InlineKeyboardButton(
                        "🔊 source lava CH", url="https://t.me/UU_lava"
                    ),
                    InlineKeyboardButton(
                        "💕 super ", url="https://t.me/suber_2"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/C4S_BOT?startgroup=true"
                    ) 
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ هل ترغب في البحث علي فديوهات باليوتيوب?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 القناه", url="https://t.me/sourcejokes1"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "✅ نعم", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "لا ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\nلتشغيل اغنيه /play «اسم الاغنيه»
\n لتشغيل اغنيه من ديزر /dplay «اسم الاغنيه»
/playlist - لعرض قائمه التشغيل
/current - لعرض الاغنيه المشغله حاليا
\n لتحميل اغنيه التي تريدها  /song «اسم الاغنيه»
\n للحث علي فيديو علي اليوتيوب /Search «اسم الاغنيه»
\n لتشغيل اغنيه من ديزر /deezer «اسم الاغنيه»
/video <song name> - لتحميل الفيديوهات
\n*Admins only*
/pause - ايقاف الاغنيه
/resume - استكمال الاغنيه
/skip - تخطي الاغنيه
/end - ايقاف تشغيل الموسيقي
/userbotjoin - لدعوة البوت المساعد للمجموعة
/admincache - لتحديث قائمه الادمنيه
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/sourcejokes1"
                    )
                ]
            ]
        )
    )    
