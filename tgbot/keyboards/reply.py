from aiogram.types import KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from tgbot.middlewares.lang_middleware import _


def main_keyb():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    my_profile = _("👤 Мой профиль")
    markup.add(KeyboardButton(my_profile))

    buttons = [[_('🎊 У кого сегодня день рождение'), _('🌐 Поменять язык')],
               [_('🌀 Прочее'), _('❔ Помощь')]]

    for text_1, text_2 in buttons:
        markup.add(KeyboardButton(text_1),
                   KeyboardButton(text_2))

    return markup


def additional_keyb():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [[_('🥳 Моё день рождение'), _('🎊 Праздники [beta]')],
               [_('🔢 Номер дня в году'), _('⏳ Сколько дней')]]
    for text_1, text_2 in buttons:
        markup.add(KeyboardButton(text_1),
                   KeyboardButton(text_2))

    markup.add(KeyboardButton(text=_("↪️ Назад в главное меню")))
    return markup


# HOLIDAYS KEYBOARD

# END OF HOLIDAYS


def back_keyb():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton(text=_("↪️ Назад")))
    return markup


def cancel_keyb():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton(text=_("↪️ Назад в главное меню")))
    return markup


lang_cb = CallbackData("language", "name")

lang_keyb = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇸 English", callback_data=lang_cb.new(name="en")),
            InlineKeyboardButton(text="🇷🇺 Русский", callback_data=lang_cb.new(name="ru"))
        ],
        [
            InlineKeyboardButton(text="🇺🇿 O'zbek", callback_data=lang_cb.new(name="uz")),
            InlineKeyboardButton(text="🇺🇦 Український", callback_data=lang_cb.new(name="ua"))
        ],
        [
            InlineKeyboardButton(text="🇪🇸 Español", callback_data=lang_cb.new(name="es")),
            InlineKeyboardButton(text="🇫🇷 Français", callback_data=lang_cb.new(name="fr"))
        ]
    ]
)


def share_message(action: str):
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton(
        text=_("Поделиться сообщением"),
        switch_inline_query=action
    ))

    return markup


def switch_to_bot():
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton(
        text=_("Перейти к боту"),
        url="t.me/totalyclearbot"
    ))

    return markup


switch_or_gratz_cb = CallbackData("gratz", "birthday_man_id")


def switch_or_gratz(user_bday: int):
    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton(
            text=_("Поздравить"),
            callback_data=switch_or_gratz_cb.new(birthday_man_id=str(user_bday))
        ),
        InlineKeyboardButton(
            text=_("Перейти к боту"),
            url="t.me/totalyclearbot"
        )
    )

    return markup


def profile_back_manual():
    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton(
            text=_("Назад"),
            callback_data="back_profile"
        )
    )

    return markup
