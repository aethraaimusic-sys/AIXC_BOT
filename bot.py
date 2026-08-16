from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

TOKEN = "8647168718:AAFCJLnBRNaFpgQjamAOt1bmGH8UuXwR2ys"


def home_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("💰 Invest", callback_data="invest"),
            InlineKeyboardButton("📚 Courses", callback_data="courses"),
        ],
        [
            InlineKeyboardButton("💳 Deposit", callback_data="deposit"),
            InlineKeyboardButton("💸 Withdraw", callback_data="withdraw"),
        ],
        [
            InlineKeyboardButton("👥 Referrals", callback_data="referrals"),
            InlineKeyboardButton("📊 History", callback_data="history"),
        ],
        [
            InlineKeyboardButton("👤 Profile", callback_data="profile"),
            InlineKeyboardButton("📞 Support", callback_data="support"),
        ],
    ])


def page(text):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🏠 Home", callback_data="home")]
    ]), text


PAGES = {
    "home": """
🤖 AUSTIN INVESTMENT X COURSE

👋 Welcome

💰 Balance: $0.00
📈 Active Investment: $0.00
💵 Earnings: $0.00
👥 Referrals: 0

Choose an option below.
""",
    "invest": """
💰 INVESTMENT CENTER

🥉 Starter - $200
🥈 Silver - $500
🥇 Gold - $800
💎 Platinum - $1000
👑 VIP - $1500
""",
    "courses": """
📚 COURSES

📈 Beginner Trading
📊 Technical Analysis
🕯️ Candlestick Patterns
⚠️ Risk Management
🧠 Trading Psychology
""",
    "deposit": """
💳 DEPOSIT CENTER

₮ USDT (TRC20)

₮ USDT (BEP20)
""",
    "withdraw": """
💸 WITHDRAWAL CENTER

Minimum withdrawal: $60
""",
    "referrals": """
👥 REFERRAL CENTER

Referral reward: 1.5%
""",
    "history": """
📊 TRANSACTION HISTORY
""",
    "profile": """
👤 PROFILE

Balance: $0.00

Status: Active
""",
    "support": """
📞 SUPPORT CENTER
"""
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name

    await update.message.reply_text(
        PAGES["home"].replace("Welcome", f"Welcome, {user}"),
        reply_markup=home_keyboard(),
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    await query.answer()

    if query.data == "home":
        await query.edit_message_text(
            PAGES["home"],
            reply_markup=home_keyboard(),
        )
        return

    keyboard, text = page(PAGES[query.data])

    await query.edit_message_text(
        text,
        reply_markup=keyboard,
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))

app.run_polling()
