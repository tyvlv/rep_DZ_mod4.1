class Item:
    """Класс товара в магазине электроники"""
    pay_rate = 1
    all = []

    def __init__(self, name: str, price: float, amount: float):
        self.name = name
        self.price = price
        self.amount = amount
        self.all.append(self)

    def calculate_total_price(self) -> float:
        """Возвращает общую стоимость конкретного товара"""
        return self.price * self.amount

    def apply_discount(self) -> None:
        """Применяет установленную скидку на конкретный товар"""
        self.price = self.price * Item.pay_rate
