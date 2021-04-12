# У каждого может быть свой метод __init__() или square()
# или какой-нибудь другой. Какой именно из методов square() вызывается,
# и что он делает, зависит от принадлежности объекта к тому или иному классу.
# https://younglinux.info/oopython/polymorphism


class SumCounter:
    def __init__(self):
        self.n = 10

    def total(self, a):
        return self.n + int(a)


class LengthCounter:
    def __init__(self):
        self.string = 'Hi'

    def total(self, a):
        return len(self.string + str(a))


sum_counter = SumCounter()
length_counter = LengthCounter()

print(sum_counter.total(35))  # Вывод: 45
print(length_counter.total(35))  # Вывод: 4
