from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

from keyboards import home_keyboard
from screens import home_screen

TOKEN = "8647168718:AAFCJLnBRNaFpgQjamAOt1bmGH8UuXwR2ys"


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(

        home_screen(
            update.effective_user.first_name
        ),

        reply_markup=home_keyboard()

    )


app = Application.builder().token(TOKEN).build()

app.add_handler(
    CommandHandler(
        "start",
        start
    )
)

app.run_polling()
