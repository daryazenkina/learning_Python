#1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_str=input("введите что-нибудь, для выхода не вводите ничего, просто нажмите Enter: ")

with open("text_1.txt",'w',encoding='UTF-8') as f:
     while my_str!='':
         f.write(my_str + '\n')
         my_str=input("введите что-нибудь, для выхода не вводите ничего, просто нажмите Enter: ")