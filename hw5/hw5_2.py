# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк,
# количества слов в каждой строке.

with open("temp.txt", 'a', encoding='UTF-8') as f:
    f.write('один' + '\n')
    f.write('вторая строка' + '\n')
    f.write('это третья строка' + '\n')

# Топорный вариант перебора файла построчно, вариант который мне кажется интереснее в следующей задаче
count_line = 0
with open("temp.txt", 'r', encoding='UTF-8') as f:
    for line in f:
        count_line += 1
        str_list = line.split()
        print(f"Слов в строке №{count_line}: {len(str_list)}")

print("Всего строк в файле: ", count_line)
