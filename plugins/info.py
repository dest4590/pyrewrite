import os
import platform
import sys

from pyrogram import Client, filters
from pyrogram.types import Message

from utils.config import cfg
from utils.help import help_menu
from utils.i18n import i18n
from utils.prefix import prefix

SYSTEM = "Linux 🐧" if os.name == "posix" else "Windows 💻"

if os.name == "posix":
    if "termux" in sys.executable.lower():
        SYSTEM = "Termux 📱"
    else:
        import distro

        SYSTEM = distro.name(pretty=False)

default = i18n.get['cmds']['info-module-default-text'].format(prefix, SYSTEM, platform.node(), str(help_menu.get_len()), str(help_menu.get_len_buildin()), str(help_menu.get_len_custom()))

def get_info_menu(info_type="full"):
    """Returns info text by info_type param"""
    if info_type == "full":
        return default

    if info_type == "lite":
        return i18n.get['cmds']['info-module-lite-text'].format(prefix, str(help_menu.get_len()))

    return default


@Client.on_message(filters.command("info", prefixes=prefix.symbol) & filters.me)
async def info(client: Client, message: Message):
    chat_id = message.chat.id
    await message.delete()
    if message.reply_to_message is not None:
        await client.send_animation(
            chat_id,
            cfg.sets["banner", "https://envs.sh/hkf.mp4"],
            get_info_menu(cfg.sets["info"]),
            reply_to_message_id=message.reply_to_message.id,
        )
    else:
        await client.send_animation(
            chat_id,
            cfg.sets["banner", "https://envs.sh/hkf.mp4"],
            get_info_menu(cfg.sets["info"]),
        )

help_menu.command("info", i18n.get['cmds']['info-module-help-short-desc'], i18n.get['cmds']['info-module-help-long-desc'])