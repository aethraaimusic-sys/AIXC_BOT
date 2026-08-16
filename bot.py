from telegram import Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

from keyboards import home_keyboard
from screens import home_screen

TOKEN = "YOUR_BOT_TOKEN"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        home_screen(update.effective_user.first_name),
        reply_markup=home_keyboard(),
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    await query.edit_message_text(
        text=f"You selected: {query.data}",
        reply_markup=home_keyboard(),
    )


def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CallbackQueryHandler(buttons)
    )

    print("AIXC Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
