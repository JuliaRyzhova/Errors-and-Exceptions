# Разработайте программу, которая выбросит Exception, когда пользователь вводит пустую строку.
# Пользователю должно показаться сообщение, что пустые строки вводить нельзя!!!

def user_input():
    while True:
        text = input('Input something: ')
        try:
            text = text.strip()
            check_empty = text[0]
            print('Ok! This is correct data!')
            return text
        except IndexError:
            print('You cannot enter empty lines!')


user_input()
