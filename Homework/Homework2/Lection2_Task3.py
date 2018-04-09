"""Задание 3
Пользователь вводит целое число.
Требуется определить, является ли год с данным номером високосным.
Если год является високосным, то выведите YES, иначе выведите NO.
Напомним, что в соответствии с григорианским календарем, год является високосным,
если его номер кратен 4, но не кратен 100, а также если он кратен 400."""


y = input("Print year \n")
try:
    y = int(y)
except ValueError:
    print("Year must be integer")
else:
#print(type(y) == int)
    #print((y % 4) == 0, (y % 100) == 0, (y % 400) == 0)
    if (y % 4) == 0:
        if (y % 100) == 0:
            if (y % 400) == 0:
                print(y,"is a leap year")
            else:
                print(y,"is not a leap year")
        else:
            print(y,"is a leap year")
    else:
        print(y,"is not a leap year")