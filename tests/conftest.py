import pytest
from classes import Item, Phone, Keyboard


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def item2():
    return Item("Ноутбук", 20000, 5)


@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120_000, 5, 2)


@pytest.fixture
def kb():
    return Keyboard('Dark Project KD87A', 9600, 5)
