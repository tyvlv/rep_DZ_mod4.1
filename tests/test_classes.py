from classes import Item


def test_class_item(item1, item2):
    """Тестирование класса Item"""
    assert len(Item.all) == 2
    assert item1.calculate_total_price() == 200_000
    Item.pay_rate = 0.8
    item2.apply_discount()
    assert item2.price == 16_000

