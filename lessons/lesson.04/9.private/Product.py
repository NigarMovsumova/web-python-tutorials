

class Basket:

    # искажение имени аттрибута _Basket__items
    def __init__(self):
        self.__items = []
        self._discount = 0

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, val):
        self.__iadd__(val)

    def __iadd__(self, product):
        self.__items.append(product)
        return self

    def add(self, product):
        self.__items.append(product)

    def __len__(self):
        return len(self.__items)

    def __iter__(self):
        return (el for el in self.__items)


basket = Basket()
print(basket._discount)
print(basket.__items)

# print(vars(getattribute))
# print(getattribute.__items)
print(basket._discount)
