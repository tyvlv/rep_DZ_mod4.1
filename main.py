from classes import Item, Phone, Keyboard


def main():
    # item = Item('Телефон', 10000, 4)
    #
    # print(item)
    #
    # phone1 = Phone("iPhone 14", 120_000, 5, 2)
    # print(phone1)
    # print(repr(phone1))
    # phone1.number_of_sim = 3
    #
    # print(repr(phone1))
    #
    # kb = Keyboard('Dark Project KD87A', 9600, 5)
    # print(kb)
    # print(kb.language)
    # kb.change_lang()
    # print(kb.language)
    # kb.change_lang()
    # print(kb.language)
    Item.instantiate_from_csv()

    for i in Item.all:
        print(repr(i))


if __name__ == "__main__":
    main()
