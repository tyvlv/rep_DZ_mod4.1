import pytest
from classes import Item


def test_instantiate_from_csv():
    """Тест метода создания экземпляров класса из csv-файла"""
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_is_integer():
    """Тест метода проверки целого числа"""
    assert Item.is_integer(5) is True
    assert Item.is_integer(4.0) is True
    assert Item.is_integer(3.3) is False


def test_name(item1):
    """Тест превышения длины наименования товара"""
    item1.name = "Телефон"
    assert item1.name == "Телефон"
    with pytest.raises(ValueError):
        item1.name = "Калькулятор"


def test_calculate_total_price(item1):
    """Тест метода расчета общей стоимости всего количества товара"""
    assert item1.calculate_total_price() == 200_000


def test_apply_discount(item2):
    """Тест метода применения скидки на товар"""
    Item.pay_rate = 0.8
    item2.apply_discount()
    assert item2.price == 16_000
