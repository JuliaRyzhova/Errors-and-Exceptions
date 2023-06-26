def read_file():
    """Функция считывания файла из папки"""
    try:
        with open('home_work_1/description_hw_1.txt', encoding='utf-8') as file:
            data = file.readlines()
            for line in data:
                print(line)
    except FileNotFoundError:
        print("Невозможно открыть файл")
    else:
        print()
        print("Это и есть весь ваш файл!")


read_file()
