from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

# Replace this with your actual bot token
TOKEN = "8647168718:AAFCJLnBRNaFpgQjamAOt1bmGH8UuXwR2ys"


def main_menu():

    keyboard = [
        [
            InlineKeyboardButton(
                "💰 Investment",
                callback_data="investment",
            ),
            InlineKeyboardButton(
                "📚 Courses",
                callback_data="courses",
            ),
        ],
        [
            InlineKeyboardButton(
                "💳 Deposit",
                callback_data="deposit",
            ),
            InlineKeyboardButton(
                "💸 Withdraw",
                callback_data="withdraw",
            ),
        ],
        [
            InlineKeyboardButton(
                "👥 Referrals",
                callback_data="referrals",
            ),
            InlineKeyboardButton(
                "📊 Transactions",
                callback_data="transactions",
            ),
        ],
        [
            InlineKeyboardButton(
                "👤 Profile",
                callback_data="profile",
            ),
            InlineKeyboardButton(
                "📞 Support",
                callback_data="support",
            ),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🤖 Welcome to Austin Investment X Course (AIXC)\n\nChoose an option below.",
        reply_markup=main_menu(),
    )


async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    query = update.callback_query

    await query.answer()

    await query.edit_message_text(
        f"You selected: {query.data}",
        reply_markup=main_menu(),
    )


def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CallbackQueryHandler(button_handler)
    )

    print("Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
