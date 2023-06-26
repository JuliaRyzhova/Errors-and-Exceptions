def divide(number_1, number_2):
    """Функция деления двух чисел"""
    try:
        result = number_1 / number_2
        print(f'{number_1} divide {number_2} = {result}')
    except ZeroDivisionError:
        print("На ноль делить нельзя")


divide(10, 0)
