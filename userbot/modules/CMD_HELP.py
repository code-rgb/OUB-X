from userbot import CMD_HELP

#admin.py
CMD_HELP.update({
    "admin":
    ".promote <username/reply> <custom rank (optional)>\
\nUsage: Provides admin rights to the person in the chat.\
\n\n.demote <username/reply>\
\nUsage: Revokes the person's admin permissions in the chat.\
\n\n.ban <username/reply> <reason (optional)>\
\nUsage: Bans the person off your chat.\
\n\n.unban <username/reply>\
\nUsage: Removes the ban from the person in the chat.\
\n\n.mute <username/reply> <reason (optional)>\
\nUsage: Mutes the person in the chat, works on admins too.\
\n\n.unmute <username/reply>\
\nUsage: Removes the person from the muted list.\
\n\n.gmute <username/reply> <reason (optional)>\
\nUsage: Mutes the person in all groups you have in common with them.\
\n\n.ungmute <username/reply>\
\nUsage: Reply someone's message with .ungmute to remove them from the gmuted list.\
\n\n.zombies\
\nUsage: Searches for deleted accounts in a group. Use .zombies clean to remove deleted accounts from the group.\
\n\n.admins\
\nUsage: Retrieves a list of admins in the chat.\
\n\n.bots\
\nUsage: Retrieves a list of bots in the chat.\
\n\n.pin <reply/tag>\
\nUsage: pins the replied/tagged message on the top the chat silently.\
\n\n.cpin <reply/tag>\
\nUsage: pins the replied/tagged message on the top the chat LOUDLY.\
\n\n.users or .users <name of member>\
\nUsage: Retrieves all (or queried) users in the chat.\
\n\n.setgppic <reply to image>\
\nUsage: Changes the group's display picture."
})  
  
#afk
CMD_HELP.update({
    "afk":
    "`.afk` [Optional Reason]\
\nUsage: Sets you as afk.\nReplies to anyone who tags/PM's \
you telling them that you are AFK(reason).\n\nSwitches off AFK when you type back anything, anywhere."
})
  
#memes.py
CMD_HELP.update({
    "memes":
    ".cowsay\
\nUsage: cow which says things.\
\n\n:/\
\nUsage: Check yourself ;)\
\n\n-_-\
\nUsage: Ok...\
\n\n;_;\
\nUsage: Like `-_-` but crying.\
\n\n.lol\
\n\n.pickup\
\n\n.earth\
\nusage:type .earth\
\nusage: Reply .lol for funny lol text\
\n\n.cp\
\nUsage: Copypasta the famous meme\
\n\n.vapor\
\nUsage: Vaporize everything!\
\n\n.str\
\nUsage: Stretch it.\
\n\n.10iq\
\nUsage: You retard !!\
\n\n.zal\
\nUsage: Invoke the feeling of chaos.\
\n\nOem\
\nUsage: Oeeeem\
\n\nOof\
\nUsage: Ooooof\
\n\n.fp\
\nUsage: Facepalm :P\
\n\n.moon\
\nUsage: kensar moon animation.\
\n\n.clock\
\nUsage: kensar clock animation.\
\n\n.hi\
\nUsage: Greet everyone!\
\n\n.coinflip <heads/tails>\
\nUsage: Flip a coin !!\
\n\n.owo\
\nUsage: UwU\
\n\n.pro or .nub or .bye\
\nUsage: see it yourself\
\n\n.react\
\nUsage: Make your userbot react to everything.\
\n\n.slap\
\nUsage: reply to slap them with random objects !!\
\n\n.cry\
\nUsage: y u du dis, i cri.\
\n\n.shg\
\nUsage: Shrug at it !!\
\n\n.run\
\nUsage: Let Me Run, run, RUNNN!\
\n\n.chase\
\nUsage: You better start running\
\n\n.metoo\
\nUsage: Haha yes\
\n\n.dorime\
\nUsage: pray\
\n\n.mock\
\nUsage: Do it and find the real fun.\
\n\n.clap\
\nUsage: Praise people!\
\n\n.f <emoji/character>\
\nUsage: Pay Respects.\
\n\n.men\
\nUsage: reply .men text and mention ur friends with custom text.\
\n\n.bt\
\nUsage: Believe me, you will find this useful.\
\n\n.type\
\nUsage: Just a small command to make your keyboard become a typewriter!\
\n\n.lfy <query>\
\nUsage: Let me Google that for you real quick !!\
\n\n.decide [Alternates: (.yes, .no, .maybe)]\
\nUsage: Make a quick decision.\
\n\n.scam <action> <time>\
\n[Available Actions: (typing, contact, game, location, voice, round, video, photo, document, cancel)]\
\nUsage: Create fake chat actions, for fun. (Default action: typing)\
\n\nAnd many more\
\n.nou ; .bot ; .gey ; .gey ; .tf ; .paw ; .taco ; .nih ;\
\n.fag ; .gtfo ; .stfu ; .lol ; .lols ; .lool ; .fail ; .love\
\n.rain ; .earth ; .iwi ; .sayhi\
\n\n\nThanks to BottomBextBot (@NotAMemeBot) for some of these."
})

#android.py
CMD_HELP.update({
    "android":
    ".magisk"
    "\nGet latest Magisk releases"
    "\n\n.pixeldl **<download.pixelexperience.org>**"
    "\nUsage: Download pixel experience ROM into your userbot server."
    "\n\n.twrp <codename>"
    "\nUsage: Get latest twrp download for android device."
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
\nUsage: A Plugin to tagall in the chat."
})  


#anime_chooser.py
CMD_HELP.update({
        "anime":  \
        "Anime random generator \
        \nUsage: .(genre) number of times(interger)\
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
    \nUsage: Type .scan to remove virus"
})

#aria.py
CMD_HELP.update({
    "aria":
    "`.aurl` [URL] (or) .amag [Magnet Link] (or) .ator [path to torrent file]\
    \nUsage: Downloads the file into your userbot server storage.\
    \n\n`.apause` (or) .aresume\
    \nUsage: Pauses/resumes on-going downloads.\
    \n\n`.aclear`\
    \nUsage: Clears the download queue, deleting all on-going downloads.\
    \n\n`.ashow`\
    \nUsage: Shows progress of the on-going downloads."
})

#ariav2.py
CMD_HELP.update({
    "aria2":
    ".url [url]\
    \nUsage: Downloads the file into your userbot server storage.\
    \nUsing ariav2."
})

#blacklist.py
CMD_HELP.update({
    "blacklist":
    ".listbl\
    \nUsage: Lists all active userbot blacklist in a chat.\
    \n\n.addbl <keyword>\
    \nUsage: Saves the message to the 'blacklist keyword'.\
    \nThe bot will delete to the message whenever 'blacklist keyword' is mentioned.\
    \n\n.rmbl <keyword>\
    \nUsage: Stops the specified blacklist."
})

#carbon.py
CMD_HELP.update({
    "carbon":
    "`.carbon` value <values=1,2,3,4,5>\
        \nUsage:reply or type .carbon value and beautify your text."
})

#changelog.py
CMD_HELP.update({
    'update':
    ".chl\
\nUsage: Checks if the main userbot repository has any updates and shows a changelog if so.\
\n\n.update\
\nUsage: Updates your userbot, if there are any updates in the main userbot repository."
})

#chat.py
CMD_HELP.update({
    "chat":
    ".chatid\
\nUsage: Fetches the current chat's ID\
\n\n.userid\
\nUsage: Fetches the ID of the user in reply, if its a forwarded message, finds the ID for the source.\
\n\n.log\
\nUsage: Forwards the message you've replied to in your bot logs group.\
\n\n.kickme\
\nUsage: Leave from a targeted group.\
\n\n.unmutechat\
\nUsage: Unmutes a muted chat.\
\n\n.mutechat\
\nUsage: Allows you to mute any chat.\
\n\n.link <username/userid> : <optional text> (or) reply to someone's message with .link <optional text>\
\nUsage: Generate a permanent link to the user's profile with optional custom text.\
\n\n.regexninja on/off\
\nUsage: Globally enable/disables the regex ninja module.\
\nRegex Ninja module helps to delete the regex bot's triggering messages."
})

#chatinfo.py
CMD_HELP.update({
        "chatinfo":
        ".chatinfo [optional: <reply/tag/chat id/invite link>]\
            \nUsage: Gets info of a chat. Some info might be limited due to missing permissions.\
            \n\n.invite\
            \nUsage:Invites users to a chat, not to a private message."
})

#covidv2.py
CMD_HELP.update(
    {"corona": ".corona [country]\n"
     "Usage: Corona Virus stats."})

#covid.py
CMD_HELP.update({
        "covid": 
        ".covid <country>"
        "\nUsage: Get an information about data covid-19 in your country.\n"
    })

#create.py
CMD_HELP.update({
    "create": "\
Create\
\nUsage: Create Channel, Group & Group With Bot.\
\n\n.create g <group name>\
\nUsage: Create a Private Group.\
\n\n.create b <group name>\
\nUsage: Create a Group with Bot.\
\n\n.create c <channel name>\
\nUsage: Create a Channel.\
"})

#dbs.py
CMD_HELP.update(
    {"dbs": ".dbs\n"
     "Usage: Shows database related info."})

#deepfry.py
CMD_HELP.update({
"deepfry": ".deepfry\
    \nUsage: Reply .deepfry 1-5 to an image or sticker to deep fry it!. "
})   

#dfry.py
CMD_HELP.update({
    "dfry":
    ".dfry or .dfry [level(1-8)]"
    "\nUsage: deepfry image/sticker from the reply."
    "\n@image_deepfrybot"
})

#dice_dart_basketball.py

CMD_HELP.update({
    "dice":
    ".dice or .dice 1 to 6 any value\
\nUsage: hahaha just a magic.\
\nwarning: `you would be in trouble if you input any other value than mentioned.`"
})    

CMD_HELP.update({
    "basketball":
    ".basketball or .basketball 1 to 5 any value\
\nUsage: hahaha just a magic.\
\nwarning: `you would be in trouble if you input any other value than mentioned.`"
})    

CMD_HELP.update({
    "dart":
    ".dart or .dart 1 to 6 any value\
\nUsage: hahaha just a magic.\
\nwarning: `you would be in trouble if you input any other value than mentioned.`"
})   

#dictionary.py
CMD_HELP.update({
        "dictionary": 
        ".meaning <word>"
        "\nUsage: Atleast it works :p\n"
    })

#direct_link.py
CMD_HELP.update({
    "direct":
    ".direct <url>\n"
    "Usage: Reply to a link or paste a URL to\n"
    "generate a direct download link\n\n"
    "List of supported URLs:\n"
    "`Google Drive - Cloud Mail - Yandex.Disk - AFH - "
    "ZippyShare - MediaFire - SourceForge - OSDN - GitHub`"
})

#dogbin.py
CMD_HELP.update({
    "dogbin":
    ".paste <text/reply>\
\nUsage: Create a paste or a shortened url using dogbin (https://del.dog/)\
\n\n.getpaste\
\nUsage: Gets the content of a paste or shortened url from dogbin (https://del.dog/)"
})

#evaluator.py
CMD_HELP.update({"eval": ".eval 2 + 3\nUsage: Evalute mini-expressions."})
CMD_HELP.update(
    {"exec": ".exec print('hello')\nUsage: Execute small python scripts."})
CMD_HELP.update(
    {"term": ".term ls\nUsage: Run bash commands and scripts on your server."})

#fgban.py
CMD_HELP.update(
    {"fgban": ".fgban\
    \nUsage: Type .fgban or Reply .fgban reason and see it yourself."})

#figlet.py
CMD_HELP.update({
        "figlet": 
        ".figlet \
          \nUsage: Enhance ur text to strip line with anvil.\n"
    })

#fileext.py
CMD_HELP.update({
        "fileext": 
        ".fileext <ext>\
          \nUsage: get information about file extentions.\n"
    })

#filter.py
CMD_HELP.update({
    "filter":
    ".filters\
    \nUsage: Lists all active userbot filters in a chat.\
    \n\n.filter <keyword> <reply text> or reply to a message with .filter <keyword>\
    \nUsage: Saves the replied message as a reply to the 'keyword'.\
    \nThe bot will reply to the message whenever 'keyword' is mentioned.\
    \nWorks with everything from files to stickers.\
    \n\n.stop <filter>\
    \nUsage: Stops the specified filter.\
    \n\n.rmbotfilters <marie/rose>\
    \nUsage: Removes all filters of admin bots (Currently supported: Marie, Rose and their clones.) in the chat."
})

#gban.py
CMD_HELP.update({
    "gban": "\
`.gban reason`\
\nUsage: Globally Ban users from all the Group Administrations bots where you are SUDO.\
\n\n`.ungban reason`\
\nUsage: Globally unBan users from all the Group Administrations bots where you are SUDO"
})

#gdrive.py
CMD_HELP.update({
    "gdrive":
    "`.gdauth`"
    "\nUsage: generate token to enable all cmd google drive service."
    "\nThis only need to run once in life time."
    "\n\n`.gdreset`"
    "\nUsage: reset your token if something bad happened or change drive acc."
    "\n\n`.gd`"
    "\nUsage: Upload file from local or uri/url/drivelink into google drive."
    "\nfor drivelink it's upload only if you want to."
    "\n\n`.gdabort`"
    "\nUsage: Abort process uploading or downloading."
    "\n\n`.gdlist`"
    "\nUsage: Get list of folders and files with default size 50."
    "\nUse flags `-l range[1-1000]` for limit output."
    "\nUse flags `-p parents-folder_id` for lists given folder in gdrive."
    "\n\n`.gdf mkdir`"
    "\nUsage: Create gdrive folder."
    "\n\n`.gdf check`"
    "\nUsage: Check file/folder in gdrive."
    "\n\n`.gdf rm`<file/folder>name"
    "\nUsage: Delete files/folders in gdrive."
    "\nCan't be undone, this method skipping file trash, so be caution..."
    "\n\n`.gdfset put`"
    "\nUsage: Change upload directory in gdrive."
    "\n\n`.gdfset rm`"
    "\nUsage: remove set parentId from cmd\n`.gdfset put` "
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
        "\nUsage: Finding and uploading song.\n"
        "`.smd` <song tittle> "
        "\nUsage: Download music from spotify"
})

#github.py
CMD_HELP.update({"git": "Like .whois but for GitHub usernames."})

#gitupload.py
CMD_HELP.update({
    "gcommit": 
    ".gcommit\
    \n\nUsage: GITHUB File Uploader Plugin for userbot. Heroku Automation should be Enabled. Else u r not that lazy , For lazy people\
\n\nInstructions:- Set GITHUB_ACCESS_TOKEN and GIT_REPO_NAME Variables in Heroku vars First\
\n\n.gcommit reply_to_any_plugin can be any type of file too. but for plugin must be in .py ."})


#hazmat.py
CMD_HELP.update({
    "hazmat":
    "`.hz` or `.hz [flip, x2, rotate (degree), background (number), black]`"
    "\nUsage: Reply to a image / sticker to suit up!"
})

#help_on_update.py
CMD_HELP.update({
    "useitoub":
    ".useitoub\
\nUsage: Provide links to update repo guides while you keep your changes on the floor.\
\n.varoub\
\nUsage: Provide vars to cross check for you."
})

#heroku.py
CMD_HELP.update({
    "heroku":
    ">.`usage`"
    "\nUsage: Check your heroku dyno hours remaining"
    "\n\n>`.set var <NEW VAR> <VALUE>`"
    "\nUsage: add new variable or update existing value variable"
    "\n!!! WARNING !!!, after setting a variable the bot will restarted"
    "\n\n>`.get var or .get var <VAR>`"
    "\nUsage: get your existing varibles, use it only on your private group!"
    "\nThis returns all of your private information, please be caution..."
    "\n\n>`.del var <VAR>`"
    "\nUsage: delete existing variable"
    "\n!!! WARNING !!!, after deleting variable the bot will restarted"
})

#invite.py
CMD_HELP.update({
    'invite':
    '.invite <username> \
        \nUsage: Invite some user or bots if u want.'
})

#listmyusernames.py
CMD_HELP.update({
   "listmyusernames":
  "\ndo this in your private group for security purpose.\
   \n-listmyusernames \
\nUsage: Provides all titles according to the usernames reserved by you.\
  -listmychatids \
\nUsage: Provides all Chat IDs reserved by you."
})

#locks.py
CMD_HELP.update({
    "locks":
    ".lock <all (or) type(s)> or .unlock <all (or) type(s)>\
\nUsage: Allows you to lock/unlock some common message types in the chat.\
[NOTE: Requires proper admin rights in the chat !!]\
\n\nAvailable message types to lock/unlock are: \
\n`all, msg, media, sticker, gif, game, inline, poll, invite, pin, info`"
})

#logpms.py
CMD_HELP.update({
    "logpms":
    "If you don't want chat logs than use `.nolog` , for opposite use `.log`. Default is .log enabled\
\nUsage: This will now log chat msgs to your PM_LOGGR_BOT_API_ID.\
\nnotice: now you can totally disable pm logs by adding heroku vars PM_LOGGR_BOT_API_ID by providing a valid group ID and NC_LOG_P_M_S True or False,\
\nwhere False means no pm logs at all..enjoy.. update and do add above mentioned vars."
})  

#lydia.py
CMD_HELP.update({
    "lydia":
    ".addcf <username/reply>\
\nUsage: add's lydia auto chat request in the chat.\
\n\n.remcf <username/reply>\
\nUsage: remove's lydia auto chat request in the chat.\
\n\n.repcf <username/reply>\
\nUsage: starts lydia repling to perticular person in the chat.\
\n Note:  get your value from https://coffeehouse.intellivoid.info/dashboard."
})

#mega_downloader.py
CMD_HELP.update({
    "mega":
    ".mega <mega url>\n"
    "Usage: Reply to a mega link or paste your mega link to\n"
    "download the file into your userbot server\n\n"
    "Only support for *FILE* only."
})

#memex.py waifu.py
CMD_HELP.update({
    "waifu":
    ".waifu [text]\
\nUsage: for custom anime girl stickers. \
\n\n.memex\
\nUsage: for custom meme stickers."})

#memeify.py
CMD_HELP.update({
    "memify": 
        "`.mmf` texttop ; textbottom\
        \nUsage: Reply a sticker/image/gif and send with cmd."
})

#misc.py
CMD_HELP.update({
    'random':
    '.random <item1> <item2> ... <itemN>\
\nUsage: Get a random item from the list of items.'
})

CMD_HELP.update({
    'sleep':
    '.sleep <seconds>\
\nUsage: Userbots get tired too. Let yours snooze for a few seconds.'
})

CMD_HELP.update({
    "shutdown":
    ".shutdown\
\nUsage: Sometimes you need to shut down your bot. Sometimes you just hope to\
hear Windows XP shutdown sound... but you don't."
})




CMD_HELP.update({
    'repo':
    '.repo\
\nUsage: If you are curious what makes the userbot work, this is what you need.'
})

CMD_HELP.update({
    'myrepo':
    '.myrepo\
\nUsage: If you are curious which is your personal repo, this is what you have.'
})

CMD_HELP.update({
    "readme":
    ".readme\
\nUsage: Provide links to setup the userbot and it's modules."
})

CMD_HELP.update(
    {"creator": ".creator\
\nUsage: Know who created this awesome userbot !!"})

CMD_HELP.update({
    "repeat":
    ".repeat <no.> <text>\
\nUsage: Repeats the text for a number of times. Don't confuse this with spam tho."
})

CMD_HELP.update({"restart": ".restart\
\nUsage: Restarts the bot !!"})

CMD_HELP.update({
    "raw":
    ".raw\
\nUsage: Get detailed JSON-like formatted data about replied message."
})

#nhentai.py
CMD_HELP.update({
"nhentai": 
".nhentai <link / code> \
\nUsage: view nhentai in telegra.ph XD\n"})

#notes.py
CMD_HELP.update({
    "notes":
    "\
#<notename>\
\nUsage: Gets the specified note.\
\n\n.save <notename> <notedata> or reply to a message with .save <notename>\
\nUsage: Saves the replied message as a note with the notename. (Works with pics, docs, and stickers too!)\
\n\n.notes\
\nUsage: Gets all saved notes in a chat.\
\n\n.clear <notename>\
\nUsage: Deletes the specified note.\
\n\n.rmbotnotes <marie/rose>\
\nUsage: Removes all notes of admin bots (Currently supported: Marie, Rose and their clones.) in the chat."
})

#ocr.py
CMD_HELP.update({
    'ocr':
    ".ocr <language>\nUsage: Reply to an image or sticker to extract text from it.\n\nGet language codes from [here](https://ocr.space/ocrapi)"
})

#pics.py
CMD_HELP.update({
    "pics": ".pic reply any document image\nUsage : Convert any Document Image to Full Size Image"
})

#pmmute.py
CMD_HELP.update({
    "nopm":
    "`.pmute`\
\nUsage: Reply .pmute and it will mute that person in pm  \
\n\n.`punmute`\
\nUsage:Reply .punmute and it will unmute that person in pm \
"
})

#pmpermit.py
CMD_HELP.update({
    "pmpermit":
    "\
.approve\
\nUsage: Approves the mentioned/replied person to PM.\
\n\n.disapprove\
\nUsage: Disapproves the mentioned/replied person to PM.\
\n\n.block\
\nUsage: Blocks the person.\
\n\n.unblock\
\nUsage: Unblocks the person so they can PM you.\
\n\n.notifoff\
\nUsage: Clears/Disables any notifications of unapproved PMs.\
\n\n.notifon\
\nUsage: Allows notifications for unapproved PMs."
})

#profile.py
CMD_HELP.update({
    "profile":
    ".username <new_username>\
\nUsage: Changes your Telegram username.\
\n\n.name <firstname> or .name <firstname> <lastname>\
\nUsage: Changes your Telegram name.(First and last name will get split by the first space)\
\n\n.setpfp\
\nUsage: Reply with .setpfp to an image to change your Telegram profie picture.\
\n\n.setbio <new_bio>\
\nUsage: Changes your Telegram bio.\
\n\n.delpfp or .delpfp <number>/<all>\
\nUsage: Deletes your Telegram profile picture(s).\
\n\n.reserved\
\nUsage: Shows usernames reserved by you.\
\n\n.count\
\nUsage: Counts your groups, chats, bots etc..."
})


#purge.py
CMD_HELP.update({
    'purge':
    '.purge\
        \nUsage: Purges all messages starting from the reply.'
})

CMD_HELP.update({
    'purgeme':
    '.purgeme <x>\
        \nUsage: Deletes x amount of your latest messages.'
})

CMD_HELP.update({"del": ".del\
\nUsage: Deletes the message you replied to."})

CMD_HELP.update({
    'edit':
    ".edit <newmessage>\
\nUsage: Replace your last message with <newmessage>."
})

CMD_HELP.update({
    'sd':
    '.sd <x> <message>\
\nUsage: Creates a message that selfdestructs in x seconds.\
\nKeep the seconds under 100 since it puts your bot to sleep.'
})


#qrcode.py
CMD_HELP.update({
    'qr':
    ".makeqr <content>\
\nUsage: Make a QR Code from the given content.\
\nExample: .makeqr www.google.com\
\nNote: use .decode <reply to barcode/qrcode> to get decoded content."
})

CMD_HELP.update({
    'barcode':
    ".barcode <content>\
\nUsage: Make a BarCode from the given content.\
\nExample: .barcode www.google.com\
\nNote: use .decode <reply to barcode/qrcode> to get decoded content."
})

#quotly.py
CMD_HELP.update({
        "quotly": 
        ".q reply_message. \
          \nUsage: Enhance ur text to sticker. \
          \nNote: please add API_TOKEN and API_URL in Heroku vars. \
          \n you can get those from http://antiddos.systems/. "
    })

#remove_bg.py
CMD_HELP.update({
    "rbg":
    ".rbg <Link to Image> or reply to any image (Warning: does not work on stickers.)\
\nUsage: Removes the background of images, using remove.bg API"
})   

#reverse.py
CMD_HELP.update({
    'reverse':
    '.reverse\
        \nUsage: Reply to a pic/sticker to revers-search it on Google Images !!'
})

#sangmata.py
CMD_HELP.update({
        "sangmata": 
        ".sg \
          \nUsage: View user history.\n"
    })

#scrapers.py
CMD_HELP.update({
    'img':
    '.img <search_query>\
        \nUsage: Does an image search on Google and shows 5 images.'
})
CMD_HELP.update({
    'currency':
    '.currency <amount> <from> <to>\
        \nUsage: Converts various currencies for you.'
})
CMD_HELP.update({
    'carbon':
    '.carbon <text> [or reply]\
        \nUsage: Beautify your code using carbon.now.sh\nUse .crblang <text> to set language for your code.'
})
CMD_HELP.update(
    {'google': '.google <query>\
        \nUsage: Does a search on Google.'})
CMD_HELP.update(
    {'wiki': '.wiki <query>\
        \nUsage: Does a search on Wikipedia.'})
CMD_HELP.update(
    {'ud': '.ud <query>\
        \nUsage: Does a search on Urban Dictionary.'})
CMD_HELP.update({
    'tts':
    '.tts <text> [or reply]\
        \nUsage: Translates text to speech for the language which is set.\nUse .lang tts <language code> to set language for tts. (Default is English.)'
})
CMD_HELP.update({
    'trt':
    '.trt <text> [or reply]\
        \nUsage: Translates text to the language which is set.\nUse .lang trt <language code> to set language for trt. (Default is English)'
})
CMD_HELP.update({'yt': '.yt <text>\
        \nUsage: Does a YouTube search.'})
CMD_HELP.update(
    {"imdb": ".imdb <movie-name>\nShows movie info and other stuff."})
CMD_HELP.update({
    'rip':
    '.ripaudio <url> or ripvideo <url>\
        \nUsage: Download videos and songs from YouTube (and [many other sites](https://ytdl-org.github.io/youtube-dl/supportedsites.html)).'
})

#screencapture.py
CMD_HELP.update({
    "ss":
    ".ss <url>\
    \nUsage: Takes a screenshot of a website and sends the screenshot.\
    \nExample of a valid URL : `https://www.google.com`"
})

#sed.py
CMD_HELP.update({
    "sed":
    ".s<delimiter><old word(s)><delimiter><new word(s)>\
    \nUsage: Replaces a word or words using sed.\
    \nDelimiters: `/, :, |, _`"
})

#singer.py
CMD_HELP.update({
"singer": ".singer\
    \nUsage: Type Usage: .singer Duman - Haberin Yok Ölüyorum"
})

#snips.py
CMD_HELP.update({
    "snips":
    "\
$<snip_name>\
\nUsage: Gets the specified snip, anywhere.\
\n\n.snip <name> <data> or reply to a message with .snip <name>\
\nUsage: Saves the message as a snip (global note) with the name. (Works with pics, docs, and stickers too!)\
\n\n.snips\
\nUsage: Gets all saved snips.\
\n\n.remsnip <snip_name>\
\nUsage: Deletes the specified snip.\
"
})

#spam.py
CMD_HELP.update({
    "spam":
    ".cspam <text>\
\nUsage: Spam the text letter by letter.\
\n\n.spam <count> <text>\
\nUsage: Floods text in the chat !!\
\n\n.wspam <text>\
\nUsage: Spam the text word by word.\
\n\n.picspam <count> <link to image/gif>\
\nUsage: As if text spam was not enough !!\
\n\n.delayspam <delay> <count> <text>\
\nUsage: .bigspam but with custom delay.\
\n\n\nNOTE : Spam at your own risk !!"
})

#stickers.py
CMD_HELP.update({
    "stickers":
    ".kang\
\nUsage: Reply .kang to a sticker or an image to kang it to your userbot pack.\
\n\n.kang [emoji('s)]\
\nUsage: Works just like .kang but uses the emoji('s) you picked.\
\n\n.kang [number]\
\nUsage: Kang's the sticker/image to the specified pack but uses 🤔 as emoji.\
\n\n.kang [emoji('s)] [number]\
\nUsage: Kang's the sticker/image to the specified pack and uses the emoji('s) you picked.\
\n\n.stkrinfo\
\nUsage: Gets info about the sticker pack.\
\n\n.getsticker\
\nUsage: reply to a sticker to get 'PNG' file of sticker."
})

#sticklet_un.py
CMD_HELP.update({
"sticklet_un": ".un\
    \nUsage: Type .un text and generate rgb sticker. "
}) 
# system_stat.py
CMD_HELP.update(
    {"sysd": ".sysd\
    \nUsage: Shows system information using neofetch."})
CMD_HELP.update({"botver": ".botver\
    \nUsage: Shows the userbot version."})
CMD_HELP.update(
    {"pip": ".pip <module(s)>\
    \nUsage: Does a search of pip modules(s)."})
CMD_HELP.update({
    "alive":
    ".alive\
    \nUsage: Type .alive to see wether your bot is working or not.\
    \n\n.aliveu <text>\
    \nUsage: Changes the 'user' in alive to the text you want.\
    \n\n.resetalive\
    \nUsage: Resets the user to default."
})

#telegraph.py
CMD_HELP.update({
    "telegraph": ".tg media as reply to a media \
        \n & .tg text as reply to a large text \
        \nUsage: Upload text & media on Telegraph.\
        \nNotice: you are required to set TELEGRAPH_SHORT_NAME in Heroku vars so that your bot remains alive \
        \nor else your bot will die."
})

#time.py
CMD_HELP.update({
    "time":
    ".time <country name/code> <timezone number>"
    "\nUsage: Get the time of a country. If a country has "
    "multiple timezones, it will list all of them "
    "and let you select one."
})
CMD_HELP.update({
    "date":
    ".date <country name/code> <timezone number>"
    "\nUsage: Get the date of a country. If a country has "
    "multiple timezones, it will list all of them "
    "and let you select one."
})

#toolx.py
CMD_HELP.update({
    "toolx":
    "`.app`\
\nUsage: type .app name and get app details.\
\n\n`.undlt`\
\nUsage: undo deleted message but u need admin permission.\
\n\n`.calc`\
\nUsage:.calc <term1><operator><term2>\nFor eg .calc 02*02 or 99*99 (the zeros are important) (two terms and two digits max).\
\n\n`.remove`\
\nUsage:.remove d or y or m or w or o or q or r.\n(d=deletedaccount y=userstatsempty m=userstatsmonth w=userstatsweek o=userstatsoffline q=userstatsonline r=userstatsrecently).\
\n\n`.xcd`\
\nUsage: type xcd <query>.ps:i have no damm idea how it works 🤷\
\n\n`.grab` <count>\
\nUsage:replay .grab or .grab <count> to grab profile picture.\
\n\n`.rnupload` filename.extenstion\
\nusage:reply to a sticker and type .rnupload xyz.jpg\
\n\n`.clone` @username\
\nusage: clone you whole freking account except username so stay safe\
\n\n`.res`\
\nusage: type account,channel,group or bot username and reply with .res and check restriction\
\n\n`.watch` <movie/tv> show\
\nusage:know details about particular movie/show."         
})

#uniborg_memes.py
CMD_HELP.update({
    "uniborg_memes":
    ".eye\
\nUsage: see it yourself.\
\n\n.earth\
\nusage: spins like earth 🌎🌎\
\n\n.bombs\
\nUsage: For bombing tg 🤣🤣\
\n\n.gift\
\nUsage: Well it's a gift i can't say what's inside 😁😁!\
\n\n.police\
\nUsage: Time to go to jail 😔😔.\
\n\n.kill\
\nUsage: For killing your enemies 🔫🔫 !!\
\n\n.os\
\nUsage: see it yourself 🤐🤐.\
\n\n.isro\
\nUsage: For calling aliens 👽👽 :P\
\n\n.gangstar\
\nUsage:U becum gengstar 🤠🤠.\
\n\n.hack\
\nUsage: For hacking telegram🖥️🖥️.\
\n\n.hypno\
\nUsage: Oh fek my eyes 👀\
\n\n.whatsapp\
\nUsage: Now you can hack whatsapp too 😂😂 \
\n\n.solar\
\nUsage: Our beautiful solar system 🌞🌞\
\n\n.quickheal or .sqh or .vquickheal\
\nUsage: Virus found ...Remove it using this 😂😂.\
\n\n.plane\
\nUsage: For travelling from one place to another ✈️✈️\
\n\n.jio\
\nUsage: Your network slow?? Boost it using this 🤣🤣\
\n\n\nWARNING⚠️⚠️: All this cmds will spam group recents.\nUse it in OT groups/Spam groups OR GET YOU A** KICKED😂😂."
})		

#update.py
CMD_HELP.update({
    'update':
    ".update\
\nUsage: Checks if the main userbot repository has any updates and shows a changelog if so.\
\n\n.update now\
\nUsage: Updates your userbot, if there are any updates in the main userbot repository."
})

#upload_download.py
CMD_HELP.update({
    "download":
    "`.download` <link|filename> or reply to media\
\nUsage: Downloads file to the server.\
\n\n`.upload` <path in server>\
\nUsage: Uploads a locally stored file to the chat."
})

#w3m.py
CMD_HELP.update(
    {"w3m": ".w3m google.com\nUsage: Browse the internet with w3m on your server.\nPut your device into landscape mode for better preview."})

#weather.py 
CMD_HELP.update({
    "weather":
    ".weather <city> or .weather <city>, <country name/code>\
    \nUsage: Gets the weather of a city."
})

#web_upload.py
CMD_HELP.update({
        "webupload": 
        "\n.webupload --(anonfiles|transfer|filebin|anonymousfiles|megaupload|bayfiles)\
         \nUsage: reply .webupload --anonfiles or .webupload --filebin and the file will be uploaded to that website. "
    })

#weebify.py
CMD_HELP.update({
    "textx":
    "Usage: .font <text>\
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
\nUsage: Saves the message as a welcome note in the chat.\
\n\nAvailable variables for formatting welcome messages :\
\n`{mention}, {title}, {count}, {first}, {last}, {fullname}, {userid}, {username}, {my_first}, {my_fullname}, {my_last}, {my_mention}, {my_username}`\
\n\n.checkwelcome\
\nUsage: Check whether you have a welcome note in the chat.\
\n\n.rmwelcome\
\nUsage: Deletes the welcome note for the current chat.\
"
})

#whois.py
CMD_HELP.update({
    "whois":
    ".whois <username> or reply to someones text with .whois\
    \nUsage: Gets info of an user."
})

#zipfile.py
CMD_HELP.update({
        "compress":
        ".compress [optional: <reply to file >]\
            \nUsage: make files to zip."
})

#www.py
CMD_HELP.update(
    {"speed": ".speed\
    \nUsage: Does a speedtest and shows the results."})
CMD_HELP.update(
    {"dc": ".dc\
    \nUsage: Finds the nearest datacenter from your server."})
CMD_HELP.update(
    {"ping": ".ping\
    \nUsage: Shows how long it takes to ping your bot."})

#wtf_is_this_shit.py
CMD_HELP.update({
    "retarded":
    ".color\
    \nUsage: color #<hex color code>\
    \n\n.chu\
    \nUsage: this is a stupid module."
   
})






















