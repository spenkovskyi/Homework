"""Задание 8
Оформляем в функции наши задания на уроке:

1)	Пишем функцию, которая попросит пользователя ввести слово
(строка без пробелов в середине, а вначале и в конце пробелы могут быть). Пока он не введёт правильно,
просите его ввести. Функция возвращает введённое слово

2)	Пишем функцию, которая попросит ввести число.
Пока он не введёт правильно, просите его ввести. Функция возвращает введённое число.
"""
def enter_string_wo_spaces():
    """
    Function is asking user to enter a word (string without spaces) and return it
    """

    while True:
        row = input("Enter word: \n")
        row = row.strip(" ")
        if " " in row:
            print("Try again")
        else:
            print("Row is ok")
            break

#    print("Method execution finished. result:",row)
    return row


def number(s):
    """
    Function is asking user to enter a number and return it
    """
    while True:
        num = input(s)
        try:
            num = float(num)
        except ValueError:
            print("Try again")
        else:
            return num


if __name__ == "__main__":
    print("Your word is", enter_string_wo_spaces())
    print("Your number is", number("Enter number: \n"))
