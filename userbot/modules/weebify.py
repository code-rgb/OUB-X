#Ported to OUB-X
#Ported from Saitama Bot. 
#By :- @PhycoNinja13b
#Modified by :- @kirito6969

from userbot.events import register
from userbot import bot, CMD_HELP
from telethon import events
#from uniborg.util import admin_cmd

normiefont = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
weebyfont = ['卂', '乃', '匚', '刀', '乇', '下', '厶', '卄', '工', '丁', '长', '乚', '从', '𠘨', '口', '尸', '㔿', '尺', '丂', '丅', '凵',
             'リ', '山', '乂', '丫', '乙']


@register(outgoing=True, pattern="^.weeb(?: |$)(.*)")
async def weebify(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text   
    if not args:
        await event.edit("`What I am Supposed to Weebify U Dumb`")
        return
    string = '  '.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await event.edit(string)
   

boldfont = ['𝗮', '𝗯', '𝗰', '𝗱', '𝗲', '𝗳', '𝗴', '𝗵', '𝗶', '𝗷', '𝗸', '𝗹', '𝗺', '𝗻', '𝗼', '𝗽', '𝗾', '𝗿', '𝘀', '𝘁', '𝘂',
              '𝘃', '𝘄', '𝘅', '𝘆', '𝘇']
   
@register(outgoing=True, pattern="^.bold(?: |$)(.*)")
async def thicc(bolded):

    args = bolded.pattern_match.group(1)
    if not args:
        get = await bolded.get_reply_message()
        args = get.text   
    if not args:
        await bolded.edit("`What I am Supposed to bold for U Dumb`")
        return
    string = '  '.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            boldcharacter = boldfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, boldcharacter)
    await bolded.edit(string)
    

    
    CMD_HELP.update({
    "text_transform":
    "`.weeb` Weebify a text\
    \nUsage: .weeb <text>\
    \n`.bold` make text bold.\
    \nUsage: .bold <text>"
})
