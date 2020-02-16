# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def data_to_int(cls, data):
        day, month, year = map(int, data.split('-'))
        return cls(day, month, year)

    @staticmethod
    def data_valid(data):
        day, month, year = map(int, data.split('-'))
        return day <= 31 and day > 0 and month <= 12 and month > 0


d = Data.data_to_int('23-02-1934')
print(d.day, d.month, d.year)
print(Data.data_valid('23-02-1934'))
