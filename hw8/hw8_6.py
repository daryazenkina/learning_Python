# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    def __init__(self, name):
        self.name = name
        self.place = []

    def add_office_equipment(self, office_equipment):
        self.place.append(office_equipment)

    def transfer_to(self, office_equipment, office_name):
        try:
            self.place.remove(office_equipment)
            print(f"Техника {office_equipment} передана в подразделение {office_name}")
        except:
            print(f"Данной техники ({office_equipment}) на складе нет")


class OfficeEquipment:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price

    def __str__(self):
        return self.name


class Printer(OfficeEquipment):
    def __init__(self, name, size, price, color):
        super().__init__(name, size, price)
        self.color = color

    @classmethod
    # Проверка на тип данных атрибута color
    def valid_data(cls, name, size, price, color):
        if color != True and color != False:
            print(OwnError("Цветность должна быть типа bool, по умолчанию будет False"))
            color = False
        return cls(name, size, price, color)


class Scanner(OfficeEquipment):
    def __init__(self, name, size, price, paper_size):
        super().__init__(name, size, price)
        self.paper_size = paper_size


class Xerox(OfficeEquipment):
    def __init__(self, name, size, price, speed):
        super().__init__(name, size, price)
        self.speed = speed


p = Printer.valid_data('Принтер', "30Х30Х60", 23000, 335)
s = Scanner('Сканер', "40Х40Х40", 15000, "А4")
x = Xerox('Ксерокс', "20Х20Х20", 30000, 40)

w = Warehouse("Склад 1")

w.add_office_equipment(p)
w.add_office_equipment(s)
w.add_office_equipment(x)
w.add_office_equipment(x)

print(w.place)

w.transfer_to(p, 'Офис1')

print(w.place)
