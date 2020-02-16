# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Warehouse:
    def __init__(self, name):
        self.name = name


class OfficeEquipment:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price


class Printer(OfficeEquipment):
    def __init__(self, name, size, price, color):
        super().__init__(name, size, price)
        self.color = color


class Scanner(OfficeEquipment):
    def __init__(self, name, size, price, paper_size):
        super().__init__(name, size, price)
        self.paper_size = paper_size


class Xerox(OfficeEquipment):
    def __init__(self, name, size, price, speed):
        super().__init__(name, size, price)
        self.speed = speed


p = Printer('Принтер', "30Х30Х60", 23000, True)
s = Scanner('Сканер', "40Х40Х40", 15000, "А4")
x = Xerox('Ксерокс', "20Х20Х20", 30000, 40)

w = Warehouse("Склад 1")
