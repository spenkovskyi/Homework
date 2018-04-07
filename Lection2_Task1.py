"""Task #1. Задание 1.
(Подсказка: ищите как это сделать с помощью методов строк)
1. Определите является ли строка записью числа. (Подсказка: ищите как это
сделать с помощью методов строк)
2. Посчитайте сколько у вас пробелов в строке.
3. Посчитайте сколько у вас символов точки &#39;.&#39; в строке.
4. Создайте строку &quot;Homework&quot;. Преобразуйте ее в строку длиной 100 символов,
посередине которой исходное слово, а с обоих сторон строка заполнена пробелами.
Выведите ее на экран.
5. Сделайте первые буквы слов строки большими (upper case)."""
#1
#s = input("Enter string \n")
s='123'
print(s)
if s.isdigit()==True:
    print("string is digital")
else:
    print("string is not digital")
#2
l = """Please count quantity of spaces in this string. And dots..."""
print(l)
print("Your string has", l.count(" "), "spaces")
#3
print("Your string has", l.count("."), "dots")
#4
r = "Homework"
r = r.ljust(50, " ")
print("String length is", len(r), ". Quantity of spaces is", r.count(" "),"String is")
print(r)
r = r.rjust(100, " ")
print("String length is", len(r), "Quantity of spaces is", r.count(" "),"String is")
print(r)
#5
print("String with capital first letters:", l.title())

