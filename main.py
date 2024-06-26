"""
1. Создать модуль `exceptions`, в нем класс `ValidationError`,
который наследуется от `Exception`. Никакие методы,
   свойства переопределять не нужно, необходимо только описать в docstring
   , что это класс ошибки валидации данных.
2. Создать модуль `validator`, в котором:
    1. Реализовать класс `Data`, конструктор которого принимает `name` и `age`
     аргументы, сохраняет их в одноименные
       переменные экземпляра класса. Так же у этого класса должен быть метод
       `_clear_whitespaces`, который очищает от
       пробелов в на+-чале и в конце переменные `name` и `age` у
    экземпляра класса. Вызывать метод `_clear_whitespaces`
       необходимо из конструктора класса.
    2. Реализовать класс `DataWithDate`, наследовавшись от класса `Data`.
    Конструктор должен делать то же самое, что и
       родительский класс, но дополнительно сохраяняет текущее время, когда
        был создан этот экземпляр класса (
       см. `datetime.utcnow`).
    3. Реализовать класс `Validator`.
    У класса `Validator` должны быть следующие методы:
        1. конструктор класса — в экземпляре класса создает переменную `
        data_history`, которая является пустым списком,
           но будет хранить объекты класса `Data`.
        2. `_validate_name` — валидация имени
        (скопировать код из функции `validate_name`).
        3. `_validate_age` — валидация возраста
        (скопировать код из функции `validate_age`).
        4. `validate` — принимает аргумент `data`
        (объект класса `Data`) и сохраняет в список `data_history`. Далее
           запускает методы валидации, описанные выше.

       При этом методы `_validate_name` и `_validate_age` должны брать имя
       и возраст из
       переменной `Validator.data_history` (самое последнее значение).
        А также выбрасывать исключения `ValidationError`
       вместо `Exception`. Если переменная `data_history` пуста,
       тогда выбрасывать исключение `ValueError`.

3. В вашем основном файле, где вся текущая домашка:
    1. В самом верху необходимо импортировать класс `Validator` из модуля
    `validator`.
    2. В самом верху необходимо импортировать класс `ValidationError` из
    модуля `exceptions`.
    3. В функции `main` до цикла создать объект класса.
    Вызвать метод `validate` вместо тех функций валидаций, которые
       были написаны в домашках ранее -
       эти функции необходимо удалить из этого файла. Обрабатывать
       ошибку `ValidationError` вместо `Exception`.
    4. После того как пользователь ввел данные, необходимо создать
    объект класса `DataWithDate` и далее работать только
       с ним.
    5. Теперь количество попыток ввода данных должно выводиться только
    в том случае, если пользователь не смог с первого
       раза ввести верные данные.
    6. После ввода верных данных и до запуска игры необходимо
    показать пользователю:
       1. Общее количество попыток
       2. Время первой попытки, время последней попытки
       3. Сколько времени понадобилось пользователю, чтобы от первой попытки
       дойти к последней (формат HH:MM:SS, где HH
        - часы, MM - минуты, SS - секунды)
"""


from validator import Validator, DataWithDate
from exceptions import ValidationError


def main() -> None:
    """Запуск всех модулей"""

    validator = Validator()
    count_date = []
    count_user_validate = 0
    while True:
        name = input('Введите имя: ')
        try:
            count_user_validate += 1
            age = input('Введите возраст: ')
            date = DataWithDate(name, age)
            count_date.append(date.dt)
            validator.validate(date)

        except ValidationError as e:
            print(e)
            continue

        print(f'Привет {name}, тебе {age} лет.\n', validator.validate(date))
        if count_user_validate > 1:
            print(f'Количетсво попыток проверки:{count_user_validate}.')
        break
    first_try = count_date[0].strftime('%H:%M:%S')
    last_try = count_date[-1].strftime('%H:%M:%S')
    print(f'Общее количество попыток валидации: {count_user_validate}')

    if len(count_date) > 1:
        print(f'Время первой попытки: {first_try}.\n'
              f'Время последней попытки: {last_try} ')
        time_diff = count_date[-1] - count_date[0]
        hours, remainder = divmod(time_diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_diff_str = f"{hours:02}:{minutes:02}:{seconds:02}"
        print(f'Время на прохождение: {time_diff_str}')

    validator.guess_number_game()


if __name__ == '__main__':
    main()
