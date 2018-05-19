import pytest

@pytest.fixture
def fixt1():
    print("\nInitialization of fixture")
    fixture = "I am a fixture"
    yield fixture
    print("\nDestroying of fixture")