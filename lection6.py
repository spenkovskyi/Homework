"""
Задание 1. Со значениями по умолчанию
Пишем функцию, которая генерирует песню la-la-la. Функция принимает 3 аргумента:

1-е число – сколько строк будет в песне. По умолчанию 3
2-е число – сколько «la» будет в строке («la» в строке объединяются дефисом). По умолчанию 3
3-е число – если 0, то в конце стоит точка, если 1, то в конце стоит «!». По умолчанию 0
"""




def song_generation(rows=3, la=3, end_of_song = 0):
    """
    Function will generate the best song you've ever heard
    """
    song = "la-"*la
    song = song.strip("-")
    if end_of_song:
        song = (song + "!" + "\n")*rows
    else:
        song = (song + "." + "\n")*rows
#    print(song)
    return song

if __name__ == "__main__":
    import urllib.request
    import requests

    r = requests.get('http://google.com')
    print(r.content)
    f = open("google_from_requests.html", "w")
    f.write(str(r.content))
    f.close()

    # content = urllib.request.urlopen("http://google.com").read()
    #
    # f = open("google.html", "w")
    # f.write(str(content))
    # f.close()
    # print(type(content), content)


    # print("Your song is \n", song_generation(rows=5, la=10, end_of_song=1))
    # try:
    #     f = open("temp.txt", "a")
    #     f.write(song_generation(rows=5, la=10, end_of_song=1))
    #     print("File temp.txt was updated")
    #     f.close()
    # except:
    #     pass
    # finally:
    #     f.close()
    # f = open("temp.txt", "r")
    # f.
    # for line in f:
    #     print(line.strip("\n")+"!")
    # f.close()

    # f1 = open(r'D:\SPenkovskyi\Homework\Lection5.py', 'r')
    # print(f1.read())
    # f1.close()
    #
