import random
# Если необходимо, исправьте данный код 
# (задание 2 https://docs.google.com/document/d/17EaA1lDxzD5YigQ5OAal60fOFKVoCbEJqooB9XfhT7w/edit)


def generate_list():
    """Функция генерирующая список рандомных целых чисел"""
    result = random.sample(range(1, 50), 10)
    print("Random number list is :")
    print(result)
    return result

def divide(my_list, divider):
    try:
        print(my_list[8] / divider)
    except IndexError:
        print("Исключение IndexError, индекс списка вне диапазона.")
    except ZeroDivisionError:
        print("На ноль делить нельзя")


lst = generate_list()
divide(lst, 0)




