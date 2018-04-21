"""Задание 2
Пишем функцию, которая выводит второе по возрастанию значение из переданных аргументов.
Учитываем, что может быть повторяющиеся значения аргументов.
"""

def second_value(*args):
#    print(args)
    l=list(args)
    l.sort()
    d=dict()
    for i in range(len(l)):
        d.update({l[i] : l.count(l[i])})
#        print(d)
    l=list(d.keys())
#    print("keys in dict", l)
#    print(type(l))
    return l[1]


print("2nd argument is", second_value(5,5,5,8,2,7,2,2,3,2))

