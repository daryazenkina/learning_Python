#5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def list_sum(int_list):
    """
    сумирует числа из списка до символа выхода
    (list)->int
    """
    result=0
    for el in int_list[0:int_list.index('q') if 'q' in my_list else len(int_list)]:
        result+=int(el)
    return result

num=0
while True:
    my_list=input('введите числа разделенные пробелом, для выхода нажмите q ').split()
    num+=list_sum(my_list)
    print("сумма вновь введенных чисел:",list_sum(my_list))
    print("общая сумма",num)
    if 'q' in my_list:
        print('До новых встреч')
        break