from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.user(OWNER_ID) & filters.command(["iloveu", "lover"], ["."]))
async def lovers(client: Client, message: Message):
    e = await message.edit("ɪ ʟᴏᴠᴇᴇ ʏᴏᴜᴜᴜ 💕")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💘💞💗💕")
    await e.edit("💘💞💕💗")
    await e.edit("ʟᴏᴠᴇ ʏᴏᴜ 💝💖💘")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💘💞💕💗")
    await e.edit("ʟᴏᴠᴇ")
    await e.edit("ʏᴏᴜ")
    await e.edit("ꜰᴏʀᴇᴠᴇʀ 💕")
    await e.edit("💘💘💘💘")
    await e.edit("ʟᴏᴠᴇ")
    await e.edit("ɪ")
    await e.edit("ʟᴏᴠᴇ")
    await e.edit("ʙᴀʙʏ")
    await e.edit("ɪ ʟᴏᴠᴇ ʏᴏᴜᴜᴜᴜ")
    await e.edit("ᴍʏ ʙᴀʙʏ")
    await e.edit("💕💞💘💝")
    await e.edit("💘💕💞💝")
    await e.edit("ʟᴏᴠᴇ ʏᴏᴜ 💞")