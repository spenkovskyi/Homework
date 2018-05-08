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
        song = (song + "\n")*(rows-1) + (song + "!" + "\n")
    else:
        song = (song + "\n")*(rows-1) + (song + "." + "\n")
#    print(song)
    return song

if __name__ == "__main__":
    print("Your song is \n", song_generation(rows=5, la=10, end_of_song=1))
