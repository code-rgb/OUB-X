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
   
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("**Module doesn't exist or Module name is invalid**")
    else:
        await event.edit("**All currently  loaded modules are listed below**\
            \nUsage: Type `.mlist or .help <module name>` for more info.")
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`  •  "
        await event.reply(string)
