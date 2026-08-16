from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup


def home_keyboard():

    keyboard = [

        [
            InlineKeyboardButton(
                "💰 Invest",
                callback_data="invest"
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
                "📊 History",
                callback_data="history"
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
