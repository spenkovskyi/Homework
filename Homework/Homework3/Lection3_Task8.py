"""Задание 8
Оформляем в функции наши задания на уроке:

1)	Пишем функцию, которая попросит пользователя ввести слово
(строка без пробелов в середине, а вначале и в конце пробелы могут быть). Пока он не введёт правильно,
просите его ввести. Функция возвращает введённое слово

2)	Пишем функцию, которая попросит ввести число.
Пока он не введёт правильно, просите его ввести. Функция возвращает введённое число.
"""
def row():
    while True:
        row = input("Enter word: \n")
        row = row.strip(" ")
        try:
            row.index(" ", 0, len(row))
        except ValueError:
            print("Row is ok")
            break
        else:
            print("Try again")
#    print("Method execution finished. result:",row)
    return row
print("Your word is", row())


def number():
    while True:
        num = input("Enter number: \n")
        try:
            num = float(num)
        except ValueError:
            print("Try again")
        else:
            return num
print("Your number is", number())
