

class Basket:

    def __init__(self):
        self._items = []
        # -> _attr - protected - снаружи трогать нельзя
        # self.items = []

    def __iadd__(self, product):
        self._items.append(product)
        return self

    def add(self, product):
        self._items.append(product)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        # --> должен возвращать iterable
        return (el for el in self._items)


basket = Basket()
basket._items.append('nokia')
basket.add('nokia')
print('nokia' in basket)
print(basket._items)
print(len(basket))
