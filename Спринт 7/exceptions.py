class TelegramError(Exception):
    """Ошибка телеграма."""
    pass


class InvalidResponseCodeError(Exception):
    """Не верный код ответа."""
    pass


class EmptyResponseFromAPIError(Exception):
    """Пустой ответ от API."""
    pass
