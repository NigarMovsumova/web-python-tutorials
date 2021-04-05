from core import is_even

if __name__ == '__main__':

    # num = int(input('Введите число для проверки на чётность:'))
    # print(is_even(num))
    search_engine_choice = int(input('''
    1. Google
    2. Yandex
    3. Bing
    Choose your search engine:
    '''))
    if search_engine_choice == 1:
        print('Google')
    elif search_engine_choice == 2:
        print('Yandex')
    elif search_engine_choice == 3:
        print('Bing')
    else:
        print('Wrong choice')
