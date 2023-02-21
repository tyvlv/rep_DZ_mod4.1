from classes import Item


def main():
    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон'
    print(item._Item__name)
    print(item.name)
    print(item.__dict__)

    item.name = 'СуперСмарт'
    print(item.name)

    Item.instantiate_from_csv()  # создание объектов из данных файла
    print(len(Item.all))  # в файле 5 записей с данными по товарам

    item1 = Item.all[2]
    print(item1.price)
    print(type(item1.price))

    print(Item.is_integer(5))
    print(Item.is_integer(5.0))
    print(Item.is_integer(5.5))


if __name__ == "__main__":
    main()
