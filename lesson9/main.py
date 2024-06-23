from authenticator import Authenticator
from exceptions import AuthorizationError, RegistrationError


def main() -> str:
    """Запуск всех модулей"""

    while True:
        authentication = Authenticator()
        try:
            if authentication.login:
                login = input('Введите логин:')
                password = input('Введите пароль:')
                authentication.authorize(login, password)
                result = (f'Добро пожаловать {authentication.login.strip()}!\nВремя в которое вы зашли: '
                          f'{authentication.last_success_login_at.strftime('%H:%M:%S')}\n'
                          f'Количество неверных попыток:{authentication.errors_count}')
                print(result)
                return

            login = input('Вам нужно зарегистрироваться введите логин: ')
            password = input('Придумайте пароль:')
            print('Вы успешно зарегистрированны, авторизуйтесь!')
            authentication.registrate(login, password)

        except AuthorizationError as e:
            print(e)
            continue
        except RegistrationError as e:
            print(e)
            continue


if __name__ == '__main__':
    main()
