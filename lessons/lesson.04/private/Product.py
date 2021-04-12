

class Basket:

    # искажение имени аттрибута _Basket__items
    def __init__(self):
        self.__items = []
        self._discount = 0
        self.name = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, percentage):
        self._discount = percentage

    @property
    def items(self):
        print('def items(self) is called')
        return self.__items

    @items.setter
    def items(self, val):
        self.__iadd__(val)

    @items.getter
    def items(self):
        print('Getter is also called')
        return self.__items

    def __iadd__(self, product):
        self.__items.append(product)
        return self

    def add(self, product):
        self.__items.append(product)

    def set_discount(self, percentage):
        self._discount = percentage

    def get_discount(self):
        return self._discount

    def __len__(self):
        return len(self.__items)

    def __iter__(self):
        return (el for el in self.__items)


basket = Basket()
# print(basket._discount)
# print(basket.__items)
# print(basket.items)
# basket.items = 'val'
# basket.items = 'val1'
# basket.items = 'apple'
# print(basket.items)
# basket.name = 'Test'
# print(basket.name)
# print(basket.items)
basket.set_discount(10)
print(basket.get_discount())
basket.discount = 20
print(basket.discount)
print(basket.get_discount())


# print(vars(getattribute))
# print(getattribute.__items)
# print(basket._discount)
