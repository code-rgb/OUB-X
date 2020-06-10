from userbot import CMD_HELP

#admin.py
CMD_HELP.update({
    "admin":
    "`.promote` <username/reply> <custom rank (optional)>\
\n𝙐𝙨𝙖𝙜𝙚: Provides admin rights to the person in the chat.\
\n\n`.demote` <username/reply>\
\n𝙐𝙨𝙖𝙜𝙚: Revokes the person's admin permissions in the chat.\
\n\n`.ban` <username/reply> <reason (optional)>\
\n𝙐𝙨𝙖𝙜𝙚: Bans the person off your chat.\
\n\n`.unban` <username/reply>\
\n𝙐𝙨𝙖𝙜𝙚: Removes the ban from the person in the chat.\
\n\n`.mute` <username/reply> <reason (optional)>\
\n𝙐𝙨𝙖𝙜𝙚: Mutes the person in the chat, works on admins too.\
\n\n`.unmute` <username/reply>\
\n𝙐𝙨𝙖𝙜𝙚: Removes the person from the muted list.\
\n\n`.gmute` <username/reply> <reason (optional)>\
\n𝙐𝙨𝙖𝙜𝙚: Mutes the person in all groups you have in common with them.\
\n\n`.ungmute` <username/reply>\
\n𝙐𝙨𝙖𝙜𝙚: Reply someone's message with .ungmute to remove them from the gmuted list.\
\n\n`.zombies`\
\n𝙐𝙨𝙖𝙜𝙚: Searches for deleted accounts in a group. Use .zombies clean to remove deleted accounts from the group.\
\n\n`.admins`\
\n𝙐𝙨𝙖𝙜𝙚: Retrieves a list of admins in the chat.\
\n\n`.bots`\
\n𝙐𝙨𝙖𝙜𝙚: Retrieves a list of bots in the chat.\
\n\n`.pin` <reply/tag>\
\n𝙐𝙨𝙖𝙜𝙚: pins the replied/tagged message on the top the chat silently.\
\n\n`.cpin` <reply/tag>\
\n𝙐𝙨𝙖𝙜𝙚: pins the replied/tagged message on the top the chat LOUDLY.\
\n\n`.users` or .users <name of member>\
\n𝙐𝙨𝙖𝙜𝙚: Retrieves all (or queried) users in the chat.\
\n\n`.setgppic` <reply to image>\
\n𝙐𝙨𝙖𝙜𝙚: Changes the group's display picture.\
\n`.setflood` value.\
\n𝙐𝙨𝙖𝙜𝙚:Sets flood limit in the current chat.\
\n\n`.kick` reply or userid.\
\n𝙐𝙨𝙖𝙜𝙚: kicks user.\
\n\n𝗧𝗼 𝗪𝗮𝗿𝗻 𝗨𝘀𝗲𝗿𝘀.\
\n`.warn reason`\
\n𝙐𝙨𝙖𝙜𝙚: warns users.\
\n\n`.strongwarn` <yes/on or no/off>.\
\n𝙐𝙨𝙖𝙜𝙚:sets warn mode i.e <strong warn:bans user, soft warn: kicks user>.\
\n\n`.resetwarns`\
\n𝙐𝙨𝙖𝙜𝙚: Reset user's warns.\
\n\n`.getwarns`\
\n𝙐𝙨𝙖𝙜𝙚: Shows the reason of warning.\
\n\n`.setwarn` value.\
\n𝙐𝙨𝙖𝙜𝙚:sets warn limit.\
\n\n𝗧𝗵𝗲 𝗯𝗼𝘁 𝘄𝗶𝗹𝗹 𝗱𝗲𝗹𝗲𝘁𝗲 𝘁𝗼 𝘁𝗵𝗲 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝘄𝗵𝗲𝗻𝗲𝘃𝗲𝗿 '𝗯𝗹𝗮𝗰𝗸𝗹𝗶𝘀𝘁 𝗸𝗲𝘆𝘄𝗼𝗿𝗱' 𝗶𝘀 𝗺𝗲𝗻𝘁𝗶𝗼𝗻𝗲𝗱.\
\n`.addbl <keyword>`\
\n𝙐𝙨𝙖𝙜𝙚: Saves the message to the 'blacklist keyword.\
\n\n`.listbl`\
\n𝙐𝙨𝙖𝙜𝙚: Lists all active userbot blacklist in a chat.\
\n\n`.rmbl <keyword>`\
\n𝙐𝙨𝙖𝙜𝙚: Stops the specified blacklist."

})
  
#afk
CMD_HELP.update({
    "afk":
    "`.afk` [Optional Reason]\
\n𝙐𝙨𝙖𝙜𝙚: Sets you as afk.\nReplies to anyone who tags/PM's \
you telling them that you are AFK(reason).\n\nSwitches off AFK when you type back anything, anywhere."
})
  
#memes.py
CMD_HELP.update({
    "memes":
    "`.cowsay`\
\n𝙐𝙨𝙖𝙜𝙚: cow which says things.\
\n\n`:/`\
\n𝙐𝙨𝙖𝙜𝙚: Check yourself ;)\
\n\n`-_-`\
\n𝙐𝙨𝙖𝙜𝙚: Ok...\
\n\n`;_;`\
\n𝙐𝙨𝙖𝙜𝙚: Like `-_-` but crying.\
\n\n`.cp`\
\n𝙐𝙨𝙖𝙜𝙚: Copypasta the famous meme\
\n\n`.vapor`\
\n𝙐𝙨𝙖𝙜𝙚: Vaporize everything!\
\n\n`.str`\
\n𝙐𝙨𝙖𝙜𝙚: Stretch it.\
\n\n`.zal`\
\n𝙐𝙨𝙖𝙜𝙚: Invoke the feeling of chaos.\
\n\n`Oof`\
\n𝙐𝙨𝙖𝙜𝙚: Ooooof\
\n\n`.moon`\
\n𝙐𝙨𝙖𝙜𝙚: kensar moon animation.\
\n\n`.clock`\
\n𝙐𝙨𝙖𝙜𝙚: kensar clock animation.\
\n\n`.hi`\
\n𝙐𝙨𝙖𝙜𝙚: Greet everyone!\
\n\n`.coinflip` <heads/tails>\
\n𝙐𝙨𝙖𝙜𝙚: Flip a coin !!\
\n\n`.owo`\
\n𝙐𝙨𝙖𝙜𝙚: UwU\
\n\n`.react`\
\n𝙐𝙨𝙖𝙜𝙚: Make your userbot react to everything.\
\n\n.pro or .nub or .bye\
\n𝙐𝙨𝙖𝙜𝙚: see it yourself\
\n\n`.pickup`\
\n𝙐𝙨𝙖𝙜𝙚: Cringe & Thirsty pickup lines\
\n\n`.slap`\
\n𝙐𝙨𝙖𝙜𝙚: reply to slap them with random objects !!\
\n\n`.cry`\
\n𝙐𝙨𝙖𝙜𝙚: y u du dis, i cri.\
\n\n`.shg`\
\n𝙐𝙨𝙖𝙜𝙚: Shrug at it !!\
\n\n`.gn` or `.gm`\
\n𝙐𝙨𝙖𝙜𝙚: Says goodnight and  godmorning\
\n\n`.run`\
\n𝙐𝙨𝙖𝙜𝙚: Let Me Run, run, RUNNN!\
\n\n`.chase`\
\n𝙐𝙨𝙖𝙜𝙚: You better start running\
\n\n`.metoo`\
\n𝙐𝙨𝙖𝙜𝙚: Haha yes\
\n\n`.mock`\
\n𝙐𝙨𝙖𝙜𝙚: Do it and find the real fun.\
\n\n`.clap`\
\n𝙐𝙨𝙖𝙜𝙚: Praise people!\
\n\n`.f` <emoji/character>\
\n𝙐𝙨𝙖𝙜𝙚: Pay Respects.\
\n\n`.bt`\
\n𝙐𝙨𝙖𝙜𝙚: Believe me, you will find this useful.\
\n\n`.type`\
\n𝙐𝙨𝙖𝙜𝙚: Just a small command to make your keyboard become a typewriter!\
\n\n`.lfy` <query>\
\n𝙐𝙨𝙖𝙜𝙚: Let me Google that for you real quick !!\
\n\n`.boobs`\
\n𝙐𝙨𝙖𝙜𝙚: Get b00bs imej\
\n\n`.butts`\
\n𝙐𝙨𝙖𝙜𝙚: Get 🅱️utts imej\
\n\n`.decide` [Alternates: (`.yes`, `.no`, `.maybe`)]\
\n𝙐𝙨𝙖𝙜𝙚: Make a quick decision.\
\n\n`.scam` <action> <time>\
\n[Available Actions: (`typing`, `contact`, `game`, `location`, `voice`, `round`, `video`, `photo`, `document`, `cancel`)]\
\n𝙐𝙨𝙖𝙜𝙚: Create fake chat actions, for fun. (Default action: typing)\
\n\n...𝑨𝒏𝒅 𝒎𝒂𝒏𝒚 𝒎𝒐𝒓𝒆.\
\n| `.nou` | `.bot` | `.gay` | `.gey` | `.tf` | `.paw` | `.taco` | `.nih` |\
\n| `.fag` | `.gtfo` | `.stfu` | `.lol` | `.lols` | `.lool` | `.fail` | `.love` |\
\n| `.rain` | `.earth` | `.ii` | `.tolol` |\
\n\n\nThanks to 🅱️ottom🅱️ext🅱️ot (@NotAMemeBot) for some of these."
})

#android.py
CMD_HELP.update({
    "android":
    ".magisk"
    "\nGet latest Magisk releases"
    "\n\n.pixeldl **<download.pixelexperience.org>**"
    "\n𝙐𝙨𝙖𝙜𝙚: Download pixel experience ROM into your userbot server."
    "\n\n.twrp <codename>"
    "\n𝙐𝙨𝙖𝙜𝙚: Get latest twrp download for android device."
})

#animate.py
CMD_HELP.update({
    "animate":
    "\nHey! try the below commands.\
     \n`\n.load`\
     \n`.square`\
     \n`.up`\
     \n`.round`\
     \n`.heart`\
     \n`.anim`\
     \n`.monkey`\
     \n`.hand`"
})

#all.py
CMD_HELP.update({
    "all":
    ".all\
\n𝙐𝙨𝙖𝙜𝙚: A Plugin to tagall in the chat."
})  


#anime_chooser.py
CMD_HELP.update({
        "anime":  \
        "Anime random generator \
        \n𝙐𝙨𝙖𝙜𝙚: .(genre) number of times(interger)\
        \n\nAvailable commands: \
        \n.action \
          \nInfo: Generate anime genre action.\
          \n\n.adventure \
          \nInfo: Generate anime genre adventure.\
          \n\n.harem \
          \nInfo: Generate anime genre harem UwU.\
          \n\n.romance \
          \nInfo: Generate anime genre romance.\
          \n\n.slice \
          \nInfo: Generate anime genre slice of life.\
          \n\n.mecha \
          \nInfo: Generate anime genre mecha.\
          \n\n.isekai \
          \nInfo: Generate anime genre isekai."
          
    })

#anti_spambot.py
CMD_HELP.update({
    'anti_spambot':
    "If enabled in config.env or env var,\
        \nthis module will 𝗯𝗮𝗻(𝗼𝗿 𝗶𝗻𝗳𝗼𝗿𝗺 𝘁𝗵𝗲 𝗮𝗱𝗺𝗶𝗻𝘀 𝗼𝗳 𝘁𝗵𝗲 𝗴𝗿𝗼𝘂𝗽 𝗮𝗯𝗼𝘂𝘁) the\
        \n𝘀𝗽𝗮𝗺𝗺𝗲𝗿(𝘀) if they match the userbot's anti-spam algorithm."
})

#antivirus.py
CMD_HELP.update({
"antivirus": ".scan\
    \n𝙐𝙨𝙖𝙜𝙚: Type .scan to remove virus"
})

#aria.py
CMD_HELP.update({
    "aria":
    "`.aurl` [URL] (or) .amag [Magnet Link] (or) .ator [path to torrent file]\
    \n𝙐𝙨𝙖𝙜𝙚: Downloads the file into your userbot server storage.\
    \n\n`.apause` (or) .aresume\
    \n𝙐𝙨𝙖𝙜𝙚: Pauses/resumes on-going downloads.\
    \n\n`.aclear`\
    \n𝙐𝙨𝙖𝙜𝙚: Clears the download queue, deleting all on-going downloads.\
    \n\n`.ashow`\
    \n𝙐𝙨𝙖𝙜𝙚: Shows progress of the on-going downloads."
})





#carbon.py
CMD_HELP.update({
    "carbon":
    "`.carbon` value <values=1,2,3,4,5>\
        \n𝙐𝙨𝙖𝙜𝙚:reply or type .carbon value and beautify your text."
})

#changelog.py
CMD_HELP.update({
    'update':
    ".chl\
\n𝙐𝙨𝙖𝙜𝙚: Checks if the main userbot repository has any updates and shows a changelog if so.\
\n\n.update\
\n𝙐𝙨𝙖𝙜𝙚: Updates your userbot, if there are any updates in the main userbot repository."
})

#chat.py
CMD_HELP.update({
    "chat":
    ".chatid\
\n𝙐𝙨𝙖𝙜𝙚: Fetches the current chat's ID\
\n\n.userid\
\n𝙐𝙨𝙖𝙜𝙚: Fetches the ID of the user in reply, if its a forwarded message, finds the ID for the source.\
\n\n.log\
\n𝙐𝙨𝙖𝙜𝙚: Forwards the message you've replied to in your bot logs group.\
\n\n.kickme\
\n𝙐𝙨𝙖𝙜𝙚: Leave from a targeted group.\
\n\n.unmutechat\
\n𝙐𝙨𝙖𝙜𝙚: Unmutes a muted chat.\
\n\n.mutechat\
\n𝙐𝙨𝙖𝙜𝙚: Allows you to mute any chat.\
\n\n.link <username/userid> : <optional text> (or) reply to someone's message with .link <optional text>\
\n𝙐𝙨𝙖𝙜𝙚: Generate a permanent link to the user's profile with optional custom text.\
\n\n.regexninja on/off\
\n𝙐𝙨𝙖𝙜𝙚: Globally enable/disables the regex ninja module.\
\nRegex Ninja module helps to delete the regex bot's triggering messages."
})

#chatinfo.py
CMD_HELP.update({
        "chatinfo":
        ".chatinfo [optional: <reply/tag/chat id/invite link>]\
            \n𝙐𝙨𝙖𝙜𝙚: Gets info of a chat. Some info might be limited due to missing permissions.\
            \n\n.invite\
            \n𝙐𝙨𝙖𝙜𝙚:Invites users to a chat, not to a private message."
})

#covidv2.py
CMD_HELP.update(
    {"corona": ".corona [country]\n"
     "𝙐𝙨𝙖𝙜𝙚: Corona Virus stats."})

#covid.py
CMD_HELP.update({
        "covid": 
        ".covid <country>"
        "\n𝙐𝙨𝙖𝙜𝙚: Get an information about data covid-19 in your country.\n"
    })

#create.py
CMD_HELP.update({
    "create": "\
Create\
\n𝙐𝙨𝙖𝙜𝙚: Create Channel, Group & Group With Bot.\
\n\n.create g <group name>\
\n𝙐𝙨𝙖𝙜𝙚: Create a Private Group.\
\n\n.create b <group name>\
\n𝙐𝙨𝙖𝙜𝙚: Create a Group with Bot.\
\n\n.create c <channel name>\
\n𝙐𝙨𝙖𝙜𝙚: Create a Channel.\
"})

#dbs.py
CMD_HELP.update(
    {"dbs": ".dbs\n"
     "𝙐𝙨𝙖𝙜𝙚: Shows database related info."})

#deepfry.py
CMD_HELP.update({
"deepfry": ".deepfry\
    \n𝙐𝙨𝙖𝙜𝙚: Reply .deepfry 1-5 to an image or sticker to deep fry it!. "
})   

#dfry.py
CMD_HELP.update({
    "dfry":
    ".dfry or .dfry [level(1-8)]"
    "\n𝙐𝙨𝙖𝙜𝙚: deepfry image/sticker from the reply."
    "\n@image_deepfrybot"
})

#dice_dart_basketball.py

CMD_HELP.update({
    "dice":
    ".dice or .dice 1 to 6 any value\
\n𝙐𝙨𝙖𝙜𝙚: hahaha just a magic.\
\nwarning: `you would be in trouble if you input any other value than mentioned.`"
})    

CMD_HELP.update({
    "basketball":
    ".basketball or .basketball 1 to 5 any value\
\n𝙐𝙨𝙖𝙜𝙚: hahaha just a magic.\
\nwarning: `you would be in trouble if you input any other value than mentioned.`"
})    

CMD_HELP.update({
    "dart":
    ".dart or .dart 1 to 6 any value\
\n𝙐𝙨𝙖𝙜𝙚: hahaha just a magic.\
\nwarning: `you would be in trouble if you input any other value than mentioned.`"
})   

#dictionary.py
CMD_HELP.update({
        "dictionary": 
        ".meaning <word>"
        "\n𝙐𝙨𝙖𝙜𝙚: Atleast it works :p\n"
    })

#direct_link.py
CMD_HELP.update({
    "direct":
    ".direct <url>\n"
    "𝙐𝙨𝙖𝙜𝙚: Reply to a link or paste a URL to\n"
    "generate a direct download link\n\n"
    "List of supported URLs:\n"
    "`Google Drive - Cloud Mail - Yandex.Disk - AFH - "
    "ZippyShare - MediaFire - SourceForge - OSDN - GitHub`"
})

#dogbin.py
CMD_HELP.update({
    "dogbin":
    ".paste <text/reply>\
\n𝙐𝙨𝙖𝙜𝙚: Create a paste or a shortened url using dogbin (https://del.dog/)\
\n\n.getpaste\
\n𝙐𝙨𝙖𝙜𝙚: Gets the content of a paste or shortened url from dogbin (https://del.dog/)"
})

#evaluator.py
CMD_HELP.update({"eval": ".eval 2 + 3\n𝙐𝙨𝙖𝙜𝙚: Evalute mini-expressions."})
CMD_HELP.update(
    {"exec": ".exec print('hello')\n𝙐𝙨𝙖𝙜𝙚: Execute small python scripts."})
CMD_HELP.update(
    {"term": ".term ls\n𝙐𝙨𝙖𝙜𝙚: Run bash commands and scripts on your server."})

#fgban.py
CMD_HELP.update(
    {"fgban": ".fgban\
    \n𝙐𝙨𝙖𝙜𝙚: Type .fgban or Reply .fgban reason and see it yourself."})

#figlet.py
CMD_HELP.update({
        "figlet":
        "`.figlet`"
          "\n𝙐𝙨𝙖𝙜𝙚: Enhance ur text to strip line with anvil."
          "\n\n𝗘𝘅𝗮𝗺𝗽𝗹𝗲: `.figlet TEXT.STYLE`"
          "\n𝗦𝗧𝗬𝗟𝗘 𝗟𝗜𝗦𝗧: `slant`, `3D`, `5line`, `alpha`, `banner`, `doh`, `iso`, `letter`, `allig`, `dotm`, `bubble`, `bulb`, `digi`"
    })

#fileext.py
CMD_HELP.update({
        "fileext": 
        ".fileext <ext>\
          \n𝙐𝙨𝙖𝙜𝙚: get information about file extentions.\n"
    })

#filter.py
CMD_HELP.update({
    "filter":
    ".filters\
    \n𝙐𝙨𝙖𝙜𝙚: Lists all active userbot filters in a chat.\
    \n\n.filter <keyword> <reply text> or reply to a message with .filter <keyword>\
    \n𝙐𝙨𝙖𝙜𝙚: Saves the replied message as a reply to the 'keyword'.\
    \nThe bot will reply to the message whenever 'keyword' is mentioned.\
    \nWorks with everything from files to stickers.\
    \n\n.stop <filter>\
    \n𝙐𝙨𝙖𝙜𝙚: Stops the specified filter.\
    \n\n.rmbotfilters <marie/rose>\
    \n𝙐𝙨𝙖𝙜𝙚: Removes all filters of admin bots (Currently supported: Marie, Rose and their clones.) in the chat."
})

#gban.py
CMD_HELP.update({
    "gban": "\
`.gban reason`\
\n𝙐𝙨𝙖𝙜𝙚: Globally Ban users from all the Group Administrations bots where you are SUDO.\
\n\n`.ungban reason`\
\n𝙐𝙨𝙖𝙜𝙚: Globally unBan users from all the Group Administrations bots where you are SUDO"
})

#gdrive.py
CMD_HELP.update({
    "gdrive":
    "`.gdauth`"
    "\n𝙐𝙨𝙖𝙜𝙚: generate token to enable all cmd google drive service."
    "\nThis only need to run once in life time."
    "\n\n`.gdreset`"
    "\n𝙐𝙨𝙖𝙜𝙚: reset your token if something bad happened or change drive acc."
    "\n\n`.gd`"
    "\n𝙐𝙨𝙖𝙜𝙚: Upload file from local or uri/url/drivelink into google drive."
    "\nfor drivelink it's upload only if you want to."
    "\n\n`.gdabort`"
    "\n𝙐𝙨𝙖𝙜𝙚: Abort process uploading or downloading."
    "\n\n`.gdlist`"
    "\n𝙐𝙨𝙖𝙜𝙚: Get list of folders and files with default size 50."
    "\nUse flags `-l range[1-1000]` for limit output."
    "\nUse flags `-p parents-folder_id` for lists given folder in gdrive."
    "\n\n`.gdf mkdir`"
    "\n𝙐𝙨𝙖𝙜𝙚: Create gdrive folder."
    "\n\n`.gdf check`"
    "\n𝙐𝙨𝙖𝙜𝙚: Check file/folder in gdrive."
    "\n\n`.gdf rm`<file/folder>name"
    "\n𝙐𝙨𝙖𝙜𝙚: Delete files/folders in gdrive."
    "\nCan't be undone, this method skipping file trash, so be caution..."
    "\n\n`.gdfset put`"
    "\n𝙐𝙨𝙖𝙜𝙚: Change upload directory in gdrive."
    "\n\n`.gdfset rm`"
    "\n𝙐𝙨𝙖𝙜𝙚: remove set parentId from cmd\n`.gdfset put` "
    "into **G_DRIVE_FOLDER_ID** and if empty upload will go to root."
    "\n\nNOTE:"
    "\nfor `.gdlist` you can combine -l and -p flags with or without name "
    "at the same time, it must be `-l` flags first before use `-p` flags.\n"
    "And by default it lists from latest 'modifiedTime' and then folders."
})

#getsong.py
CMD_HELP.update({
    "song":
        "`.song` <song name> "
        "\n𝙐𝙨𝙖𝙜𝙚: Finding and uploading song.\n"
        "`.smd` <song tittle> "
        "\n𝙐𝙨𝙖𝙜𝙚: Download music from spotify"
})

#github.py
CMD_HELP.update({"git": "Like .whois but for GitHub usernames."})

#gitupload.py
CMD_HELP.update({
    "gcommit": 
    ".gcommit\
    \n\n𝙐𝙨𝙖𝙜𝙚: GITHUB File Uploader Plugin for userbot. Heroku Automation should be Enabled. Else u r not that lazy , For lazy people\
\n\nInstructions:- Set GITHUB_ACCESS_TOKEN and GIT_REPO_NAME Variables in Heroku vars First\
\n\n.gcommit reply_to_any_plugin can be any type of file too. but for plugin must be in .py ."})


#hazmat.py
CMD_HELP.update({
    "hazmat":
    "`.hz` or `.hz [flip, x2, rotate (degree), background (number), black]`"
    "\n𝙐𝙨𝙖𝙜𝙚: Reply to a image / sticker to suit up!"
})

#help_on_update.py
CMD_HELP.update({
    "useitoub":
    ".useitoub\
\n𝙐𝙨𝙖𝙜𝙚: Provide links to update repo guides while you keep your changes on the floor.\
\n.varoub\
\n𝙐𝙨𝙖𝙜𝙚: Provide vars to cross check for you."
})

#heroku.py
CMD_HELP.update({
    "heroku":
    ">.`usage`"
    "\n𝙐𝙨𝙖𝙜𝙚: Check your heroku dyno hours remaining"
    "\n\n>`.set var <NEW VAR> <VALUE>`"
    "\n𝙐𝙨𝙖𝙜𝙚: add new variable or update existing value variable"
    "\n!!! WARNING !!!, after setting a variable the bot will restarted"
    "\n\n>`.get var or .get var <VAR>`"
    "\n𝙐𝙨𝙖𝙜𝙚: get your existing varibles, use it only on your private group!"
    "\nThis returns all of your private information, please be caution..."
    "\n\n>`.del var <VAR>`"
    "\n𝙐𝙨𝙖𝙜𝙚: delete existing variable"
    "\n!!! WARNING !!!, after deleting variable the bot will restarted"
})

#invite.py
CMD_HELP.update({
    'invite':
    '.invite <username> \
        \n𝙐𝙨𝙖𝙜𝙚: Invite some user or bots if u want.'
})

#listmyusernames.py
CMD_HELP.update({
   "listmyusernames":
  "\ndo this in your private group for security purpose.\
   \n-listmyusernames \
\n𝙐𝙨𝙖𝙜𝙚: Provides all titles according to the usernames reserved by you.\
  -listmychatids \
\n𝙐𝙨𝙖𝙜𝙚: Provides all Chat IDs reserved by you."
})

#locks.py
CMD_HELP.update({
    "locks":
    ".lock <all (or) type(s)> or .unlock <all (or) type(s)>\
\n𝙐𝙨𝙖𝙜𝙚: Allows you to lock/unlock some common message types in the chat.\
[NOTE: Requires proper admin rights in the chat !!]\
\n\nAvailable message types to lock/unlock are: \
\n`all, msg, media, sticker, gif, game, inline, poll, invite, pin, info`"
})

#logpms.py
CMD_HELP.update({
    "logpms":
    "If you don't want chat logs than use `.nolog` , for opposite use `.log`. Default is .log enabled\
\n𝙐𝙨𝙖𝙜𝙚: This will now log chat msgs to your PM_LOGGR_BOT_API_ID.\
\nnotice: now you can totally disable pm logs by adding heroku vars PM_LOGGR_BOT_API_ID by providing a valid group ID and NC_LOG_P_M_S True or False,\
\nwhere False means no pm logs at all..enjoy.. update and do add above mentioned vars."
})  

#lydia.py
CMD_HELP.update({
    "lydia":
    ".addcf <username/reply>\
\n𝙐𝙨𝙖𝙜𝙚: add's lydia auto chat request in the chat.\
\n\n.remcf <username/reply>\
\n𝙐𝙨𝙖𝙜𝙚: remove's lydia auto chat request in the chat.\
\n\n.repcf <username/reply>\
\n𝙐𝙨𝙖𝙜𝙚: starts lydia repling to perticular person in the chat.\
\n Note:  get your value from https://coffeehouse.intellivoid.info/dashboard."
})

#mega_downloader.py
CMD_HELP.update({
    "mega":
    ".mega <mega url>\n"
    "𝙐𝙨𝙖𝙜𝙚: Reply to a mega link or paste your mega link to\n"
    "download the file into your userbot server\n\n"
    "Only support for *FILE* only."
})

#memex.py waifu.py
CMD_HELP.update({
    "waifu":
    ".waifu [text]\
\n𝙐𝙨𝙖𝙜𝙚: for custom anime girl stickers. \
\n\n.memex\
\n𝙐𝙨𝙖𝙜𝙚: for custom meme stickers."})

#memeify.py
CMD_HELP.update({
    "memify": 
        "`.mmf` texttop ; textbottom\
        \n𝙐𝙨𝙖𝙜𝙚: Reply a sticker/image/gif and send with cmd."
})

#misc.py
CMD_HELP.update({
    'random':
    '.random <item1> <item2> ... <itemN>\
\n𝙐𝙨𝙖𝙜𝙚: Get a random item from the list of items.'
})

CMD_HELP.update({
    'sleep':
    '.sleep <seconds>\
\n𝙐𝙨𝙖𝙜𝙚: Userbots get tired too. Let yours snooze for a few seconds.'
})

CMD_HELP.update({
    "shutdown":
    ".shutdown\
\n𝙐𝙨𝙖𝙜𝙚: Sometimes you need to shut down your bot. Sometimes you just hope to\
hear Windows XP shutdown sound... but you don't."
})




CMD_HELP.update({
    'repo':
    '.repo\
\n𝙐𝙨𝙖𝙜𝙚: If you are curious what makes the userbot work, this is what you need.'
})

CMD_HELP.update({
    'myrepo':
    '.myrepo\
\n𝙐𝙨𝙖𝙜𝙚: If you are curious which is your personal repo, this is what you have.'
})

CMD_HELP.update({
    "readme":
    ".readme\
\n𝙐𝙨𝙖𝙜𝙚: Provide links to setup the userbot and it's modules."
})

CMD_HELP.update(
    {"creator": ".creator\
\n𝙐𝙨𝙖𝙜𝙚: Know who created this awesome userbot !!"})

CMD_HELP.update({
    "repeat":
    ".repeat <no.> <text>\
\n𝙐𝙨𝙖𝙜𝙚: Repeats the text for a number of times. Don't confuse this with spam tho."
})

CMD_HELP.update({"restart": ".restart\
\n𝙐𝙨𝙖𝙜𝙚: Restarts the bot !!"})

CMD_HELP.update({
    "raw":
    ".raw\
\n𝙐𝙨𝙖𝙜𝙚: Get detailed JSON-like formatted data about replied message."
})

#nhentai.py
CMD_HELP.update({
"nhentai": 
".nhentai <link / code> \
\n𝙐𝙨𝙖𝙜𝙚: view nhentai in telegra.ph XD\n"})

#notes.py
CMD_HELP.update({
    "notes":
    "\
#<notename>\
\n𝙐𝙨𝙖𝙜𝙚: Gets the specified note.\
\n\n.save <notename> <notedata> or reply to a message with .save <notename>\
\n𝙐𝙨𝙖𝙜𝙚: Saves the replied message as a note with the notename. (Works with pics, docs, and stickers too!)\
\n\n.notes\
\n𝙐𝙨𝙖𝙜𝙚: Gets all saved notes in a chat.\
\n\n.clear <notename>\
\n𝙐𝙨𝙖𝙜𝙚: Deletes the specified note.\
\n\n.rmbotnotes <marie/rose>\
\n𝙐𝙨𝙖𝙜𝙚: Removes all notes of admin bots (Currently supported: Marie, Rose and their clones.) in the chat."
})

#ocr.py
CMD_HELP.update({
    'ocr':
    ".ocr <language>\n𝙐𝙨𝙖𝙜𝙚: Reply to an image or sticker to extract text from it.\n\nGet language codes from [here](https://ocr.space/ocrapi)"
})

#pics.py
CMD_HELP.update({
    "pics": ".pic reply any document image\nUsage : Convert any Document Image to Full Size Image"
})

#pmmute.py
CMD_HELP.update({
    "nopm":
    "`.pmute`\
\n𝙐𝙨𝙖𝙜𝙚: Reply .pmute and it will mute that person in pm  \
\n\n.`punmute`\
\n𝙐𝙨𝙖𝙜𝙚:Reply .punmute and it will unmute that person in pm \
"
})

#pmpermit.py
CMD_HELP.update({
    "pmpermit":
    "\
.approve\
\n𝙐𝙨𝙖𝙜𝙚: Approves the mentioned/replied person to PM.\
\n\n.disapprove\
\n𝙐𝙨𝙖𝙜𝙚: Disapproves the mentioned/replied person to PM.\
\n\n.block\
\n𝙐𝙨𝙖𝙜𝙚: Blocks the person.\
\n\n.unblock\
\n𝙐𝙨𝙖𝙜𝙚: Unblocks the person so they can PM you.\
\n\n.notifoff\
\n𝙐𝙨𝙖𝙜𝙚: Clears/Disables any notifications of unapproved PMs.\
\n\n.notifon\
\n𝙐𝙨𝙖𝙜𝙚: Allows notifications for unapproved PMs."
})

#profile.py
CMD_HELP.update({
    "profile":
    ".username <new_username>\
\n𝙐𝙨𝙖𝙜𝙚: Changes your Telegram username.\
\n\n.name <firstname> or .name <firstname> <lastname>\
\n𝙐𝙨𝙖𝙜𝙚: Changes your Telegram name.(First and last name will get split by the first space)\
\n\n.setpfp\
\n𝙐𝙨𝙖𝙜𝙚: Reply with .setpfp to an image to change your Telegram profie picture.\
\n\n.setbio <new_bio>\
\n𝙐𝙨𝙖𝙜𝙚: Changes your Telegram bio.\
\n\n.delpfp or .delpfp <number>/<all>\
\n𝙐𝙨𝙖𝙜𝙚: Deletes your Telegram profile picture(s).\
\n\n.reserved\
\n𝙐𝙨𝙖𝙜𝙚: Shows usernames reserved by you.\
\n\n.count\
\n𝙐𝙨𝙖𝙜𝙚: Counts your groups, chats, bots etc..."
})


#purge.py
CMD_HELP.update({
    'purge':
    '.purge\
        \n𝙐𝙨𝙖𝙜𝙚: Purges all messages starting from the reply.'
})

CMD_HELP.update({
    'purgeme':
    '.purgeme <x>\
        \n𝙐𝙨𝙖𝙜𝙚: Deletes x amount of your latest messages.'
})

CMD_HELP.update({"del": ".del\
\n𝙐𝙨𝙖𝙜𝙚: Deletes the message you replied to."})

CMD_HELP.update({
    'edit':
    ".edit <newmessage>\
\n𝙐𝙨𝙖𝙜𝙚: Replace your last message with <newmessage>."
})

CMD_HELP.update({
    'sd':
    '.sd <x> <message>\
\n𝙐𝙨𝙖𝙜𝙚: Creates a message that selfdestructs in x seconds.\
\nKeep the seconds under 100 since it puts your bot to sleep.'
})


#qrcode.py
CMD_HELP.update({
    'qr':
    ".makeqr <content>\
\n𝙐𝙨𝙖𝙜𝙚: Make a QR Code from the given content.\
\nExample: .makeqr www.google.com\
\nNote: use .decode <reply to barcode/qrcode> to get decoded content."
})

CMD_HELP.update({
    'barcode':
    ".barcode <content>\
\n𝙐𝙨𝙖𝙜𝙚: Make a BarCode from the given content.\
\nExample: .barcode www.google.com\
\nNote: use .decode <reply to barcode/qrcode> to get decoded content."
})

#quotly.py
CMD_HELP.update({
        "quotly": 
        ".q reply_message. \
          \n𝙐𝙨𝙖𝙜𝙚: Enhance ur text to sticker. \
          \nNote: please add API_TOKEN and API_URL in Heroku vars. \
          \n you can get those from http://antiddos.systems/. "
    })

#remove_bg.py
CMD_HELP.update({
    "rbg":
    ".rbg <Link to Image> or reply to any image (Warning: does not work on stickers.)\
\n𝙐𝙨𝙖𝙜𝙚: Removes the background of images, using remove.bg API"
})   

#reverse.py
CMD_HELP.update({
    'reverse':
    '.reverse\
        \n𝙐𝙨𝙖𝙜𝙚: Reply to a pic/sticker to revers-search it on Google Images !!'
})

#sangmata.py
CMD_HELP.update({
        "sangmata": 
        ".sg \
          \n𝙐𝙨𝙖𝙜𝙚: View user history.\n"
    })

#scrapers.py
CMD_HELP.update({
    'img':
    '.img <search_query>\
        \n𝙐𝙨𝙖𝙜𝙚: Does an image search on Google and shows 5 images.'
})
CMD_HELP.update({
    'currency':
    '.currency <amount> <from> <to>\
        \n𝙐𝙨𝙖𝙜𝙚: Converts various currencies for you.'
})
CMD_HELP.update({
    'carbon':
    '.carbon <text> [or reply]\
        \n𝙐𝙨𝙖𝙜𝙚: Beautify your code using carbon.now.sh\nUse .crblang <text> to set language for your code.'
})
CMD_HELP.update(
    {'google': '.google <query>\
        \n𝙐𝙨𝙖𝙜𝙚: Does a search on Google.'})
CMD_HELP.update(
    {'wiki': '.wiki <query>\
        \n𝙐𝙨𝙖𝙜𝙚: Does a search on Wikipedia.'})
CMD_HELP.update(
    {'ud': '.ud <query>\
        \n𝙐𝙨𝙖𝙜𝙚: Does a search on Urban Dictionary.'})
CMD_HELP.update({
    'tts':
    '.tts <text> [or reply]\
        \n𝙐𝙨𝙖𝙜𝙚: Translates text to speech for the language which is set.\nUse .lang tts <language code> to set language for tts. (Default is English.)'
})
CMD_HELP.update({
    'trt':
    '.trt <text> [or reply]\
        \n𝙐𝙨𝙖𝙜𝙚: Translates text to the language which is set.\nUse .lang trt <language code> to set language for trt. (Default is English)'
})
CMD_HELP.update({'yt': '.yt <text>\
        \n𝙐𝙨𝙖𝙜𝙚: Does a YouTube search.'})
CMD_HELP.update(
    {"imdb": ".imdb <movie-name>\nShows movie info and other stuff."})
CMD_HELP.update({
    'rip':
    '.ripaudio <url> or ripvideo <url>\
        \n𝙐𝙨𝙖𝙜𝙚: Download videos and songs from YouTube (and [many other sites](https://ytdl-org.github.io/youtube-dl/supportedsites.html)).'
})

#screencapture.py
CMD_HELP.update({
    "ss":
    ".ss <url>\
    \n𝙐𝙨𝙖𝙜𝙚: Takes a screenshot of a website and sends the screenshot.\
    \nExample of a valid URL : `https://www.google.com`"
})

#sed.py
CMD_HELP.update({
    "sed":
    ".s<delimiter><old word(s)><delimiter><new word(s)>\
    \n𝙐𝙨𝙖𝙜𝙚: Replaces a word or words using sed.\
    \nDelimiters: `/, :, |, _`"
})

#singer.py
CMD_HELP.update({
"singer": ".singer\
    \n𝙐𝙨𝙖𝙜𝙚: Type 𝙐𝙨𝙖𝙜𝙚: .singer Duman - Haberin Yok Ölüyorum"
})

#snips.py
CMD_HELP.update({
    "snips":
    "\
$<snip_name>\
\n𝙐𝙨𝙖𝙜𝙚: Gets the specified snip, anywhere.\
\n\n.snip <name> <data> or reply to a message with .snip <name>\
\n𝙐𝙨𝙖𝙜𝙚: Saves the message as a snip (global note) with the name. (Works with pics, docs, and stickers too!)\
\n\n.snips\
\n𝙐𝙨𝙖𝙜𝙚: Gets all saved snips.\
\n\n.remsnip <snip_name>\
\n𝙐𝙨𝙖𝙜𝙚: Deletes the specified snip.\
"
})

#spam.py
CMD_HELP.update({
    "spam":
    ".cspam <text>\
\n𝙐𝙨𝙖𝙜𝙚: Spam the text letter by letter.\
\n\n.spam <count> <text>\
\n𝙐𝙨𝙖𝙜𝙚: Floods text in the chat !!\
\n\n.wspam <text>\
\n𝙐𝙨𝙖𝙜𝙚: Spam the text word by word.\
\n\n.picspam <count> <link to image/gif>\
\n𝙐𝙨𝙖𝙜𝙚: As if text spam was not enough !!\
\n\n.delayspam <delay> <count> <text>\
\n𝙐𝙨𝙖𝙜𝙚: .bigspam but with custom delay.\
\n\n\nNOTE : Spam at your own risk !!"
})

#stickers.py
CMD_HELP.update({
    "stickers":
    ".kang\
\n𝙐𝙨𝙖𝙜𝙚: Reply .kang to a sticker or an image to kang it to your userbot pack.\
\n\n.kang [emoji('s)]\
\n𝙐𝙨𝙖𝙜𝙚: Works just like .kang but uses the emoji('s) you picked.\
\n\n.kang [number]\
\n𝙐𝙨𝙖𝙜𝙚: Kang's the sticker/image to the specified pack but uses 🤔 as emoji.\
\n\n.kang [emoji('s)] [number]\
\n𝙐𝙨𝙖𝙜𝙚: Kang's the sticker/image to the specified pack and uses the emoji('s) you picked.\
\n\n.stkrinfo\
\n𝙐𝙨𝙖𝙜𝙚: Gets info about the sticker pack.\
\n\n.getsticker\
\n𝙐𝙨𝙖𝙜𝙚: reply to a sticker to get 'PNG' file of sticker."
})

#sticklet_un.py
CMD_HELP.update({
"sticklet_un": ".un\
    \n𝙐𝙨𝙖𝙜𝙚: Type .un text and generate rgb sticker. "
}) 
# system_stat.py
CMD_HELP.update(
    {"sysd": ".sysd\
    \n𝙐𝙨𝙖𝙜𝙚: Shows system information using neofetch."})
CMD_HELP.update({"botver": ".botver\
    \n𝙐𝙨𝙖𝙜𝙚: Shows the userbot version."})
CMD_HELP.update(
    {"pip": ".pip <module(s)>\
    \n𝙐𝙨𝙖𝙜𝙚: Does a search of pip modules(s)."})
CMD_HELP.update({
    "alive":
    ".alive\
    \n𝙐𝙨𝙖𝙜𝙚: Type .alive to see wether your bot is working or not.\
    \n\n.aliveu <text>\
    \n𝙐𝙨𝙖𝙜𝙚: Changes the 'user' in alive to the text you want.\
    \n\n.resetalive\
    \n𝙐𝙨𝙖𝙜𝙚: Resets the user to default."
})

#telegraph.py
CMD_HELP.update({
    "telegraph": ".tg media as reply to a media \
        \n & .tg text as reply to a large text \
        \n𝙐𝙨𝙖𝙜𝙚: Upload text & media on Telegraph.\
        \nNotice: you are required to set TELEGRAPH_SHORT_NAME in Heroku vars so that your bot remains alive \
        \nor else your bot will die."
})

#time.py
CMD_HELP.update({
    "time":
    ".time <country name/code> <timezone number>"
    "\n𝙐𝙨𝙖𝙜𝙚: Get the time of a country. If a country has "
    "multiple timezones, it will list all of them "
    "and let you select one."
})
CMD_HELP.update({
    "date":
    ".date <country name/code> <timezone number>"
    "\n𝙐𝙨𝙖𝙜𝙚: Get the date of a country. If a country has "
    "multiple timezones, it will list all of them "
    "and let you select one."
})

#toolx.py
CMD_HELP.update({
    "toolx":
    "`.app`\
\n𝙐𝙨𝙖𝙜𝙚: type .app name and get app details.\
\n\n`.undlt`\
\n𝙐𝙨𝙖𝙜𝙚: undo deleted message but u need admin permission.\
\n\n`.calc`\
\n𝙐𝙨𝙖𝙜𝙚:.calc <term1><operator><term2>\nFor eg .calc 02*02 or 99*99 (the zeros are important) (two terms and two digits max).\
\n\n`.remove`\
\n𝙐𝙨𝙖𝙜𝙚:.remove d or y or m or w or o or q or r.\n(d=deletedaccount y=userstatsempty m=userstatsmonth w=userstatsweek o=userstatsoffline q=userstatsonline r=userstatsrecently).\
\n\n`.xcd`\
\n𝙐𝙨𝙖𝙜𝙚: type xcd <query>.ps:i have no damm idea how it works 🤷\
\n\n`.grab` <count>\
\n𝙐𝙨𝙖𝙜𝙚:replay .grab or .grab <count> to grab profile picture.\
\n\n`.rnupload` filename.extenstion\
\n𝙐𝙨𝙖𝙜𝙚:reply to a sticker and type .rnupload xyz.jpg\
\n\n`.clone` @username\
\n𝙐𝙨𝙖𝙜𝙚: clone you whole freking account except username so stay safe\
\n\n`.res`\
\n𝙐𝙨𝙖𝙜𝙚: type account,channel,group or bot username and reply with .res and check restriction\
\n\n`.watch` <movie/tv> show\
\n𝙐𝙨𝙖𝙜𝙚:know details about particular movie/show."         
})

#uniborg_memes.py
CMD_HELP.update({
    "uniborg_memes":
    ".eye\
\n𝙐𝙨𝙖𝙜𝙚: see it yourself.\
\n\n.earth\
\n𝙐𝙨𝙖𝙜𝙚: spins like earth 🌎🌎\
\n\n.bombs\
\n𝙐𝙨𝙖𝙜𝙚: For bombing tg 🤣🤣\
\n\n.gift\
\n𝙐𝙨𝙖𝙜𝙚: Well it's a gift i can't say what's inside 😁😁!\
\n\n.police\
\n𝙐𝙨𝙖𝙜𝙚: Time to go to jail 😔😔.\
\n\n.kill\
\n𝙐𝙨𝙖𝙜𝙚: For killing your enemies 🔫🔫 !!\
\n\n.os\
\n𝙐𝙨𝙖𝙜𝙚: see it yourself 🤐🤐.\
\n\n.isro\
\n𝙐𝙨𝙖𝙜𝙚: For calling aliens 👽👽 :P\
\n\n.gangstar\
\n𝙐𝙨𝙖𝙜𝙚:U becum gengstar 🤠🤠.\
\n\n.hack\
\n𝙐𝙨𝙖𝙜𝙚: For hacking telegram🖥️🖥️.\
\n\n.hypno\
\n𝙐𝙨𝙖𝙜𝙚: Oh fek my eyes 👀\
\n\n.whatsapp\
\n𝙐𝙨𝙖𝙜𝙚: Now you can hack whatsapp too 😂😂 \
\n\n.solar\
\n𝙐𝙨𝙖𝙜𝙚: Our beautiful solar system 🌞🌞\
\n\n.quickheal or .sqh or .vquickheal\
\n𝙐𝙨𝙖𝙜𝙚: Virus found ...Remove it using this 😂😂.\
\n\n.plane\
\n𝙐𝙨𝙖𝙜𝙚: For travelling from one place to another ✈️✈️\
\n\n.jio\
\n𝙐𝙨𝙖𝙜𝙚: Your network slow?? Boost it using this 🤣🤣\
\n\n\nWARNING⚠️⚠️: All this cmds will spam group recents.\nUse it in OT groups/Spam groups OR GET YOU A** KICKED😂😂."
})		

#update.py
CMD_HELP.update({
    'update':
    ".update\
\n𝙐𝙨𝙖𝙜𝙚: Checks if the main userbot repository has any updates and shows a changelog if so.\
\n\n.update now\
\n𝙐𝙨𝙖𝙜𝙚: Updates your userbot, if there are any updates in the main userbot repository."
})

#upload_download.py
CMD_HELP.update({
    "download":
    "`.download` <link|filename> or reply to media\
\n𝙐𝙨𝙖𝙜𝙚: Downloads file to the server.\
\n\n`.upload` <File path in server>\
\n𝙐𝙨𝙖𝙜𝙚: Uploads a locally stored file to the chat.\
\n\n`.uploadas(stream|vn|all)` <path in server>\
\n𝙐𝙨𝙖𝙜𝙚: Allows you to specify some arguments for upload.\
 \n\n`.uploadir` <Folder path in server>\
\n𝙐𝙨𝙖𝙜𝙚: Allows you to upload everything from a folder in the server."
})

#w3m.py
CMD_HELP.update(
    {"w3m": ".w3m google.com\n𝙐𝙨𝙖𝙜𝙚: Browse the internet with w3m on your server.\nPut your device into landscape mode for better preview."})

#weather.py 
CMD_HELP.update({
    "weather":
    ".weather <city> or .weather <city>, <country name/code>\
    \n𝙐𝙨𝙖𝙜𝙚: Gets the weather of a city."
})

#web_upload.py
CMD_HELP.update({
        "webupload": 
        "\n.webupload --(anonfiles|transfer|filebin|anonymousfiles|megaupload|bayfiles)\
         \n𝙐𝙨𝙖𝙜𝙚: reply .webupload --anonfiles or .webupload --filebin and the file will be uploaded to that website. "
    })

#weebify.py
CMD_HELP.update({
    "textx":
    "𝙐𝙨𝙖𝙜𝙚: .font <text>\
      \n`.weeb` Weebify a text\
    \n\n`.cursive` make text cursive.\
    \n\n`.cursivebold` make text cursive bold.\
    \n\n`.medieval` make text medival.\
    \n\n`.medievalbold` make text medival bold.\
    \n\n`.doublestruck` make text doublestruck.\
    \n\n`.bold` make text bold."
   
})

#welcome.py
CMD_HELP.update({
    "welcome":
    "\
.setwelcome <welcome message> or reply to a message with .setwelcome\
\n𝙐𝙨𝙖𝙜𝙚: Saves the message as a welcome note in the chat.\
\n\nAvailable variables for formatting welcome messages :\
\n`{mention}, {title}, {count}, {first}, {last}, {fullname}, {userid}, {username}, {my_first}, {my_fullname}, {my_last}, {my_mention}, {my_username}`\
\n\n.checkwelcome\
\n𝙐𝙨𝙖𝙜𝙚: Check whether you have a welcome note in the chat.\
\n\n.rmwelcome\
\n𝙐𝙨𝙖𝙜𝙚: Deletes the welcome note for the current chat.\
"
})

#whois.py
CMD_HELP.update({
    "whois":
    ".whois <username> or reply to someones text with .whois\
    \n𝙐𝙨𝙖𝙜𝙚: Gets info of an user."
})

#zipfile.py
CMD_HELP.update({
        "zipfile":
        "`.compress` [optional: <reply to file >]\
            \n𝙐𝙨𝙖𝙜𝙚: make files to zip."
        "\n`.addzip` <reply to file >\
            \n𝙐𝙨𝙖𝙜𝙚: add files to zip list."
        "\n`.upzip` [optional: <zip title>]\
            \n𝙐𝙨𝙖𝙜𝙚: upload zip list."
})

#www.py
CMD_HELP.update(
    {"speed": ".speed\
    \n𝙐𝙨𝙖𝙜𝙚: Does a speedtest and shows the results."})
CMD_HELP.update(
    {"dc": ".dc\
    \n𝙐𝙨𝙖𝙜𝙚: Finds the nearest datacenter from your server."})
CMD_HELP.update(
    {"ping": ".ping\
    \n𝙐𝙨𝙖𝙜𝙚: Shows how long it takes to ping your bot."})

#wtf_is_this_shit.py
CMD_HELP.update({
    "retarded":
    ".color\
    \n𝙐𝙨𝙖𝙜𝙚: color #<hex color code>\
    \n\n.chu\
    \n𝙐𝙨𝙖𝙜𝙚: this is a stupid module."
   
})


#hash.py
CMD_HELP.update({"base64": "Find the base64 encoding of the given string"})

CMD_HELP.update({
    "hash":
    "Find the md5, sha1, sha256, sha512 of the string when written into a txt file."
})

#stats.py
CMD_HELP.update(
    {"stats": ".stats\
    \n𝙐𝙨𝙖𝙜𝙚: Count the Number of Dialogs you have in your Telegram Account."})



















