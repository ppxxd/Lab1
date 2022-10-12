class Error(Exception):
    """Базовый класс для ошибок"""
    pass


class ValueIsNotValid(Error):
    """Когда опция меньше 1 или больше 9"""
    pass


class UserExists(Error):
    """Когда юзер существует уже в базе"""
    pass