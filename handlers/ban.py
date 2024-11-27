from aiogram import Router, types
from aiogram.exceptions import TelegramBadRequest
from datetime import timedelta


ban_router = Router()

BANNED_WORDS = {"запрет", "пример", "слово"}

@ban_router.message()
async def check_message_for_banned_words(message: types.Message):
    if any(word in message.text.lower() for word in BANNED_WORDS):
        try:
            await message.chat.ban(user_id=message.from_user.id)
            await message.answer(
                f"Пользователь {message.from_user.full_name} был забанен за использование запрещённых слов."
            )
            await message.delete()
        except TelegramBadRequest as e:
            await message.reply(f"Ошибка при бане пользователя: {e}")

@ban_router.message(commands=["бан"])
async def command_ban(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение пользователя, которого нужно забанить.")
        return

    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.reply("Укажите срок бана. Например: `бан 1д`, `бан 3ч`, `бан 10м`.")
        return

    time_str = args[1]
    duration_mapping = {"д": "days", "ч": "hours", "н": "weeks", "м": "minutes"}
    try:
        unit = time_str[-1]
        value = int(time_str[:-1])
        if unit not in duration_mapping:
            raise ValueError("Неверный формат времени.")
        kwargs = {duration_mapping[unit]: value}
        ban_duration = timedelta(**kwargs)
    except (ValueError, KeyError):
        await message.reply("Неверный формат времени. Используйте `1д`, `3ч`, `10м`.")
        return

    try:
        user = message.reply_to_message.from_user
        await message.chat.ban(user_id=user.id, until_date=ban_duration)
        await message.answer(f"Пользователь {user.full_name} был забанен на {time_str}.")
    except TelegramBadRequest as e:
        await message.reply(f"Не удалось забанить пользователя: {e}")
