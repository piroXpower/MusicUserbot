from Deadly import PLAYER, OWNER_ID
from pyrogram import filters, Client
import speedtest
import asyncio

HNDLR = "+"



def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("Running Download SpeedTest")
        test.download()
        m = m.edit("Running Upload SpeedTest")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("Sharing SpeedTest Results")
    except Exception as e:
        return m.edit(e)
    return result

# 		Send Speed of Internet


@Client.on_message(filters.command(["speedcheck"], prefixes=f"{HNDLR}") | filters.user(OWNER_ID))
async def speedtest_function(client, message):
    m = await message.reply_text("Running Speed test")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""**Speedtest Results**

<u>**Client:**</u>
**__ISP:__** {result['client']['isp']}
**__Country:__** {result['client']['country']}
**__ISP Rating:__** {result['client']['isprating']}

<u>**Server:**</u>
**__Name:__** {result['server']['name']}
**__Country:__** {result['server']['country']}, {result['server']['cc']}
**__Sponsor:__** {result['server']['sponsor']}
**__Latency:__** {result['server']['latency']}
**__Ping:__** {result['ping']}

<u>**Speed:**</u>
**__Download Speed:__** {result['download'] / 1024 / 1024:.2f} Mbps
**__Upload Speed:__** {result['upload'] / 1024 / 1024:.2f} Mbps
"""
    msg = await app.send_message(chat_id=message.chat.id, message=output)
    await m.delete()
