"""
Задание 3
Записывает в новый файл все слова в алфавитном порядке из другого файла с текстом. Каждое слово на новой строке.
* (доп.) Рядом со словом укажите сколько раз оно встречалось в тексте

"""

if __name__ == "__main__":
    with open(r'f:\Python lections\Homework_6.txt', encoding='UTF-8', mode='r') as f1:
        s=str()
        for line in f1:
            line=line.replace("\n", " ")
            line=line.replace("\t", " ")
            s=s+line
        for char in s:
            if char in "?.,!:;•()\"\'\\/[]{}😊*“”…_-–#1234567890":
                s=s.replace(char,' ')
        l=s.split()
        l.sort()
        with open(r'F:\Git\Homework\Homework6\temp3.txt', encoding='UTF-8', mode='w') as f2:
            for element in l:
                f2.write(element + ":" + str(l.count(element))+"\n")
                while element in l:
                    l.remove(element)
        with open(r'F:\Git\Homework\Homework6\temp3.txt', encoding='UTF-8', mode='r') as f3:
            print("f2 file is", f3.read(),sep='\n')

    #
    #
    #
    #
    #
