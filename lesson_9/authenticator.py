"""Модуль регистрации и авторизации"""
import json
from datetime import datetime, UTC
import os
from validator import Validator
from exceptions import AuthorizationError, RegistrationError


class Authenticator:
    def __init__(self):
        self.login: str | None = None
        self._password: str | None = None
        self.last_success_login_at: datetime | None = None
        self.errors_count: int = 0
        if self._is_auth_file_exist():
            self._read_auth_file()

    @staticmethod
    def _is_auth_file_exist():
        """Проверяет наличие файла для обработки"""
        return os.path.isfile('auth.json')

    def _read_auth_file(self):
        """Записываем данные из файла"""
        with open('auth.json', 'r') as f:
            data = json.loads(f.read())
            self.login = data["login"]
            self._password = data["password"]
            self.last_success_login_at = datetime.fromisoformat(data["last_success_login_at"])
            self.errors_count = data["errors_count"]

    def _update_auth_file(self):
        """Обновляет данные в файле"""
        with open('auth.json', 'w') as f:
            data = {
                'login': self.login,
                'password': self._password,
                #Так как у Json нет объекта datitme, было решено использовать
                #isoformat, потому что он возращает строку, которая может
                # сохранится в json
                'last_success_login_at': datetime.now(tz=UTC).isoformat(),
                'errors_count': self.errors_count
            }
            json.dump(data, f)

    def registrate(self, login: str | None, password: str | None) -> None:
        """Регистрирует пользователя"""
        if os.path.isfile('auth.json'):
            self.errors_count += 1
            raise RegistrationError('Файл с данным уже создан')

        if self.login is not None:
            raise RegistrationError('Логин не может быть заполненым')
        if Validator.validate_password(password) and Validator.validate_email(login):
            self.login = login
            self._password = Validator.hash_password(password)
            self.last_success_login_at = datetime.now(tz=UTC)
            self._update_auth_file()

    def authorize(self, login: str | None, password: str | None) -> bool | str:
        """ `authorize(login, password)` - Проверка логина и пароля.


                Принимает аргументы строки логина и пароля.
                Сравнивает логин и пароль из аргументов с логином и паролем из файла.
                Если логин и пароль неверные, вызывает исключение `AuthorizationError`
                (нужно создать этот класс в соответствующем месте) и увеличиваем счетчик п
                роваленных попыток-ошибок и перезаписываем в файле -
                вызывает метод `_update_auth_file`.
                Если `self.login` имеет `None`
                значение, вызвать ошибку `AuthorizationError`."""
        if self.login is None:
            raise AuthorizationError('Недопустимый логин')
        if login == self.login.strip() and Validator.check_hash_password(password, self._password):
            self._update_auth_file()
            return True

        self.errors_count += 1
        self._update_auth_file()
        raise AuthorizationError("Неверный логин или пароль!")
