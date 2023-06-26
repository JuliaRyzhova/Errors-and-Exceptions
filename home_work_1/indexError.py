import random


def generate_list():
    """Функция генерирующая список рандомных целых чисел"""
    result = random.sample(range(1, 50), 10)
    print("Random number list is :")
    print(result)
    return result


def show_item_by_index(input_list):
    """ Функция выводящая в консоль элемент по индексу"""
    try:
        print(input_list[100])
    except IndexError:
        print("Исключение IndexError, индекс списка вне диапазона.")
    else:
        print("Успех, нет ошибок!")


lst = generate_list()
show_item_by_index(lst)
