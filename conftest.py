import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    return "http://pulse-rest-testing.herokuapp.com/"

@pytest.fixture()
def book(base_url):
    book= {"title": "sdgfs", "author": "sdfds"}
    yield book
    if "id" in book.keys():
        requests.delete(base_url + "books/" + str(book["id"]))