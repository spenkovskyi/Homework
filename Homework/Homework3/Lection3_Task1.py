"""
Задание 1
Входные данные
Пользователь вводит строку. Выловите исключения, если введённая строка слишком короткая.
Выходные данные
Воспользуйтесь одним print(), но при этом выводите с новой строки:
•	Сначала выведите третий символ этой строки.
•	Во второй строке выведите предпоследний символ этой строки.
•	В третьей строке выведите первые пять символов этой строки.
•	В четвертой строке выведите всю строку, кроме последних двух символов.
•	В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы выводятся, начиная с первого).
•	В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
•	В седьмой строке выведите все символы в обратном порядке.
•	В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
•	В девятой строке выведите все символы в обратном порядке без первого и последнего элемента.
•	В десятой строке выведите длину данной строки.
"""


try:
    s = input("Enter string \n")
except EOFError:
    print("String is too small")
#s ="Hi there! Are you ok?"
#print(s)
print(s[2:3], s[-2:-1], s[:5], s[:-2], s[::2], s[1::2], s[len(s)::-1], s[(len(s)-2):0:-1], len(s), sep='\n')