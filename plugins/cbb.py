#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b> ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>ᴘxᴢᴛᴇᴀᴍ</a>\nꜱᴜᴘᴘᴏʀᴛ : <a href='https://t.me/noobPrivate'>noob Support</a>\nꜱᴜᴘᴘᴏʀᴛ ᴜᴘᴅᴀᴛᴇ : <a href='https://t.me/noobPrivate'>noob Support</a>\nꜱᴛᴏʀᴇ : <a href='https://t.me/noob_je'>ᴘxᴢꜱᴛᴏʀᴇ </a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('🛃 ᴅᴇᴠᴇʟᴏᴘᴇʀ 1', url='https://telegram.im/noob_je'),
                    InlineKeyboardButton('🛃 ᴅᴇᴠᴇʟᴏᴘᴇʀ 2', url='https://telegram.im/l_abani')],
                   [ InlineKeyboardButton('🛂 ꜱᴜᴘᴘᴏʀᴛ ', url='https://t.me/HRBsupport')],
                   [InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")]
                
                ]
            )
        )
    elif data == "donate":
        await query.message.edit_text(
            text = f"<b>DONATE - NoobFamily</b>\nJika kalian suka sama video yang kami bagikan secara gratis/bayaran, ingin berbagi (donasi) kepada PXZteam? Silahkan pilih via donasi\n If you like the videos we share for free/paid, want to share (donate) to PXZteam? Please choose via donation",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
              [  InlineKeyboardButton('🧾 ꜱᴀᴡᴇʀɪᴀ', url='https://telegram.im/noob_je'),
                InlineKeyboardButton('🧾 ᴘᴀʏᴘᴀʟ', url='https://telegram.im/noob_je')
          ],
                [InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")]
                
            ])            
        )
    elif data == "premium":
        await query.message.edit_text(
            text = f"<b>List To Be Premium of PXZVip\n<blockquote>100 video 5k\n200 video 10k\n300 video 15k\n400 video 20k\n500 video 25k\n600 video 30k\n\nIF YOU WANT BUY VIP, PLEASE CONTACT</blockquote></b>",
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('🔓 ꜱᴀᴡᴇʀɪᴀ', url='https://telegram.im/noob_je'),
                InlineKeyboardButton('🔓 ᴘᴀʏᴘᴀʟ', url='https://telegram.im/noob_je')],
                [InlineKeyboardButton('🛂 ᴄᴏɴᴛᴀᴄᴛ', url='https://telegram.im/noob_je')],
                [InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")]
            ])            
        )
    elif data == "promotion":
        await query.message.edit_text(
            text = f"<b>IF YOU WANT PROMOTION VIDEO/PHOTO/ETC CONTACT STORE TEAM👇</b>",
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('🤖 ᴄᴏɴᴛᴀᴄᴛ', url='https://telegram.im/noob_je'),
                InlineKeyboardButton('📤 ᴜᴘʟᴏᴀᴅᴇᴅ', url='https://telegram.im/NoobPrivate')],
                [
                InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")]
            ])            
    )
        
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
