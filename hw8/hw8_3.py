# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


num_list = []

while True:
    inp_data = input("Введите следующее число, для прекращения ввода введите stop: ")
    if inp_data == "stop":
        break

    try:
        el = int(inp_data)
    except ValueError:
        print(OwnError("Вы что-то не то ввели"))
    else:
        num_list.append(el)

print(num_list)
