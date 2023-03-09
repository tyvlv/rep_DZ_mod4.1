import csv


class Item:
    """Класс товара в магазине электроники"""
    pay_rate = 1
    all = []

    def __init__(self, name: str, price: float, amount: float):
        self.__name = name
        self.price = price
        self.amount = amount
        self.all.append(self)

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.__name}", {self.price}, {self.amount})'

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Второе слагаемое должно быть класса Item или дочернего')
        return self.amount + other.amount

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """Создаёт новые экземпляры из csv-файла"""
        with open('items.csv', 'r', encoding="windows-1251") as file:
            reader = csv.DictReader(file)
            for column in reader:
                if cls.is_integer(column['price']):
                    price = int(float(column['price']))
                else:
                    price = float(column['price'])
                if cls.is_integer(column['quantity']):
                    amount = int(float(column['quantity']))
                else:
                    amount = float(column['quantity'])
                cls(column['name'], price, amount)

    @staticmethod
    def is_integer(data) -> bool:
        """Возвращает True, если число целое"""
        if float(data).is_integer():
            return True
        return False

    @property
    def name(self) -> str:
        """Возвращает наименование товара"""
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """Контролирует превышение длины наименования товара"""
        if len(name) < 11:
            self.__name = name
        else:
            raise ValueError('Длина наименования товара превышает 10 символов.')

    def calculate_total_price(self) -> float:
        """Возвращает общую стоимость всего количества конкретного товара"""
        return self.price * self.amount

    def apply_discount(self) -> None:
        """Применяет установленную скидку на конкретный товар"""
        self.price = self.price * Item.pay_rate


class Phone(Item):
    """Класс товара - Телефон"""

    def __init__(self, name: str, price: float, amount: float, number_of_sim: int):
        super().__init__(name, price, amount)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}", {self.price}, {self.amount}, {self.number_of_sim})'

    @property
    def number_of_sim(self) -> int:
        """Возвращает количество sim-карт, поддерживаемых телефоном"""
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim: int) -> None:
        """Контролирует, что количество sim-карт, поддерживаемых телефоном, больше нуля"""
        if number_of_sim > 0 and type(number_of_sim) is int:
            self._number_of_sim = number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')


class MixinLang:
    """Миксин - раскладка клавиатуры"""

    def __init__(self, *args):
        self.__language = 'EN'
        super().__init__(*args)

    @property
    def language(self) -> str:
        """Возвращает текущую раскладку клавиатуры"""
        return self.__language

    def change_lang(self) -> None:
        """Меняет раскладку клавиатуры"""
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'


class Keyboard(MixinLang, Item):
    """Класс товара - Клавиатура"""
    pass
