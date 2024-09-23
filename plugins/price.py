#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "price":
        await query.message.edit_text(
            text = f"<b> ʜᴀʀɢᴀ ʏᴀɴɢ ᴋᴀᴍɪ ᴄᴀɴᴛᴜᴍᴋᴀɴ ᴅᴇɴɢᴀɴ ʜᴀʀɢᴀ ʀᴇɴᴅᴀʜ (ᴍᴜʀᴀʜ) 600 ᴠɪᴅᴇᴏ (30ᴋ/330🌟)
ᴜɴᴛᴜᴋ ʟᴇʙɪʜ ʟᴀɴᴊᴜᴛ, ꜱɪʟᴀʜᴋᴀɴ ʜᴜʙᴜɴɢɪ ᴋᴀᴍɪ

(ᴇɴɢʟɪꜱʜ)
ᴛʜᴇ ᴘʀɪᴄᴇ ᴡᴇ ʟɪꜱᴛ ɪꜱ ʟᴏᴡ (ᴄʜᴇᴀᴘ)
600 ᴠɪᴅᴇᴏꜱ (30ᴋ/330🌟)ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ, ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴜꜱ   </b>",
          disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('🛃 1ᴅᴇᴠᴇʟᴏᴘᴇʀ ', url='https://t.me/dammingyu'),
                    InlineKeyboardButton('🛃 2ᴅᴇᴠᴇʟᴏᴘᴇʀ ', url='https://t.me/PXZteam')],
                    
                   [InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")],
                
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
