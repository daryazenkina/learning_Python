# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Автомобиль {self.name} движется со скоростью {self.speed}")

    def stop(self):
        print(f"Автомобиль {self.name} стоит")

    def turn(self, direction):
        print(f"Автомобиль {self.name} повернул {direction}")

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = False

    def show_speed(self):
        print(self.speed if self.speed <= 60 else "Вы превысили скорость!")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = False


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = False

    def show_speed(self):
        print(self.speed if self.speed <= 40 else "Вы превысили скорость!")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = True


# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

t_c_1 = TownCar(30, 'color', 'TownCar1', False)
t_c_2 = TownCar(80, 'color', 'TownCar2', False)
s_c = SportCar(80, 'color', 'SportCar', False)
w_c1 = WorkCar(30, 'color', 'WorkCar1', False)
w_c_2 = WorkCar(80, 'color', 'WorkCar2', False)
p_c = PoliceCar(110, 'color', 'PoliceCar', False)

print(f'Имя:{t_c_1.name}, цвет:{t_c_1.color}, скорость:{t_c_1.speed}, полицейский?{t_c_1.is_police}')
print(f'Имя:{t_c_2.name}, цвет:{t_c_2.color}, скорость:{t_c_2.speed}, полицейский?{t_c_2.is_police}')
print(f'Имя:{s_c.name}, цвет:{s_c.color}, скорость:{s_c.speed}, полицейский?{s_c.is_police}')
print(f'Имя:{w_c1.name}, цвет:{w_c1.color}, скорость:{w_c1.speed}, полицейский?{w_c1.is_police}')
print(f'Имя:{w_c_2.name}, цвет:{w_c_2.color}, скорость:{w_c_2.speed}, полицейский?{w_c_2.is_police}')
print(f'Имя:{p_c.name}, цвет:{p_c.color}, скорость:{p_c.speed}, полицейский?{p_c.is_police}')

s_c.go()
s_c.turn("На лево")
s_c.show_speed()
s_c.stop()

t_c_1.go()
t_c_1.turn("На лево")
t_c_1.show_speed()
t_c_1.stop()

t_c_2.go()
t_c_2.turn("На лево")
t_c_2.show_speed()

w_c1.go()
w_c1.turn("На лево")
w_c1.show_speed()

w_c_2.go()
w_c_2.turn("На лево")
w_c_2.show_speed()
w_c_2.stop()
