"""Модуль регистрации и авторизации"""

from datetime import datetime, UTC
import os

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
        return os.path.isfile('auth.txt')

    def _read_auth_file(self):
        """Записываем данные из файла"""
        with open('auth.txt', 'r') as f:
            self.login = f.readline()
            self._password = f.readline()
            self.last_success_login_at = datetime.fromisoformat((f.readline().strip()))
            self.errors_count = int(f.readline())

    def _update_auth_file(self):
        """Обновляет данные в файле"""
        with open('auth.txt', 'w') as f:
            f.write(f'{self.login.strip()}\n')
            f.write(f'{self._password.strip()}\n')
            f.write(f'{datetime.now(tz=UTC).isoformat()}\n')
            f.write(str(self.errors_count))

    def registrate(self, login: str | None, password: str | None) -> None:
        """Регистрирует пользователя"""
        if os.path.isfile('auth.txt'):
            self.errors_count += 1
            raise RegistrationError('Файл с данным уже создан')

        if self.login is not None:
            raise RegistrationError('Логин не может быть заполненым')
        self.login = login
        self._password = password
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
        if login == self.login.strip() and password == self._password.strip():
            self._update_auth_file()
            return True

        self.errors_count += 1
        self._update_auth_file()
        raise AuthorizationError("Неверный логин или пароль!")
