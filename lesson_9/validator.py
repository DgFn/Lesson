"""Модуль валидации введных данных


    Тут я использовал уже готовыю библиотеку ждя хэширования пароля
    Ее преимущества в том что она добавляет соль(какое-то количество символов) к паролю
    и вдобавок многократно хеэширует пароль
"""
import re

import bcrypt
import base64
from exceptions import ValidationError


class Validator:
    """Класс валидирует данные """

    @staticmethod
    def validate_password(password: str) -> None | bool:
        """Метод валидации пароля"""

        regex = r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{4,}'
        if re.fullmatch(regex, password) is None:
            raise ValidationError(
                'В пароле должно бытьминимум 4 символа, '
                'минимум один заглавный символ, минимум один прописной символ,'
                ' минимум одна цифра, минимум один спецсимвол.')
        return True

    @staticmethod
    def validate_email(email: str) -> None | bool:
        """Метод валидации почты"""

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex,email) is None:
            raise ValidationError('Неверно указан email')
        return True

    @staticmethod
    def hash_password(password: str) -> str:
        """Метод хэширование пароля"""

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        hashed_password = base64.b64encode(hashed_password).decode('utf-8')
        return hashed_password

    @staticmethod
    def check_hash_password(password: str, hashed_password: str) -> bool:
        """Метод проверки хэшированного пароля с введенным"""
        hashed_password = base64.b64decode(hashed_password)
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

