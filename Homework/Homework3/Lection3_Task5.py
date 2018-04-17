"""Задание 5
Создайте строку, в которой написан, какой-то текст. Пример:
We are not what we should be!
We are not what we need to be.
But at least we are not what we used to be
 (Football Coach)
•	Посчитайте сколько слов в тексте (разбейте на слова методом строк split)
•	Удалите знаки препинания (пройдитесь циклом все слова и удалите методом strip знаки препинания)
•	Выведите слова в алфавитном порядке (найдите метод списка, который сортирует)
Усложнённое ** (можно сначала его не делать):
•	Посчитать, сколько раз встречается каждое слово.
(Подсказка: создавать словарь, где ключи — это слова из текста, а в значениях подсчитываем количество «встречаний» этого слова)
"""

s = "You cannot help people permanently by doing for them, \nwhat they could and should do for themselves. \n\t\t\t\t\t\t\t(Abraham Lincoln)"

print(s)
l = s.split()
print(l)
print(len(l))
#l1=list()
for i in range(len(l)):
    l[i] = l[i].strip(".,()")
print(l)
l.sort()
print(l)
d=dict()
for i in range(len(l)):
    d.update({l[i] : l.count(l[i])})
print(d)
