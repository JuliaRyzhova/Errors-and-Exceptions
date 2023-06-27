# Реализуйте метод, который запрашивает у пользователя ввод дробного числа (типа float), и возвращает введенное значение. 
# Ввод текста вместо числа не должно приводить к падению приложения, 
# вместо этого, необходимо повторно запросить у пользователя ввод данных.

def user_input_float():
    while True:
        number = input('Input any float number: ')
        try:
            return float(number)
        except ValueError:
            print('Incorrect input data. Try again!')


print(user_input_float())
