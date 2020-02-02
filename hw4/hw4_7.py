# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fibo_gen().
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.


from functools import reduce

#на странице очень не понятно написаны условия, задачи. Скрестила с условиями из методички. Надеюсь поняла правильно.
def fibo_gen(n):
    for el in range(1,n+1):
        #Велено выводить первые 15 чисел
        if el>15:
            break
        yield reduce(lambda a,b: a*b,range(1,el+1))

g = fibo_gen(16)
print(g)

for el in fibo_gen(16):
    print(el)