# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
from functools import reduce

with open("text.txt", 'r', encoding='UTF-8') as f:
    staff = [line.split() for line in f]

salary = [float(el[1]) for el in staff]
result = reduce(lambda a, b: a + b, salary) / len(salary)
print("Средняя величина дохода сотрудников", result)
min_staff = [el[0] for el in staff if float(el[1]) < 20000]
# Можно было бы сделать вывод эстетичным, но у меня температура и не думается совсем... прошу прощения
print("Оклад менее 20 тыс. у следующих сотрудников:", min_staff)
