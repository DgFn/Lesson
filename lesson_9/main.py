from authenticator import Authenticator
from exceptions import AuthorizationError, RegistrationError


def main() -> str:
    """Запуск всех модулей"""

    authentication = Authenticator()
    if authentication.login:
        print('Вам нужно авторизоваться')
    else:
        print('Вам нужно зарегистрироватся')
    while True:
        login = input('Введите логин:')
        password = input('Введите пароль:')
        if authentication.login:
            try:
                authentication.authorize(login, password)
            except AuthorizationError as e:
                print(e)
                continue
            result = (f'Добро пожаловать {authentication.login.strip()}!\nВремя в которое вы зашли: '
                      f'{authentication.last_success_login_at.strftime('%H:%M:%S')}\n'
                      f'Количество неверных попыток:{authentication.errors_count}')
            print(result)
            return result

        try:
            authentication.registrate(login, password)

        except RegistrationError as e:
            print(e)
            continue
        print('Вы успешно зарегистрированны, авторизуйтесь!')


# регистрация отдельно, авторизацая в блоке ry

if __name__ == '__main__':
    main()
