# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

num = []
with open("text1.txt", 'r', encoding='UTF-8') as f:
    for line in f:
        print(line.replace('One', 'Один').replace('Two', 'Два').replace('Three', 'Три').replace('Four', 'Четыре'))
        num.append(line.replace('One', 'Один').replace('Two', 'Два').replace('Three', 'Три').replace('Four', 'Четыре'))

with open("text_new.txt", 'w', encoding='UTF-8') as f:
    for el in num:
        #Текст в файле скопировался сразу с \n так что в данном конкретном случее добавлять его не надо
        f.write(el)
