from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.private)
async def on_message(_, message:Message):
   mention = message.from_used.first_name + message.from_used.last_name
   await message.reply_photo(photo="https://graph.org//file/7ea1fab6a3a1d66327d31.jpg", caption=f"{mention}\n\n𝗦𝗢𝗥𝗥𝗬 𝗠𝘆 𝗠𝗮𝘀𝘁𝗲𝗿 𝗜𝘀 𝗢𝗳𝗳𝗹𝗶𝗻𝗲 𝗛𝗲 𝗪𝗶𝗹𝗹 𝗚𝗲𝘁𝗕𝗮𝗰𝗸 𝗧𝗼 𝗬𝗼𝘂 𝗦𝗼𝗼𝗻 𝗝𝘂𝘀𝘁 𝗟𝗲𝗮𝘃𝗲 𝗢𝗻𝗲 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 𝗔𝗻𝗱 𝗴𝗼 𝗽𝗹𝗲𝗮𝘀𝗲 𝗱𝗼𝗻'𝘁 𝗳𝗹𝗼𝗼𝗱 𝗼𝗿 𝗦𝗽𝗮𝗺") 

app.run()
idle()
