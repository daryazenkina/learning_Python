#4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def my_func_muly(x, y):
    """
       возводит x в степень y не используя возведение в степень (простой алгоритм с умножением)
       (int,int)->float
    """
    if y>=0 or x<0:
        print('Плохие входные параметры')
        return

    result=1
    for num in range(abs(y)):
        result=result*x

    result=1/result

    return result

def my_multy (i:int,n:int):
    """
    умножение без оператора умножения
    (int)->int
    """
    result=0
    for num in range(n):
        result+=i

    return result

def my_func(x, y):
    """
    возводит x в степень y не используя возведение в степень (дихотомический алгоритм) (сложнее я не придумала)
    (int,int)->float
    """
    if y >= 0 or x < 0:
        print('Плохие входные параметры')
        return

    multiplier=1
    degree=abs(y)
    num=abs(x)
    result=0
    while True:
        if degree==0:
            break

        if degree%2!=0:
            multiplier=my_multy(multiplier,num)

        if degree>2:
            num=my_multy(num,num)
            degree=degree//2
        else:
            num = my_multy(num, num)
            result=my_multy(num,multiplier)
            break

    result=1/result
    return result

print(my_func_muly(3,-19))
print(my_func(3,-19))