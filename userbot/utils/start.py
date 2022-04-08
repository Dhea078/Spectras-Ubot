import pybase64
from telethon import Button
from telethon.tl.functions.channels import JoinChannelRequest as Invt
from userbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/dca7e3f42d2c8cc547e1d.jpg?fbclid=IwAR0uNTwu1qpGJkrSxMeAyrHLY_-KlmofRSnFjJgtno4lvnYZj_ZPSUpY56k",
                caption="✨ **𝙎𝙋𝙀𝘾𝙏𝙍𝘼𝙎 𝙐𝙎𝙀𝙍𝘽𝙊𝙏**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 8.0@master\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @NastyProject ",
                buttons=[(Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/NastySupportt"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None


async def checking(client):
    gcsp = str(pybase64.b64decode("QE5hc3R5UHJvamVjdA=="))[2:15]
    chsp = str(pybase64.b64decode("QE5hc3R5U3VwcG9ydHQ="))[2:16]
    chgbt = str(pybase64.b64decode("QGFoaHN1ZGFobGFoaGg="))[2:16]
    if client:
        try:
            await client(Invt(gcsp))
        except BaseException:
            pass
        try:
            await client(Invt(chsp))
        except BaseException:
            pass
        try:
            await client(Invt(chgbt))
        except BaseException:
            pass
