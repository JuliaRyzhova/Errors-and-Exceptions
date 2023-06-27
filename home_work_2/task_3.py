# Дан следующий код, исправьте его там, где требуется
# (задание 3 https://docs.google.com/document/d/17EaA1lDxzD5YigQ5OAal60fOFKVoCbEJqooB9XfhT7w/edit)

def main():
    a = 90
    b = 3
    abc = [1, 2]
    try:
        print(a / b)
        print_sum(23, 'dva')
        abc[3] = 9
    except ValueError:
        print('Некорректные входные данные для сложения чисел.')
    except TypeError:
        print('Некорректные входные данные для деления чисел.')
    except IndexError:
        print('Исключение IndexError, индекс списка вне диапазона.')


def print_sum(c, d):
    if isinstance(c, (float, int)) and isinstance(d, (float, int)):
        print(c + d)
    else:
        raise ValueError


main()
