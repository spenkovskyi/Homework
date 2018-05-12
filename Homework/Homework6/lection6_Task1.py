"""Задание 1 (Обязательное всем!!!!)
Тестовое приложение с REST API http://pulse-rest-testing.herokuapp.com/
Создаём один скрипт:
•	Создаёт персонажа POST /roles/, вы запоминаете его id.
•	Проверяете, что он создался и доступен по ссылке GET /roles/[id]
•	Проверяете, что он есть в списке пользователей по GET /roles/
•	Изменяете этого пользователя методом PUT roles/[id]/
•	Проверяете, что он изменился и доступен по ссылке /roles/[id]
•	Проверяете, что он есть в списке пользователей по GET /roles/ с новой инфой
•	Удаляете этого пользователя методом DELETE roles/[id]
Второй скрипт: тоже самое с книгами
** Попробуйте воспользоваться http.client вместо requests. Ощутите разницу 😊

"""

import requests
class personage:
    def __init__(self, pers_attr):
        self.attr = pers_attr

    def create_pers(self, base_url):
        self.resp = requests.post(base_url, data=self.attr)
        self.resp = self.resp.json()
        return self.resp

    def exist_in_roles(self, base_url):
        r = requests.get(base_url + str(self.resp['id']))
        if r.status_code == 200:
            return True
        else:
            return False

    def pers_really_exist(self, base_url):
        if self.resp in requests.get(base_url).json():
            return True
        else:
            return False

    def upd_pers(self, base_url, updated_pers_attr):
        self.attr = updated_pers_attr
        self.resp = requests.put(base_url + str(self.resp['id']),data=self.attr)
        self.resp = self.resp.json()
        return self.resp

    def delete_pers(self, base_url):
        resp_delete = requests.delete(base_url + str(self.resp['id']))
        if resp_delete.status_code == 204:
            return True
        else:
            return False


if __name__ == "__main__":
    base_url_roles = "http://pulse-rest-testing.herokuapp.com/roles/"
    pers_dict = {"name": "Vasisualy Pupipkov", "type": "an hero", "level": 12, "book": 5}
    role = personage(pers_dict)
    role.create_pers(base_url_roles)
    if role.exist_in_roles(base_url_roles):
        print("Success. ID exist")
    else:
        print("Fail. ID does not exist")
    if role.pers_really_exist(base_url_roles):
        print("Personage really exist")
    else:
        print("Personage doesn't exist")
    upd_pers_dict = {"name": "Vaska Pupkov", "type": "an real hero", "level": 14, "book": 10}
    role.upd_pers(base_url_roles,upd_pers_dict)
    if role.exist_in_roles(base_url_roles):
        print("Success. Updated ID exist")
    else:
        print("Fail. Upgated ID does not exist")
    if role.pers_really_exist(base_url_roles):
        print("Personage really updated")
    else:
        print("Personage doesn't updated")
    if role.delete_pers(base_url_roles): print("ID deleted")
    if role.exist_in_roles(base_url_roles):
        print("Success. ID exist")
    else:
        print("Fail. ID does not exist")
    if role.pers_really_exist(base_url_roles):
        print("Personage really exist")
    else:
        print("Personage doesn't exist")
    base_url_books = "http://pulse-rest-testing.herokuapp.com/books/"
    book_dict = {"title": "Vasisualy Pupipkov journey", "author": "Vasisualy Pupipkov"}
    book = personage(book_dict)
    book.create_pers(base_url_books)
    if book.exist_in_roles(base_url_books):
        print("Success. Book exist")
    else:
        print("Fail. Book does not exist")
    if book.pers_really_exist(base_url_books):
        print("Book really exist")
    else:
        print("Book doesn't exist")
    upd_book_dict = {"title": "Vaselina Pup4ikova around the world", "author": "Vaselina Pup4ikova"}
    book.upd_pers(base_url_books,upd_book_dict)
    if book.exist_in_roles(base_url_books):
        print("Success. Updated book exist")
    else:
        print("Fail. Upgated book does not exist")
    if book.pers_really_exist(base_url_books):
        print("Book really updated")
    else:
        print("Book doesn't updated")
    # if book.delete_pers(base_url_roles): print("Book deleted")
    if book.exist_in_roles(base_url_books):
        print("Success. Book exist")
    else:
        print("Fail. Book does not exist")
    if role.pers_really_exist(base_url_books):
        print("Book really exist")
    else:
        print("Book doesn't exist")