# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# The entire source code is OSSRPL except
# 'download, uploadir, uploadas, upload' which is MPL
# License: MPL and OSSRPL
""" Userbot module which contains everything related to \
    downloading/uploading from/to the server. """

import logging
import mimetypes
from datetime import datetime
from time import sleep
import json
import os
import subprocess
import time
import math
import re
from io import BytesIO
from pySmartDL import SmartDL
import asyncio
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
import psutil
from pyDownload import Downloader
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from telethon.tl.types import DocumentAttributeVideo, MessageMediaPhoto
from userbot import GDRIVE_FOLDER_ID as GDRIVE_FOLDER
from userbot import LOGS, CMD_HELP, TEMP_DOWNLOAD_DIRECTORY
from userbot.events import register

TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./")



async def progress(current, total, event, start, type_of_ps, file_name=None):
    """Generic progress_callback for uploads and downloads."""
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "[{0}{1}] {2}%\n".format(
            ''.join(["▰" for i in range(math.floor(percentage / 10))]),
            ''.join(["▱" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2))
        tmp = progress_str + \
            "{0} of {1}\nETA: {2}".format(
                humanbytes(current),
                humanbytes(total),
                time_formatter(estimated_total_time)
            )
        if file_name:
            await event.edit("{}\nFile Name: `{}`\n{}".format(
                type_of_ps, file_name, tmp))
        else:
            await event.edit("{}\n{}".format(type_of_ps, tmp))


def humanbytes(size):
    """Input size in bytes,
    outputs in a human readable format"""
    # https://stackoverflow.com/a/49361727/4723940
    if not size:
        return ""
    # 2 ** 10 = 1024
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


def time_formatter(milliseconds: int) -> str:
    """Inputs time in milliseconds, to get beautified time,
    as string"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + " day(s), ") if days else "") + \
        ((str(hours) + " hour(s), ") if hours else "") + \
        ((str(minutes) + " minute(s), ") if minutes else "") + \
        ((str(seconds) + " second(s), ") if seconds else "") + \
        ((str(milliseconds) + " millisecond(s), ") if milliseconds else "")
    return tmp[:-2]

async def download_from_url(url: str, file_name: str) -> str:
    """
    Download files from URL
    """
    start = datetime.now()
    downloader = Downloader(url=url)
    if downloader.is_running:
        sleep(1)
    end = datetime.now()
    duration = (end - start).seconds
    os.rename(downloader.file_name, file_name)
    status = f"Downloaded `{file_name}` in {duration} seconds."
    return status


async def download_from_tg(target_file) -> (str, BytesIO):
    """
    Download files from Telegram
    """
    async def dl_file(buffer: BytesIO) -> BytesIO:
        buffer = await target_file.client.download_media(
            reply_msg,
            buffer,
            progress_callback=progress,
        )
        return buffer

    start = datetime.now()
    buf = BytesIO()
    reply_msg = await target_file.get_reply_message()
    avail_mem = psutil.virtual_memory().available + psutil.swap_memory().free
    try:
        if reply_msg.media.document.size >= avail_mem:  # unlikely to happen but baalaji crai
            filen = await target_file.client.download_media(
                reply_msg,
                progress_callback=progress,
            )
        else:
            buf = await dl_file(buf)
            filen = reply_msg.media.document.attributes[0].file_name
    except AttributeError:
        buf = await dl_file(buf)
        try:
            filen = reply_msg.media.document.attributes[0].file_name
        except AttributeError:
            if isinstance(reply_msg.media, MessageMediaPhoto):
                filen = 'photo-' + str(datetime.today())\
                    .split('.')[0].replace(' ', '-') + '.jpg'
            else:
                filen = reply_msg.media.document.mime_type\
                    .replace('/', '-' + str(datetime.today())
                             .split('.')[0].replace(' ', '-') + '.')
    end = datetime.now()
    duration = (end - start).seconds
    await target_file.edit(f"`Downloaded {filen} in {duration} seconds.`")
    return filen, buf


async def gdrive_upload(filename: str, filebuf: BytesIO = None) -> str:
    """
    Upload files to Google Drive using PyDrive2
    """
    # a workaround for disabling cache errors
    # https://github.com/googleapis/google-api-python-client/issues/299
    logging.getLogger('googleapiclient.discovery_cache').setLevel(
        logging.CRITICAL)

    # Authenticate Google Drive automatically
    # https://stackoverflow.com/a/24542604
    gauth = GoogleAuth()
    # Try to load saved client credentials
    gauth.LoadCredentialsFile("secret.json")
    if gauth.credentials is None:
        return "nosecret"
    if gauth.access_token_expired:
        gauth.Refresh()
    else:
        # Initialize the saved credentials
        gauth.Authorize()
    # Save the current credentials to a file
    gauth.SaveCredentialsFile("secret.json")
    drive = GoogleDrive(gauth)

    if filename.count('/') > 1:
        filename = filename.split('/')[-1]
    filedata = {
        'title': filename,
        "parents": [{
            "kind": "drive#fileLink",
            "id": GDRIVE_FOLDER
        }]
    }

    if filebuf:
        mime_type = mimetypes.guess_type(filename)
        if mime_type[0] and mime_type[1]:
            filedata['mimeType'] = f"{mime_type[0]}/{mime_type[1]}"
        else:
            filedata['mimeType'] = 'text/plain'
        file = drive.CreateFile(filedata)
        file.content = filebuf
    else:
        file = drive.CreateFile(filedata)
        file.SetContentFile(filename)
    name = filename.split('/')[-1]
    file.Upload()
    # insert new permission
    file.InsertPermission({
        'type': 'anyone',
        'value': 'anyone',
        'role': 'reader'
    })
    if not filebuf:
        os.remove(filename)
    reply = f"[{name}]({file['alternateLink']})\n" \
        f"__Direct link:__ [Here]({file['downloadUrl']})"
    return reply


@register(pattern=r"^.mirror(?: |$)([\s\S]*)", outgoing=True)
async def gdrive_mirror(request):
    """ Download a file and upload to Google Drive """
    message = request.pattern_match.group(1)
    if not request.reply_to_msg_id and not message:
        await request.edit("`Usage: .mirror <url> <url>`")
        return
    reply = ''
    reply_msg = await request.get_reply_message()
    links = re.findall(r'\bhttps?://.*\.\S+', message)
    if not (links or reply_msg or reply_msg.media or reply_msg.media.document):
        reply = "`No links or telegram files found!`\n"
        await request.edit(reply)
        return
    if request.reply_to_msg_id:
        await request.edit('`Downloading from Telegram...`')
        filen, buf = await download_from_tg(request)
        await request.edit(f'`Uploading {filen} to GDrive...`')
        reply += await gdrive_upload(
            filen, buf) if buf else await gdrive_upload(filen)
    elif "|" in message:
        url, file_name = message.split("|")
        url = url.strip()
        file_name = file_name.strip()
        await request.edit(f'`Downloading {file_name}`')
        status = await download_from_url(url, file_name)
        await request.edit(status)
        await request.edit(f'`Uploading {file_name} to GDrive...`')
        reply += await gdrive_upload(file_name)
    if "nosecret" in reply:
        reply = "`Run the generate_drive_session.py file " \
                "in your machine to authenticate on google drive!!`"
        await request.edit(reply)


@register(pattern=r"^.drive(?: |$)(\S*.?\/*.?\.?[A-Za-z0-9]*)", outgoing=True)
async def gdrive(request):
    """ Upload files from server to Google Drive """
    path = request.pattern_match.group(1)
    if not path:
        await request.edit("`Usage: .drive <file>`")
        return
    if not os.path.isfile(path):
        await request.edit("`No such file!`\n")
        return
    file_name = path.split('/')[-1]
    await request.edit(f'`Uploading {file_name} to GDrive...`')
    reply = await gdrive_upload(path)
    await request.edit(reply)



@register(pattern=r".download(?: |$)(.*)", outgoing=True)
async def download(target_file):
    """ For .download command, download files to the userbot's server. """
    await target_file.edit("Processing ...")
    input_str = target_file.pattern_match.group(1)
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    if "|" in input_str:
        url, file_name = input_str.split("|")
        url = url.strip()
        # https://stackoverflow.com/a/761825/4723940
        file_name = file_name.strip()
        head, tail = os.path.split(file_name)
        if head:
            if not os.path.isdir(os.path.join(TEMP_DOWNLOAD_DIRECTORY, head)):
                os.makedirs(os.path.join(TEMP_DOWNLOAD_DIRECTORY, head))
                file_name = os.path.join(head, tail)
        downloaded_file_name = TEMP_DOWNLOAD_DIRECTORY + "" + file_name
        downloader = SmartDL(url, downloaded_file_name, progress_bar=False)
        downloader.start(blocking=False)
        c_time = time.time()
        display_message = None
        while not downloader.isFinished():
            status = downloader.get_status().capitalize()
            total_length = downloader.filesize if downloader.filesize else None
            downloaded = downloader.get_dl_size()
            now = time.time()
            diff = now - c_time
            percentage = downloader.get_progress() * 100
            speed = downloader.get_speed()
            elapsed_time = round(diff) * 1000
            progress_str = "[{0}{1}] {2}%".format(
                ''.join(["▰" for i in range(math.floor(percentage / 10))]),
                ''.join(["▱"
                         for i in range(10 - math.floor(percentage / 10))]),
                round(percentage, 2))
            estimated_total_time = downloader.get_eta(human=True)
            try:
                current_message = f"{status}..\
                \nURL: {url}\
                \nFile Name: {file_name}\
                \n{progress_str}\
                \n{humanbytes(downloaded)} of {humanbytes(total_length)}\
                \nETA: {estimated_total_time}"

                if round(diff %
                         10.00) == 0 and current_message != display_message:
                    await target_file.edit(current_message)
                    display_message = current_message
            except Exception as e:
                LOGS.info(str(e))
        if downloader.isSuccessful():
            await target_file.edit("Downloaded to `{}` successfully !!".format(
                downloaded_file_name))
        else:
            await target_file.edit("Incorrect URL\n{}".format(url))
    elif target_file.reply_to_msg_id:
        try:
            c_time = time.time()
            downloaded_file_name = await target_file.client.download_media(
                await target_file.get_reply_message(),
                TEMP_DOWNLOAD_DIRECTORY,
                progress_callback=lambda d, t: asyncio.get_event_loop(
                ).create_task(
                    progress(d, t, target_file, c_time, "Downloading...")))
        except Exception as e:  # pylint:disable=C0103,W0703
            await target_file.edit(str(e))
        else:
            await target_file.edit("Downloaded to `{}` successfully !!".format(
                downloaded_file_name))
    else:
        await target_file.edit(
            "Reply to a message to download to my local server.")


@register(pattern=r".uploadir (.*)", outgoing=True)
async def uploadir(udir_event):
    """ For .uploadir command, allows you to upload everything from a folder in the server"""
    input_str = udir_event.pattern_match.group(1)
    if os.path.exists(input_str):
        await udir_event.edit("Processing ...")
        lst_of_files = []
        for r, d, f in os.walk(input_str):
            for file in f:
                lst_of_files.append(os.path.join(r, file))
            for file in d:
                lst_of_files.append(os.path.join(r, file))
        LOGS.info(lst_of_files)
        uploaded = 0
        await udir_event.edit(
            "Found {} files. Uploading will start soon. Please wait!".format(
                len(lst_of_files)))
        for single_file in lst_of_files:
            if os.path.exists(single_file):
                # https://stackoverflow.com/a/678242/4723940
                caption_rts = os.path.basename(single_file)
                c_time = time.time()
                if not caption_rts.lower().endswith(".mp4"):
                    await udir_event.client.send_file(
                        udir_event.chat_id,
                        single_file,
                        caption=caption_rts,
                        force_document=False,
                        allow_cache=False,
                        reply_to=udir_event.message.id,
                        progress_callback=lambda d, t: asyncio.get_event_loop(
                        ).create_task(
                            progress(d, t, udir_event, c_time, "Uploading...",
                                     single_file)))
                else:
                    thumb_image = os.path.join(input_str, "thumb.jpg")
                    c_time = time.time()
                    metadata = extractMetadata(createParser(single_file))
                    duration = 0
                    width = 0
                    height = 0
                    if metadata.has("duration"):
                        duration = metadata.get("duration").seconds
                    if metadata.has("width"):
                        width = metadata.get("width")
                    if metadata.has("height"):
                        height = metadata.get("height")
                    await udir_event.client.send_file(
                        udir_event.chat_id,
                        single_file,
                        caption=caption_rts,
                        thumb=thumb_image,
                        force_document=False,
                        allow_cache=False,
                        reply_to=udir_event.message.id,
                        attributes=[
                            DocumentAttributeVideo(
                                duration=duration,
                                w=width,
                                h=height,
                                round_message=False,
                                supports_streaming=True,
                            )
                        ],
                        progress_callback=lambda d, t: asyncio.get_event_loop(
                        ).create_task(
                            progress(d, t, udir_event, c_time, "Uploading...",
                                     single_file)))
                os.remove(single_file)
                uploaded = uploaded + 1
        await udir_event.edit(
            "Uploaded {} files successfully !!".format(uploaded))
    else:
        await udir_event.edit("404: Directory Not Found")


@register(pattern=r".upload (.*)", outgoing=True)
async def upload(u_event):
    """ For .upload command, allows you to upload a file from the userbot's server """
    await u_event.edit("Processing ...")
    input_str = u_event.pattern_match.group(1)
    if input_str in ("userbot.session", "config.env"):
        await u_event.edit("`That's a dangerous operation! Not Permitted!`")
        return
    if os.path.exists(input_str):
        c_time = time.time()
        await u_event.client.send_file(
            u_event.chat_id,
            input_str,
            force_document=True,
            allow_cache=False,
            reply_to=u_event.message.id,
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, u_event, c_time, "Uploading...", input_str)))
        await u_event.edit("Uploaded successfully !!")
    else:
        await u_event.edit("404: File Not Found")


def get_video_thumb(file, output=None, width=90):
    """ Get video thumbnail """
    metadata = extractMetadata(createParser(file))
    popen = subprocess.Popen(
        [
            "ffmpeg",
            "-i",
            file,
            "-ss",
            str(
                int((0, metadata.get("duration").seconds
                     )[metadata.has("duration")] / 2)),
            "-filter:v",
            "scale={}:-1".format(width),
            "-vframes",
            "1",
            output,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    if not popen.returncode and os.path.lexists(file):
        return output
    return None


def extract_w_h(file):
    """ Get width and height of media """
    command_to_run = [
        "ffprobe",
        "-v",
        "quiet",
        "-print_format",
        "json",
        "-show_format",
        "-show_streams",
        file,
    ]
    # https://stackoverflow.com/a/11236144/4723940
    try:
        t_response = subprocess.check_output(command_to_run,
                                             stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as exc:
        LOGS.warning(exc)
    else:
        x_reponse = t_response.decode("UTF-8")
        response_json = json.loads(x_reponse)
        width = int(response_json["streams"][0]["width"])
        height = int(response_json["streams"][0]["height"])
        return width, height


@register(pattern=r".uploadas(stream|vn|all) (.*)", outgoing=True)
async def uploadas(uas_event):
    """ For .uploadas command, allows you to specify some arguments for upload. """
    await uas_event.edit("Processing ...")
    type_of_upload = uas_event.pattern_match.group(1)
    supports_streaming = False
    round_message = False
    spam_big_messages = False
    if type_of_upload == "stream":
        supports_streaming = True
    if type_of_upload == "vn":
        round_message = True
    if type_of_upload == "all":
        spam_big_messages = True
    input_str = uas_event.pattern_match.group(2)
    thumb = None
    file_name = None
    if "|" in input_str:
        file_name, thumb = input_str.split("|")
        file_name = file_name.strip()
        thumb = thumb.strip()
    else:
        file_name = input_str
        thumb_path = "a_random_f_file_name" + ".jpg"
        thumb = get_video_thumb(file_name, output=thumb_path)
    if os.path.exists(file_name):
        metadata = extractMetadata(createParser(file_name))
        duration = 0
        width = 0
        height = 0
        if metadata.has("duration"):
            duration = metadata.get("duration").seconds
        if metadata.has("width"):
            width = metadata.get("width")
        if metadata.has("height"):
            height = metadata.get("height")
        try:
            if supports_streaming:
                c_time = time.time()
                await uas_event.client.send_file(
                    uas_event.chat_id,
                    file_name,
                    thumb=thumb,
                    caption=input_str,
                    force_document=False,
                    allow_cache=False,
                    reply_to=uas_event.message.id,
                    attributes=[
                        DocumentAttributeVideo(
                            duration=duration,
                            w=width,
                            h=height,
                            round_message=False,
                            supports_streaming=True,
                        )
                    ],
                    progress_callback=lambda d, t: asyncio.get_event_loop(
                    ).create_task(
                        progress(d, t, uas_event, c_time, "Uploading...",
                                 file_name)))
            elif round_message:
                c_time = time.time()
                await uas_event.client.send_file(
                    uas_event.chat_id,
                    file_name,
                    thumb=thumb,
                    allow_cache=False,
                    reply_to=uas_event.message.id,
                    video_note=True,
                    attributes=[
                        DocumentAttributeVideo(
                            duration=0,
                            w=1,
                            h=1,
                            round_message=True,
                            supports_streaming=True,
                        )
                    ],
                    progress_callback=lambda d, t: asyncio.get_event_loop(
                    ).create_task(
                        progress(d, t, uas_event, c_time, "Uploading...",
                                 file_name)))
            elif spam_big_messages:
                await uas_event.edit("TBD: Not (yet) Implemented")
                return
            os.remove(thumb)
            await uas_event.edit("Uploaded successfully !!")
        except FileNotFoundError as err:
            await uas_event.edit(str(err))
    else:
        await uas_event.edit("404: File Not Found")


CMD_HELP.update({
    "download":
    ".download <link|filename> or reply to media\
\nUsage: Downloads file to the server.\
\n\n.upload <path in server>\
\nUsage: Uploads a locally stored file to the chat."
})
CMD_HELP.update({
    "drive":
    ".upload <file>\nUsage: Upload a locally stored file to GDrive."
})
CMD_HELP.update({
    "mirror":
    ".mirror [in reply to TG file]\n"
    "or .mirror <link> | <filename>\n"
    "Usage: Download a file from telegram "
    "or link to the server then upload to your GDrive."
})
