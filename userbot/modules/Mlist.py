# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.mlist$")
async def help(event):
await event.edit("**Installed Modules**😎\
\nUsage: Type `.help <module name>` to know how it works✌️")
string = ""
for i in CMD_HELP:
string += "`" + str(i)
string += "`  -  "
await event.reply(string)
