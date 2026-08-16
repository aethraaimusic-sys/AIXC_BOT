from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import Update
from telegram.ext import Application
from telegram.ext import CallbackQueryHandler
from telegram.ext import CommandHandler
from telegram.ext import ContextTypes

TOKEN = "8647168718:AAEf5mJDuVF0a1t2ceON5-Cmc3mmv-XGSww"


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
        ],

        [
            InlineKeyboardButton(
                "👥 Referrals",
                callback_data="referrals"
            ),

            InlineKeyboardButton(
                "📊 Transactions",
                callback_data="transactions"
            )
        ],

        [
            InlineKeyboardButton(
                "👤 Profile",
                callback_data="profile"
            ),

            InlineKeyboardButton(
                "📞 Support",
                callback_data="support"
            )
        ]

    ]

    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(

        "🤖 Welcome to Austin Investment X Course (AIXC)",

        reply_markup=main_menu()

    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    await query.edit_message_text(

        f"You selected: {query.data}",

        reply_markup=main_menu()

    )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(CallbackQueryHandler(button))

app.run_polling()