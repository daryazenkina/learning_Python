#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

#первый вариант
def person_v1 (**kwargs):
    """
    сприменением kwargs
    принимает значения описывающие пользователя и выводит их встроку
    (kwargs)
    """
    for key,el in kwargs.items():
        print(f'{key}:{el} ',end='')

#Второй вариант
def person_v2(p_name, p_lastname ,year, city, mail , phone):
    """
    топором
    принимает значения описывающие пользователя и выводит их встроку
    (p_name: str,p_lastname str ,year int, city str, mail  str, phone str)
    """
    print(f'имя:{p_name} фамилия:{p_lastname} год рождения:{year} город проживания:{city} email:{mail} телефон:{phone}')

person_dict={
    'имя':"hgff",
    'фамилия':"ffff",
    'год рождения':1983,
    'город проживания':'fffff',
    'email':'ydydyd',
    'телефон':'345667899'
}

#Вызов второго варианта
person_v2(year=1983,p_name="hgff",p_lastname="ffff", city='fffff', phone='345667899',mail='ydydyd')
#Вызов первого варианта
person_v1(**person_dict)