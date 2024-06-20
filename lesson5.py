"""Домашка:

Сделать функцию is_palindrome, которая определяет является ли строка палиндромом или нет.
При этом введено может быть как слово, так и целые предложения с пробелами и с различными знаками препинания.
Необходимо избегать всех символов кроме букв.
А также не копировать входящие данные (например, развернуть строку через срез — это скопировать входящие данные)
"""


def is_palindrome(word: str) -> bool:
    """Функиця проверяет является ли слово палиндромом

    :param word: принимает ввод строки от пользователя
    :return возвращает булевое значение взасимости от слова
    """
    i = 0
    j = len(word) - 1

    while i <= j:
        if not word[i].isalpha():
            i += 1
            continue

        if not word[j].isalpha():
            j -= 1
            continue

        if word[i].lower() != word[j].lower():
            return False
        i += 1
        j -= 1

    return True


while True:
    palindrome_word = input('Entry any word: ')
    print(is_palindrome(palindrome_word))