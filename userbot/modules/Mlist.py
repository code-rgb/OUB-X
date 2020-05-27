
# @register(outgoing=True, pattern="^.helpx$")
# async def helpx(e):
#     if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
#         await e.edit("\nAvailable Modules:"
# "\n\n• 𝗔𝗱𝗺𝗶𝗻: `admin`, `blacklist`, `chat`, `gban`, `locks`"
# "\n• 𝗨𝗽𝗱𝗮𝘁𝗲𝗿: `update`"
# "\n• 𝗠𝗲𝗺𝗲𝘀: `memes`,`animate`, `anime`, `deepfry`, `dfry`, `dice`, `basketball`, `dart`,  `hazmat`, `waifu`, `memify`, `random`, `nhentai`, `uniborg_memes`, `fgban`, `carbon`,"
# "\n• 𝗔𝗻𝗱𝗿𝗼𝗶𝗱: `android`"
# "\n• 𝗔𝗳𝗸: `afk`"
# "\n• 𝗧𝗼𝗼𝗹𝘀: `all`, `antivirus`, `dictionary`,`dogbin`, `listmyusernames`, `ocr`,`qr`, `sangmata`, `currency`, `wiki`, `ud`, `tts`, `trt`, `yt`, `imdb`, `ss`, `telegraph`,`toolx`, `compress`,  `fileext`,  `rbg`, `barcode`, `quotly`, `pics`"  
# "\n• 𝗡𝗼𝘁𝗲𝘀: `notes`, `filter`, `snips`"
# "\n• 𝗧𝗲𝘅𝘁-𝗧𝗿𝗮𝗻𝘀𝗳𝗼𝗿𝗺:`figlet`, `sticklet_un`, `base64`, `hash`, `textx`"
# "\n• 𝗣𝗠: `logpms`, `nopm`, `pmpermit`"
# "\n• 𝗖𝗵𝗮𝘁: `chatinfo`, `create`, `invite`, `profile`, `welcome`, `stats` `raw`, `purge`, `purgeme`, `del`, `edit`, `sd`, `whois`"  
# "\n• 𝗥𝗲𝘁𝗮𝗿𝗱𝗲𝗱: `lydia`, `retarded`, `repeat`,  `spam`, `sed`"
# "\n• 𝗘𝘃𝗮𝗹𝗮𝘁𝗼𝗿𝘀: `eval`, `exec`, `term`, `pip`"
# "\n• 𝗚𝗶𝘁𝗵𝘂𝗯: `git`, `gcommit`, `heroku`, `repo`"
# "\n• 𝗪𝗲𝗯: `google` `reverse`, `img`, `w3m`, `weather`, `speed`, `dc`, `ping`"
# "\n• 𝗨𝗽𝗹𝗼𝗮𝗱 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱: `direct`, `aria`, `aria2`, `gdrive`, `mega`, `rip`, `download`, `webupload`"
# "\n• 𝗖𝗼𝘃𝗶𝗱: `corona`, `covid`"
# "\n• 𝗨𝘀𝗲𝗿𝗯𝗼𝘁: `useitoub`, `sleep`, `shutdown`, `restart`, `anti_spambot`,  `sysd`, `botver`, , `alive`, `dbs`,  `creator`,  `readme`, `time`, `date`" 
# "\n• 𝗦𝘁𝗶𝗰𝗸𝗲𝗿𝘀: `stickers`"  
# "\n• 𝗠𝘂𝘀𝗶𝗰: `song`, `singer`")
        
        
        
        # Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.mlist(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`  -  "
        await event.reply(string)
