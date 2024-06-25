"""Домашка до среды:

Написать декоратор для функции main, в котором будет в бесконечном цикле вызов
main до тех пор, пока main функция не вернет значение True.
True значение должно вернуться в том случае, если в main не было
ни одной ошибки авторизации и пользователь был успешно авторизовано/зарегистрирован
"""

from authenticator import Authenticator
from exceptions import AuthorizationError, RegistrationError


def cycle(func):
    def wrapper():
        while True:

            if func():
                return

    return wrapper


@cycle
def main() -> bool:
    """Запуск всех модулей"""

    authentication = Authenticator()
    if authentication.login:
        print('Вам нужно авторизоваться')
    else:
        print('Вам нужно зарегистрироватся')

    login = input('Введите логин:')
    password = input('Введите пароль:')

    if authentication.login:
        try:
            authentication.authorize(login, password)
        except AuthorizationError as e:
            print(e)
            return False
        result = (f'Добро пожаловать {authentication.login.strip()}!\nВремя в которое вы зашли: '
                  f'{authentication.last_success_login_at.strftime('%H:%M:%S')}\n'
                  f'Количество неверных попыток:{authentication.errors_count}')
        print(result)
        return True

    try:
        authentication.registrate(login, password)

    except RegistrationError as e:
        print(e)
        return False
    print('Вы успешно зарегистрированны, авторизуйтесь!')


if __name__ == '__main__':
    main()
