@register(outgoing=True, pattern="^.mlist(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else: await event.edit("List Of Installed modules use .help<module name>")
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`  -  "
        await event.reply(string)
