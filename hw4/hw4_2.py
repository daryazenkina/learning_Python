# 2. Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.

my_list = [10, 25, 12, 13, 30, 45, 50]
print(my_list)
new_list = [el for ind, el in enumerate(my_list[::]) if el > my_list[ind - 1]]
print(new_list)
