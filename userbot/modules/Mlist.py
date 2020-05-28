# Copyright (C) 2020 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" OUB-X module list """

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.mlist(?: |$)(.*)")
async def help(event):
    """ For .mlist command,"""
    args = event.pattern_match.group(1)
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("Please specify a valid module name.")
    else:
        await event.edit("`Installed Modules`")
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`, "
        string = string[:-2]
        await event.reply(string)
