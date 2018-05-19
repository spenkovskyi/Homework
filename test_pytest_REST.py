import requests

def test_create_book_positive(base_url, book):
    response = requests.post(base_url + "books/", data=book)
    assert response.status_code == 201
    body = response.json()
    # self.asserDictContainsSubset(book, response.json(), )
    body["id"] = body["id"]
    for key in book:
        assert book[key].strip() == body[key]
    # TODO GET запросы
    r = requests.get(base_url + 'books/' + str(body["id"]))
    print(r.url)
    assert r.status_code == 200
