from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup


def home_keyboard():

    return InlineKeyboardMarkup([

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

    ])
