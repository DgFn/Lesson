# Берём уже то, что вы сделали к последнему уроку.
# 0. Обязательно к прочтению Дзен python.
# 1. Создать несколько функций на проверку введённых данных:
# - Проверка имени
# - Проверка возраста Функции должны возвращать строку с ошибкой. Если функции вернули ошибки, нужно вывести
# пользователю ошибки.
# 2. Улучшить проверку имени: в имени между буквами допускается только 1 пробел.
# 3. Сделать совет по получению или замене паспорта (эта задача больше не является со звездочкой) в отдельной функции,
# которая возвращает строку.
# 4. Создать функцию main, в которой будут вызовы всех остальных функций, ввод данных и прочее.
# 5. Создать цикл до тех пор, пока пользователь не введёт верные данные без ошибок.
# 6. Создать функцию, которая очищает введённые данные от лишних пробелов в начале и в конце строки.
# ### Ограничения:
# - Разрешается использовать только два раза print.
# - Нельзя использовать глобальные переменные
# ### Дополнительная информация:
# - Когда вы упакуете весь код в функции и запустите приложение, то у вас не будет запрошено что-то ввести и вывода тоже
# не будет. Рекомендую сначала вам дойти до этого момента, столкнуться с этой проблемой, 10 раз подумать, вспомнить
# прошлый урок.

# Проверка имени
def validation_name(name: str) -> tuple[bool, str]:
    if not name or len(name) < 3:
        return False, 'Ошибка: Недопустимое имя'

# Делаю список по пробелам, если есть лишний пробел вывожу ошибку
    name_array = name.split(' ')
    if '' in name_array:
        return False, 'Ошибка: Большое количество пробелов'

    return True,''

#Удаление пробелов
def validation_split(name: str) -> list[str]:
    name.split()
# Проверка возраста
def validation_age(age: int) -> tuple[bool, str]:
    if age <= 0:
        return False, 'Ошибка: Недопустимый возраст'
    if age < 14:
        return False, "Ошибка: Минимальный возраст 14 лет"
    return True,''
#Совет для паспорта
def validation_id(name: str, age: int) -> str:

    if 16 <= age <= 17:
        return 'Не забудь получить свой первый паспорт!'
    elif 25 <= age <= 26:
        return 'Не забудь заменить паспорт!'
    elif 45 <= age <= 46:
        return 'Не забудь заменить паспорт!'
    return ''



# Запускаем все функции
def main() -> None:
    while True:
        name = input('Введите имя: ')
        age = int(input('Введите возраст: '))
        result_validation_name = validation_name(name)
        result_validation_age = validation_age(age)
        if result_validation_name[0] and result_validation_age[0]:
            result_validation_id = validation_id(name, age)
            print(f'Привет {name}, тебе {age} лет.',result_validation_id)
            break
        else:
            print(result_validation_name[1],result_validation_age[1])



if __name__ == '__main__':
    main()
