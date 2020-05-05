#kanged freshly by @deleteduser420
from telethon import events
from userbot import bot, CMD_HELP
import asyncio





@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "load":

        await event.edit(input_str)

        animation_chars = [

            "▮",

            "▯",

            "▬",

            "▭"
            "‎"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])



from telethon import events
import asyncio
@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "square":

        await event.edit(input_str)

        animation_chars = [

            "◧",

            "◨",

            "◧",

            "◨"
            "‎"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])



@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "up":

        await event.edit(input_str)

        animation_chars = [

            "╹",

            "╻",

            "╹",

            "╻"
            "‎"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])

@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "round":

        await event.edit(input_str)

        animation_chars = [

            "⚫",

            "⬤",

            "●",

            "∘"
            "‎"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])



@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 7)

    input_str = event.pattern_match.group(1)

    if input_str == "heart":

        await event.edit(input_str)

        animation_chars = [

           

            "❤️",

            "🖤",

            "❤️",
            "🖤",

            "❤️",

            "🖤",

            "❤️",
      
            "‎"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 7])



@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 9)

    input_str = event.pattern_match.group(1)

    if input_str == "anim":

        await event.edit(input_str)

        animation_chars = [

            "😁",

            "😧",

            "😡",

            "😢",

           
 
            "😢",

            "😧",

            "😡",

            "😁",

           


            

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 8])



@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1.3

    animation_ttl = range(0, 7)

    input_str = event.pattern_match.group(1)

    if input_str == "monkey":

        await event.edit(input_str)

        animation_chars = [

            ">🐵<",

            ">🙉<",

            ">🙈<",

            ">🙊<",
            
            ">🐵<",

            ">🙊<",


            ">🖕‎🐵🖕<"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 7])

            
            



@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 14)

    input_str = event.pattern_match.group(1)

    if input_str == "hand":

        await event.edit(input_str)

        animation_chars = [

            "👈",

            "👉",

            "☝️",

            "👆",

            "🖕",

            "👇",

            "✌️",

            "🤞",

            "🖖",

            "🤘",

            "👌",

            "🖐️",

            "🤙"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 14])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 13)

    input_str = event.pattern_match.group(1)

    if input_str == "cnt":

        await event.edit(input_str)

        animation_chars = [

            "🔟",

            "9️⃣",

            "8️⃣",

            "7️⃣",

            "6️⃣",

            "5️⃣",

            "4️⃣",

            "3️⃣",

            "2️⃣",

            "1️⃣",

            "0️⃣",

            "🆘"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 13])
            

            
            
CMD_HELP.update({
    "animate":
    ".animate\
    \nUsage: Some animated memes see yourself lul\
     \n\n.load\
     \n.square\
     \n.up\
     \n.round\
     \n.heart\
     \n.anim\
     \n.monkey\
     \n.hand"
    
})
