# 4.Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

# Забываем про операции со стоками, идем в пещеру, берем большую дубину и пытаемся что-то выдумать при помощи арифметических операций...
# Тяжко, как решать задачи для пятого класса...
# Это я типа ною, ага :)

num = int(input('Введите число: '))
max_n = 0

while True:
    if num % 10 > max_n:
        max_n = num % 10

    if num // 10 == 0:
        break
    else:
        num = num // 10

print(f'Самая большая цифра в этом числе: {max_n}')
