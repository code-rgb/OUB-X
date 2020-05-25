# Copyright (C) 2020 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing commands related to android"""

import re
import json
from requests import get
from bs4 import BeautifulSoup
import asyncio
from userbot import CMD_HELP
from userbot.events import register

GITHUB = 'https://github.com'
DEVICES_DATA = 'https://raw.githubusercontent.com/androidtrackers/' \
               'certified-android-devices/master/devices.json'


@register(outgoing=True, pattern="^.magisk$")
async def magisk(request):
    """ magisk latest releases """
    magisk_dict = {
        "⦁ 𝗦𝘁𝗮𝗯𝗹𝗲":
        "https://raw.githubusercontent.com/topjohnwu/magisk_files/master/stable.json",
        "⦁ 𝗕𝗲𝘁𝗮":
        "https://raw.githubusercontent.com/topjohnwu/magisk_files/master/beta.json",
        "⦁ 𝗖𝗮𝗻𝗮𝗿𝘆 (𝗥𝗲𝗹𝗲𝗮𝘀𝗲)":
        "https://raw.githubusercontent.com/topjohnwu/magisk_files/canary/release.json",
        "⦁ 𝗖𝗮𝗻𝗮𝗿𝘆 (𝗗𝗲𝗯𝘂𝗴)":
        "https://raw.githubusercontent.com/topjohnwu/magisk_files/canary/debug.json"
    }
    releases = '𝗟𝗮𝘁𝗲𝘀𝘁 𝗠𝗮𝗴𝗶𝘀𝗸 𝗥𝗲𝗹𝗲𝗮𝘀𝗲:\n\n' 
    for name, release_url in magisk_dict.items():
        data = get(release_url).json()
        releases += f'{name}: [ZIP v{data["magisk"]["version"]}]({data["magisk"]["link"]}) | ' \
                    f'[APK v{data["app"]["version"]}]({data["app"]["link"]}) | ' \
                    f'[Uninstaller]({data["uninstaller"]["link"]})\n'
    await request.edit(releases)

@register(outgoing=True, pattern=r"^.twrp(?: |$)(\S*)")
async def twrp(request):
    """ get android device twrp """
    textx = await request.get_reply_message()
    device = request.pattern_match.group(1)
    if device:
        pass
    elif textx:
        device = textx.text.split(' ')[0]
    else:
        await request.edit("`Usage: .twrp <codename>`")
        return
    url = get(f'https://dl.twrp.me/{device}/')
    if url.status_code == 404:
        reply = f"`Couldn't find twrp downloads for {device}!`\n"
        await request.edit(reply)
        return
    page = BeautifulSoup(url.content, 'lxml')
    download = page.find('table').find('tr').find('a')
    dl_link = f"https://dl.twrp.me{download['href']}"
    dl_file = download.text
    size = page.find("span", {"class": "filesize"}).text
    date = page.find("em").text.strip()
    reply = f'**Latest TWRP for {device}:**\n' \
        f'[{dl_file}]({dl_link}) - __{size}__\n' \
        f'**Updated:** __{date}__\n'
    await request.edit(reply)
    
    
    @register(outgoing=True, pattern="^.pixeldl(?: |$)(.*)")
async def downzz(dl):
    await dl.edit("`Collecting information...`")
    URL = dl.pattern_match.group(1)
    URL_MSG = await dl.get_reply_message()
    if URL:
        pass
    elif URL_MSG:
        URL = URL_MSG.text
    else:
        await dl.edit("`Empty information...`")
        return
    if not re.findall(r'\bhttps?://download.*pixelexperience.*\.org\S+', URL):
        await dl.edit("`Invalid information...`")
        return
    driver = await chrome()
    await dl.edit("`Getting information...`")
    driver.get(URL)
    error = driver.find_elements_by_class_name("swal2-content")
    if len(error) > 0:
        if error[0].text == "File Not Found.":
            await dl.edit(f"`FileNotFoundError`: {URL} is not found.")
            return
    datas = driver.find_elements_by_class_name('download__meta')
    """ - enumerate data to make sure we download the matched version - """
    md5_origin = None
    i = None
    for index, value in enumerate(datas):
        for data in value.text.split("\n"):
            if data.startswith("MD5"):
                md5_origin = data.split(':')[1].strip()
                i = index
                break
        if md5_origin is not None and i is not None:
            break
    if md5_origin is None and i is None:
        await dl.edit("`There is no match version available...`")
    if URL.endswith('/'):
        file_name = URL.split("/")[-2]
    else:
        file_name = URL.split("/")[-1]
    file_path = TEMP_DOWNLOAD_DIRECTORY + file_name
    download = driver.find_elements_by_class_name("download__btn")[i]
    download.click()
    await dl.edit("`Starting download...`")
    file_size = human_to_bytes(download.text.split(None, 3)[-1].strip('()'))
    display_message = None
    complete = False
    start = time.time()
    while complete is False:
        if os.path.isfile(file_path + '.crdownload'):
            try:
                downloaded = os.stat(file_path + '.crdownload').st_size
                status = "Downloading"
            except OSError:  # Rare case
                await asyncio.sleep(1)
                continue
        elif os.path.isfile(file_path):
            downloaded = os.stat(file_path).st_size
            file_size = downloaded
            status = "Checking"
        else:
            await asyncio.sleep(0.3)
            continue
        diff = time.time() - start
        percentage = downloaded / file_size * 100
        speed = round(downloaded / diff, 2)
        eta = round((file_size - downloaded) / speed)
        prog_str = "`{0}` | [{1}{2}] `{3}%`".format(
            status,
            "".join(["●" for i in range(
                    math.floor(percentage / 10))]),
            "".join(["○"for i in range(
                    10 - math.floor(percentage / 10))]),
            round(percentage, 2))
        current_message = (
            "`[DOWNLOAD]`\n\n"
            f"`{file_name}`\n"
            f"`Status`\n{prog_str}\n"
            f"`{humanbytes(downloaded)} of {humanbytes(file_size)}"
            f" @ {humanbytes(speed)}`\n"
            f"`ETA` -> {time_formatter(eta)}"
        )
        if round(diff % 15.00) == 0 and display_message != current_message or (
          downloaded == file_size):
            await dl.edit(current_message)
            display_message = current_message
        if downloaded == file_size:
            if not os.path.isfile(file_path):  # Rare case
                await asyncio.sleep(1)
                continue
            MD5 = await md5(file_path)
            if md5_origin == MD5:
                complete = True
            else:
                await dl.edit("`Download corrupt...`")
                os.remove(file_path)
                driver.quit()
                return
    await dl.respond(
        f"`{file_name}`\n\n"
        f"Successfully downloaded to `{file_path}`."
    )
    await dl.delete()
    driver.quit()
    return



CMD_HELP.update({
    "android":
    ".magisk\
\nGet latest Magisk releases.\
\n\n>`.pixeldl` **<download.pixelexperience.org>**\
\nUsage: Download pixel experience ROM into your userbot server.\
\n\n.twrp <codename>\
\nUsage: Get latest twrp download for android device."
})
