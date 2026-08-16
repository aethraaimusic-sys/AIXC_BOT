import os
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import Update
from telegram.ext import Application
from telegram.ext import CallbackQueryHandler
from telegram.ext import CommandHandler
from telegram.ext import ContextTypes

TOKEN = os.getenv(8647168718:AAFCJLnBRNaFpgQjamAOt1bmGH8UuXwR2ys)


def main_menu():

    keyboard = [

        [
            InlineKeyboardButton(
                "💰 Investment",
                callback_data="investment"
            ),

            InlineKeyboardButton(
                "📚 Courses",
                callback_data="courses"
            )
        ],

        [
            InlineKeyboardButton(
                "💳 Deposit",
                callback_data="deposit"
            ),

            InlineKeyboardButton(
                "💸 Withdraw",
                callback_data="withdraw"
            )
        ]

    ]

    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🤖 AIXC Bot is online.",
        reply_markup=main_menu()
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    await query.edit_message_text(
        f"You selected: {query.data}",
        reply_markup=main_menu()
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(CallbackQueryHandler(buttons))

if __name__ == "__main__":
    app.run_polling()
