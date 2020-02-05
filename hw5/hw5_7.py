#7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл,
# вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
import json

num=0
count=0
with open("text_firm.txt", 'r', encoding='UTF-8') as f:
    for line in f:
        print(f'{line.split()[1]}"{line.split()[0]}" выручка {line.split()[2]} убыток {line.split()[3]}')
        #только в случае прибыли
        if int(line.split()[2])-int(line.split()[3])>0:
            num+=int(line.split()[2])-int(line.split()[3])
            count+=1

with open("text_firm.txt", 'r', encoding='UTF-8') as f:
    firm_dict = {line.split()[0]: int(line.split()[2])-int(line.split()[3]) for line in f}

average=dict(average=num/count)
json_str = json.dumps([firm_dict,average])
print(json_str)