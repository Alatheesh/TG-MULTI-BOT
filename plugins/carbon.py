from io import BytesIO
from aiohttp import ClientSession
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
aiohttpsession = ClientSession()


@Client.on_message(filters.command("carbon"))
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴀᴋᴇ ᴄᴀʀʙᴏɴ.")        
    if not message.reply_to_message.text:
        return await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴀᴋᴇ ᴄᴀʀʙᴏɴ.")       
    user_id = message.from_user.id
    code = message.reply_to_message.text
    m = await message.reply_text("ᴘʀᴏᴄᴇssɪɴɢ...")
    url = "https://carbonara.vercel.app/api/cook"
    async with aiohttpsession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"   
    await m.edit("ᴜᴘʟᴏᴀᴅɪɴɢ..")
    await message.reply_photo(photo=image, caption="**MADE WITH ❤️ BY >🇱 🇦 🇹 🇭 🇪 🇪 🇸 🇭  & 🇧 🇧 **",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("JOIN 🇳 🇹 🇲 ", url="https://t.me/llathu63035")]])                 
    )
    await m.delete()
    carbon.close()
