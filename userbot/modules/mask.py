
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.events import register
from userbot import bot, CMD_HELP


@register(outgoing=True, pattern="^.mask (?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Reply to any user message.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit("```reply to text message```")
       return
    chat = "@hazmat_suit_bot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Reply to actual users message.```")
       return
    await event.edit("```Processing```")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=905164246))
              await bot.send_message(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock @sangmatainfo_bot and try again```")
              return
          if response.text.startswith("Forward"):
             await event.edit("```can you kindly disable your forward privacy settings for good?```")
          else: 
             await bot.send_file(event.chat_id, response.message.media)
             
CMD_HELP.update({
    "mask": 
        ".mask\
        \nUsage: Reply to a user message"
})
