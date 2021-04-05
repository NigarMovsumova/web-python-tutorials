# 1. импортирование всего модуля
# import baskets
# 2. импортирование модуля с псевдонимом
# import baskets as bsk
# import numpy as np

# 3. импортирование только того, что юзаем
from baskets import Basket

# 4. импорт всего содержимого -
# bad practise - импортировать можем лишнее + нечитабельно + конфликт имен
# from baskets import *

# print('из app.py модуль app.py виден как ', __name__)

if __name__ == '__main__':
    basket = Basket()
    print(basket)
    print(__name__)
