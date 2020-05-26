from asyncio import sleep
from random import choice, getrandbits, randint
import re
from re import sub
import random
from os import execl
import time
from telethon import events
from userbot import bot
from collections import deque
import requests
import sys
import os
import io
import html
import json
from PIL import ImageEnhance, ImageOps

from userbot import CMD_HELP
from userbot.events import register
from userbot.modules.admin import get_user_from_event

EMOJI_PATTERN = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats 
    "]+")


def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return re.sub(EMOJI_PATTERN, '', inputString)

@register(outgoing=True, pattern="^.memex(?: |$)(.*)")
async def memex(xmemes):
     
    text = xmemes.pattern_match.group(1)
    if not text:
        if xmemes.is_reply:
            text = (await xmemes.get_reply_message()).message
        else:
            await xmemes.answer("`No text given, please try again")
            return
    choose =  [6, 8, 12, 30, 38, 51, 59, 3, 7, 45]
    sticcers = await bot.inline_query(
        "stickerizerbot", f"#{random.choice(choose)}{(deEmojify(text))}")
    await sticcers[0].click(xmemes.chat_id,
                            reply_to=xmemes.reply_to_msg_id,
                            silent=True if xmemes.is_reply else False,
                            hide_via=True)
    await xmemes.delete()
    
    
    
    
#     CMD_HELP.update({
#     "waifu":
#     ".waifu [text]\
# \nUsage: for custom anime girl stickers. \
# \n\n.memex\
# \nUsage: for custom meme stickers."})
