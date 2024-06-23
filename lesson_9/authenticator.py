"""1. Делаем систему регистрации-авторизации:

Создаем класс `Authenticator` в модуле `authenticator`. Методы класса:

1. Конструктор. В нем создаются переменные экземпляра класса `self.login:
 str | None`, `self._password | None`,
 `self.last_success_login_at: datetime | None`,
 `self.errors_count: int`.
 По умолчанию у этих переменных должно быть `None` значение.
  У переменной `errors_count` значение 0. Вызывает метод `_is_auth_file_exist`.
  Если файл существует, вызвать метод `_read_auth_file`.

2. `_is_auth_file_exist` - Проверяем наличие файла `auth.txt`
рядом (в той же папке).
Не принимает аргументов, возвращает `bool` значение.
 `True` - файл авторизации существует. `False` - не существует.

3. `_read_auth_file` - Чтение данных из файла `auth.txt`.
Данные из файла записываем в переменные объекта класса
созданные ранее (`self.login`, `self._password`, etc).
Ничего не возвращает. В файле должно быть 4 строки:

1. Логин

2. Пароль

3. `datetime.utcnow().isoformat()` строка, которую нужно перевести
к `datetime` объекту

4. количество проваленных попыток (ошибки)

4. `authorize(login, password)` - Проверка логина и пароля.
 Принимает аргументы строки логина и пароля. Сравнивает логин и
 пароль из аргументов с логином и паролем из файла.
 Если логин и пароль неверные, вызывает исключение
 `AuthorizationError` (нужно создать этот класс в соответствующем месте)
  и увеличиваем счетчик проваленных попыток-ошибок и перезаписываем в файле
   - вызывает метод `_update_auth_file`. Если `self.login` имеет `None`
   значение, вызвать ошибку `AuthorizationError`.

5. `_update_auth_file` - Перезапись файла `auth.txt`.
Не принимает аргументов, не возвращает ничего.
Метод должен перезаписать количество попыток авторизации и время авторизации,
 что лежат в переменных экземпляра.

6. `registrate(login, password)` - Регистрация пользователя.
Принимает аргументы строки логина и пароля.
Делает проверку, что файла рядом `auth.txt` нет.
Если он есть, вызывает исключение `RegistrationError`
(нужно создать этот класс в соответствующем месте).
Создает файл `auth.txt` и сохраняет туда логин, пароль,
`datetime.utcnow().isoformat()`, количество проваленных попыток
(ошибки) при попытке регистрации (Вызывает метод `_update_auth_file`).
Если `self.login` имеет НЕ `None` значение, вызвать ошибку `RegistrationError`.

2. В `main` функции (в файле `main.py`) создаем объект класса `Authenticator`.

3. Проверяем, что у объекта класса `Authenticator` есть логин
(не None значение). Если его нет, сказать пользователю, что он
проходит регистрацию.
Если логин есть, сказать, что нужно для авторизации вести логин и пароль.

4. В бесконечном цикле запрашиваем у пользователя логи и пароль.
 Нужно либо зарегистрировать пользователя, либо авторизовать в зависимости от предыдущей
  проверки в пункте выше. Обрабатывать ошибки, вызываемые методами класса `Authenticator`.

5. Удаляем весь код с подсказкой паспорта, ввода имени и возраста.
Класс валидатора, модуль валидатора и ошибку валидации удаляем
(но не забываем, что это должно быть все в гит истории, потому что к этому вернемся).

6. Приветствуем пользователя: пишем логин, время последней успешной авторизации
(формат `день.месяц.год час:минута:секунда`)
 и сколько раз пытались войти в приложение с ошибкой авторизации.

7. Запускаем игру в отгадайку рандомного числа."""

from datetime import datetime
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

    def _is_auth_file_exist(self):
        """Проверяет наличие файла для обработки"""
        if os.path.isfile('..\\lesson_9\\auth.txt'):
            return True
        return False

    def _read_auth_file(self):
        """Записываем данные из файла"""
        with open('..\\lesson_9\\auth.txt', 'r') as f:
            self.login = f.readline()
            self._password = f.readline()
            self.last_success_login_at = datetime.fromisoformat(eval(f.readline()))
            self.errors_count = int(f.readline())

    def _update_auth_file(self):
        """Обновляет данные в файле"""
        with open('..\\lesson_9\\auth.txt', 'w') as f:
            f.write(self.login)
            f.write(self._password)
            f.write('datetime.utcnow().isoformat()\n')
            f.write(f'{self.errors_count}')

    def registrate(self, login: str | None, password: str | None) -> None:
        """Регистрирует пользователя"""
        if os.path.isfile('..\\lesson_9\\auth.txt'):
            self.errors_count += 1
            self._update_auth_file()
            raise RegistrationError('Файл с данным уже создан')

        if self.login is not None:
            raise RegistrationError('Логин не может быть заполненым')

        with open('\\auth.txt', 'w') as f:
            f.write(f'{login}\n')
            f.write(f'{password}\n')
            f.write('datetime.utcnow().isoformat()\n')
            f.write(f'{self.errors_count}')

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