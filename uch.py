from telegram import ForceReply, ReplyKeyboardMarkup, Update,  InlineKeyboardButton,KeyboardButton,KeyboardButtonPollType,KeyboardButtonRequestChat,KeyboardButtonRequestUser,WebAppInfo
import telegram
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        f"""Hi {user.mention_html()}! 
Id - {user.id}
Username - {user.username}
Lan: - {user.language_code}
""",
)
location_keyboard = telegram.KeyboardButton(text="send_location", request_location=True)
contact_keyboard = telegram.KeyboardButton(text="send_contact", request_contact=True)
custom_keyboard = [[ location_keyboard, contact_keyboard ]]
reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
await bot.send_message(chat_id=chat_id, 
...                  text="Would you mind sharing your location and contact with me?", 
...                  reply_markup=reply_markup)
#     await update.message.reply_text(
#         "XZCZXC",

#         reply_markup=ReplyKeyboardMarkup(KeyboardButton(
#             "test",
#             request_contact=True,
#             request_chat=KeyboardButtonRequestChat())
# ))
def main() -> None:
    application = Application.builder().token("6780350501:AAGAbcTfDuInMtdxyDh1ZG4jh5-8c3PbIt0").build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling(allowed_updates=Update.ALL_TYPES)
if __name__ == "__main__":
    main()