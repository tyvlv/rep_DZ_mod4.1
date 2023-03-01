import pytest
from classes import Item, Phone


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def item2():
    return Item("Ноутбук", 20000, 5)

@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120_000, 5, 2)
