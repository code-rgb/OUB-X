from telethon import events
import asyncio
from userbot.events import register 
from userbot import  CMD_HELP, bot
from collections import deque
import importlib.util
import random



@bot.on(events.NewMessage(pattern=r"\.wchar", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
                await event.edit("`Tesla Wireless Charging (beta) Started...\nDevice Detected: Nokia 1100\nBattery Percentage:`10")
                await asyncio.sleep(0.5)
               await event.edit("`Tesla Wireless Charging (beta) Started...\nDevice Detected: Nokia 1100\nBattery Percentage:`20")
                await asyncio.sleep(0.5)
               await event.edit("`Tesla Wireless Charging (beta) Started...\nDevice Detected: Nokia 1100\nBattery Percentage:`30")
                await asyncio.sleep(0.5)
               await event.edit("`Tesla Wireless Charging (beta) Started...\nDevice Detected: Nokia 1100\nBattery Percentage:`40")
                await asyncio.sleep(0.5)
               await event.edit("`Tesla Wireless Charging (beta) Started...\nDevice Detected: Nokia 1100\nBattery Percentage:`50")
                await asyncio.sleep(0.5)
               await event.edit("`Tesla Wireless Charging (beta) Started...\nDevice Detected: Nokia 1100\nBattery Percentage:`60")
                await asyncio.sleep(0.5)
               await event.edit("`Tesla Wireless Charging (beta) Started...\nDevice Detected: Nokia 1100\nBattery Percentage:`70")
                await asyncio.sleep(0.5)
               await event.edit("`Tesla Wireless Charging (beta) Started...\nDevice Detected: Nokia 1100\nBattery Percentage:`80")
               await asyncio.sleep(0.5)
               await event.edit("`Tesla Wireless Charging (beta) Started...\nDevice Detected: Nokia 1100\nBattery Percentage:`90")
                await asyncio.sleep(0.5)
               await event.edit("`Tesla Wireless Charging (beta) Started...\nDevice Detected: Nokia 1100\nBattery Percentage:`100")
                await asyncio.sleep(0.5)
               await event.edit("`Tesla Wireless Charging (beta) Completed...\nDevice Detected: Nokia 1100` Space Grey Varient\n`Battery Percentage:` [100%] (https://telegra.ph/file/93a3563e501394fb1e861.mp4)", link_preview=True"
         await asyncio.sleep(2)
        await event.delete()
    

        
