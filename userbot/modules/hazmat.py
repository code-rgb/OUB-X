# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# OUB-X exclusive 

import os
import asyncio
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.events import register
from userbot import bot, TEMP_DOWNLOAD_DIRECTORY, CMD_HELP


@register(outgoing=True, pattern=r'^.hazmat(:? |$)(\d)?')
async def _():
    await hazmat.edit("`Sending information...`")
    level = hazmat.pattern_match.group(2)
    if hazmat.fwd_from:
        return
    if not hazmat.reply_to_msg_id:
        await hazmat.edit("`Reply to any user message photo...`")
        return
    reply_message = await hazmat.get_reply_message()
    if not reply_message.media:
        await hazmat.edit("`No image found to make hazmat suit...`")
        return
    if reply_message.sender.bot:
        await hazmat.edit("`Reply to actual user...`")
        return
    chat = "@hazmat_suit_bot"
    message_id_to_reply = hazmat.message.reply_to_msg_id
    async with hazmat.client.conversation(chat) as conv:
        try:
            msg = await conv.send_message(reply_message)
            if level:
                m = f"/hazmat {level}"
                msg_level = await conv.send_message(
                          m,
                          reply_to=msg.id)
                r = await conv.get_response()
                response = await conv.get_response()
            else:
                response = await conv.get_response()
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await hazmat.reply("`Please unblock` @image_deephazmatbot`...`")
            return
        if response.text.startswith("Forward"):
            await hazmat.edit("`Please disable your forward privacy setting...`")
        else:
            downloaded_file_name = await hazmat.client.download_media(
                                 response.media,
                                 TEMP_DOWNLOAD_DIRECTORY
            )
            await hazmat.client.send_file(
                hazmat.chat_id,
                downloaded_file_name,
                force_document=False,
                reply_to=message_id_to_reply
            )
            """ - cleanup chat after completed - """
            try:
                msg_level
            except NameError:
                await hazmat.client.delete_messages(conv.chat_id,
                                                 [msg.id, response.id])
            else:
                await hazmat.client.delete_messages(
                    conv.chat_id,
                    [msg.id, response.id, r.id, msg_level.id])
    await hazmat.delete()
    return os.remove(downloaded_file_name)


CMD_HELP.update({
    "hazmat":
    ".hazmat"
    "\nUsage: make hazmat suit from image/sticker from the reply."
})
