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
you telling them that you are AFK(reason).\n\nSwitches off AFK when you type back anything, anywhere.\
"
})
  
#

