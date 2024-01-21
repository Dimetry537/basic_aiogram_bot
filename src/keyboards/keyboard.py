from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Запусти GPT", callback_data="launch_gpt")],
        [InlineKeyboardButton(text="Запусти Kandinsky 3.0", callback_data="launch_kandinsky")],
        [InlineKeyboardButton(text="Мне нужна помощь", callback_data="help_needed")],
        [InlineKeyboardButton(text="Оплата", callback_data="payment")]
    ]
)


