import asyncio
import importlib
from sys import argv
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from Tsukino_Music import LOGGER, app, userbot
from Tsukino_Music.core.call import Hotty
from Tsukino_Music.misc import sudo
from Tsukino_Music.plugins import ALL_MODULES
from Tsukino_Music.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

from Tsukino_Music.plugins.tools.clone import restart_bots




async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Tsukino_Music.plugins" + all_module)
    LOGGER("Tsukino_Music.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Hotty.start()
    try:
        await Hotty.stream_call("https://graph.org/file/e999c40cb700e7c684b75.mp4")
    except NoActiveGroupCall:
        LOGGER("Tsukino_Music").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Hotty.decorators()
    LOGGER("Tsukino_Music").info(
        "ᴅʀᴏᴘ ʏᴏᴜʀ ɢɪʀʟꜰʀɪᴇɴᴅ'ꜱ ɴᴜᴍʙᴇʀ ᴀᴛ @Tsukino_Music ᴊᴏɪɴ @LB_Music_Bot , @Tsukino_Music ꜰᴏʀ ᴀɴʏ ɪꜱꜱᴜᴇꜱ"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("Tsukino_Music").info("Stopping Brandrd Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())