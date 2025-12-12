#
# Copyright (C) 2025-2026 by OyeKanhaa@Github, < https://github.com/OyeKanhaa >.
#
# This file is part of < https://github.com/OyeKanhaa/KanhaMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/OyeKanhaa/KanhaMusic/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import Message

from KanhaMusic import app
from KanhaMusic.core.call import Kanha
from KanhaMusic.utils.database import get_assistant

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await Kanha.stop_stream_force(message.chat.id)


@app.on_message(filters.left_chat_member, group=69)
async def bot_kick(_, msg: Message):
    if msg.left_chat_member.id == app.id:
        ub = await get_assistant(msg.chat.id)
        try:
            await ub.leave_chat(msg.chat.id)
        except:
            pass
