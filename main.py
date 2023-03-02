from classes import Item, Phone


def main():
    item = Item('Телефон', 10000, 4)

    print(item)

    phone1 = Phone("iPhone 14", 120_000, 5, 1)
    print(phone1)
    print(repr(phone1))
    phone1.number_of_sim = 3

    print(repr(phone1))


if __name__ == "__main__":
    main()
