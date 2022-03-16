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

    # rate_button = _("🌟 Оценить этого бота")
    # markup.add(KeyboardButton(rate_button))

    return markup


def additional_keyb():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [[_('🥳 Моё день рождение'), _('🎊 Праздники')],
               [_('🔢 Номер дня в году'), _('⏳ Сколько дней')]]
    for text_1, text_2 in buttons:
        markup.add(KeyboardButton(text_1),
                   KeyboardButton(text_2))

    markup.add(KeyboardButton(text=_("↪️ Назад в главное меню")))
    return markup


hol_cb = CallbackData("holidays", "hol_name")


def holidays_keyb():
    markup = InlineKeyboardMarkup(row_width=1)
    buttons = {
        _("Международные праздники"): "ih",
        _("Праздник сегодня"): "todayh",
        _("smth"): "ny",
    }

    for text, data in buttons.items():
        markup.insert(
            InlineKeyboardButton(
                text=text,
                callback_data=hol_cb.new(hol_name=data)
            )
        )
    return markup


def inter_holidays_keyb():
    markup = InlineKeyboardMarkup(row_width=1)
    buttons = {
        _("🌹 Международный женский день"): "iwd",
        _("Новый Год"): "ny",
        _("Навруз"): "navruz",
        _("Назад"): "back_holiday"
    }

    for text, data in buttons.items():
        markup.insert(
            InlineKeyboardButton(
                text=text,
                callback_data=hol_cb.new(hol_name=data)
            )
        )
    return markup


hol_pag_cb = CallbackData("hol_pg", "action")


def change_hol_keyb(page: int = 1):
    markup = InlineKeyboardMarkup()
    buttons = {
        "<<": page - 1,
        "Назад": "back_inter",
        ">>": page + 1
    }
    for text, data in buttons.items():
        markup.insert(
            InlineKeyboardButton(
                text=text,
                callback_data=hol_pag_cb.new(action=data)
            )
        )

    return markup


def choose_dy_keyb():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    buttons = [[_('Текущая дата'), _('Конкретная дата')]]
    for text_1, text_2 in buttons:
        markup.add(KeyboardButton(text_1),
                   KeyboardButton(text_2))
    markup.add(KeyboardButton(text=_("↪️ Назад")))
    return markup


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
            InlineKeyboardButton(text="🇺🇦 Український", callback_data=lang_cb.new(name="uk"))
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


bd_data = CallbackData("bd_people", "page", "action")


def bd_today_list(max_pages: int, page: int = 1):
    markup = InlineKeyboardMarkup()
    previous_page = page - 1
    previous_page_text = "<<"

    current_user_text = _("Поздравить")
    current_page_text = _("{page} из {max_pages}").format(page=page, max_pages=max_pages)

    next_page = page + 1
    next_page_text = ">>"

    markup.insert(
        InlineKeyboardButton(
            text=previous_page_text,
            callback_data=bd_data.new(page=previous_page, action="left")
        )
    )

    markup.insert(
        InlineKeyboardButton(
            text=current_page_text,
            callback_data=bd_data.new(page=page, action="current_page")
        )
    )

    markup.insert(
        InlineKeyboardButton(
            text=next_page_text,
            callback_data=bd_data.new(page=next_page, action="right")
        )
    )

    markup.add(
        InlineKeyboardButton(
            text=current_user_text,
            callback_data=bd_data.new(page=page, action="gratz")
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
