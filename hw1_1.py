# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

question = 'Введите число: '
num_1 = int(input(question))

question = 'Введите строку: '
str_1 = input(question)

str_2 = input("Введите вопрос: ")

num_2 = int(input("И еще одно число: "))

num_3 = 42

print(f'''Сумма ваших чисел {num_1 + num_2}
Ответ на ваш вопрос {num_3}
«{str_1}»: это все что Вы хотели поэтому поводу сказать?''')
