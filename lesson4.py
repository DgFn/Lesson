"""Домашка

Все функции валидации (validate_name, validate_age) должны всегда возвращать
None, а в случае ошибки - делать raise Exception(текст ошибки).

Использовать функцию clear_whitespaces еще и для введенной строки,
в которой должно быть число.

В функции main, необходимо отловить ошибки из функций validate_name,
validate_age. Вывести пользователю: "Я поймал ошибку: {текст ошибки}".
И если были ошибки,необходимо заново запросить у пользователя ввод данных.

В функции main обрабатывать ошибку ValueError (не используем Exception)
во время перевода строки к int.

Перед запросом данных в функции main пользователю должно печататься номер
текущей попытки ввода данных. Пользователю отображать попытки начиная с 1,
в коде попытки должны быть с 0.

Во время игры "угадай число" тоже должен быть счетчик попыток, который
будет отображаться при успешно угаданному числу.
Пользователю отображать попытки начиная с 1, в коде попытки должны быть с 0.
"""
import random


def validate_name(name: str) -> str | None:
    """ Проверка имени
    :param name: имя введеное пользователем
    :raise: возращает ошибки, если проверка не прошла
    :return возвращает None если проверки прошли
    """
    if not name or len(name) < 3:
        raise Exception('Ошибка: Недопустимое имя')

    name_array = name.split(' ')
    if '' in name_array:
        raise Exception('Ошибка: Большое количество пробелов')

    return None


def validate_age(age: int) -> str | None:
    """Проверка возраст
    :param age: возраст введенный пользователем
    :raise: возращает ошибки, если проверка не прошла
    :return: возвращает None если проверки прошли
    """
    if age <= 0:
        raise Exception('Ошибка: Недопустимый возраст')
    if age < 14:
        raise Exception("Ошибка: Минимальный возраст 14 лет")
    return None


def get_passport_advicce(name: str, age: int) -> str:
    """Функция которая выводит совет о получении паспорта


    :param age: возраст введенный пользователем
    :param name: имя введеное пользователем
    :return: возвращает совет о паспорте
    """
    if 16 <= age <= 17:
        return 'Не забудь получить свой первый паспорт!'
    if 25 <= age <= 26:
        return 'Не забудь заменить паспорт!'
    if 45 <= age <= 46:
        return 'Не забудь заменить паспорт!'
    return 'Паспорт пока не одобрят.'


def guess_number_game() -> None:
    """Функция игра, угадай число"""

    hidden_number = random.randint(1,5)
    count_user = 0
    while True:
        number_user = int(input('Попробуй угадать  число: '))
        if number_user == hidden_number:
            print(f'Вы угадали с {count_user +1} попытки ')
            break
        count_user += 1


def main() -> None:
    """Запуск всех функций"""

    count_user_validate = 0
    while True:
        name = input('Введите имя: ')
        try:
            count_user_validate += 1
            age = int(input('Введите возраст: '))
            validate_name(name)
            validate_age(age)
        except ValueError as e:
            print('Возраст не может быть строкой')
            continue
        except Exception as e:
            print(e)
            continue

        result_validation_id = get_passport_advicce(name, age)
        print(f'Привет {name}, тебе {age} лет.\n', result_validation_id,f'Количетсво попыток проверки:{count_user_validate}.')
        break
    guess_number_game()


if __name__ == '__main__':
    main()
