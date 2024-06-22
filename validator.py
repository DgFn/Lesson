import random
from datetime import datetime
from exceptions import ValidationError


class Data:
    """Класс инициализации данных"""
    def __init__(self, name: str, age: str):
        self.name = name
        self.age = age
        self._clear_whitespaces()
        if not self.age.isdigit():
            raise ValidationError('Возраст не может быть строкой')
        self.age = int(self.age)

    def _clear_whitespaces(self):
        self.name = self.name.strip()
        self.age = self.age.strip()


class DataWithDate(Data):
    """Дочка класса Data

    Дополнительно запоминает время валидации
    """
    dt: datetime

    def __init__(self, name: str, age: str):
        self.dt = datetime.now()
        super().__init__(name, age)


class Validator:
    """Класс валидация данных"""
    def __init__(self):
        self.data_history: list[Data] = []

    def validate(self, data: Data) -> str:
        self.data_history.append(data)

        if not self.data_history:
            raise ValueError('Нужно ввести данные')

        self._validate_name(self.data_history[-1].name)
        self._validate_age(self.data_history[-1].age)
        return self.get_passport_advicce(self.data_history[-1].age)

    def _validate_name(self, name: str) -> str | None:
        """ Проверка имени
        :param name: имя введеное пользователем
        :raise: возращает ошибки, если проверка не прошла
        :return возвращает None если проверки прошли
        """
        if not name or len(name) < 3:
            raise ValidationError('Ошибка: Недопустимое имя')

        name_array = name.split(' ')

        if '' in name_array:
            raise ValidationError('Ошибка: Большое количество пробелов')

        return None

    def _validate_age(self, age: int) -> str | None:
        """Проверка возраст
            :param age: возраст введенный пользователем
            :raise: возращает ошибки, если проверка не прошла
            :return: возвращает None если проверки прошли
            """
        if age <= 0:
            raise ValidationError('Ошибка: Недопустимый возраст')
        if age < 14:
            raise ValidationError("Ошибка: Минимальный возраст 14 лет")
        return None

    def get_passport_advicce(self, age: int) -> str:
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

    def guess_number_game(self) -> None:
        """Функция игра, угадай число"""

        hidden_number = random.randint(1, 5)
        count_user = 0
        while True:
            number_user = int(input('Попробуй угадать  число: '))
            if number_user == hidden_number:
                print(f'Вы угадали с {count_user + 1} попытки ')
                break
            count_user += 1
