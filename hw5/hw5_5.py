# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from functools import reduce

num_in = '1 2 3 4 5 6 7 8 8 8 9 100'

# не нашла можно ли сделать в одном with open?
# Режим r+ не работает когда фаил не создан, w+ считывает только пустую строку

with open("text_num.txt", 'w') as f:
    f.write(num_in)

with open("text_num.txt", 'r') as f:
    num_out = f.read().split()

print(reduce(lambda a, b: int(a) + int(b), num_out))
