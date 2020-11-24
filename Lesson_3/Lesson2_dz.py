# Task 1

class Cars:
    wheels = 4

    def __init__(self, hp, torq, fuel_cons):
        self.hp = hp
        self.torq = torq
        self.fuel_cons = fuel_cons

    def acs(self, sec):
        self.sec = sec
        print(
            f'We are acselerating {self.sec}  sec with {self.torq} torque and {self.hp} hp by loosing {self.fuel_cons} per 100 km')

    def brake(self):
        print(f'We are braking now to compensate of {self.hp} horse powers ')


class Trucks(Cars):
    wheels = 8

    def __init__(self, hp, torq, fuel_cons, cargo):
        self.hp = hp
        self.torq = torq
        self.fuel_cons = fuel_cons
        self.cargo = cargo

    def acs(self, sec):
        self.sec = sec
        print(
            f'We are acselerating {self.sec} with {self.torq}  torque and {self.hp} horse powers loosing {self.fuel_cons} per 100 km , watch out you have a {self.cargo} kg on board')

    def brake(self):
        print(
            f'We are braking now to compensate of {self.hp} horse powers ,watch out you have a {self.cargo} kg on board')


class Sportcars(Cars):
    wheels = 4

    def acs(self, sec):
        self.sec = sec
        print(
            f'We are acselerating {self.sec} with {self.torq}  torque and {self.hp} horse powers loosing {self.fuel_cons} per 100 km , watch out,  your car price has 000000 in price number')

    def brake(self):
        print(
            f'We are braking now to compensate of {self.hp} horse powers ,watch out,  your car price has 000000 in price number')


truck1 = Trucks('500', '900', '50', '20 000')
truck1.brake()
truck1.acs('50')
print('-' * 35)
Sportcar1 = Sportcars('1000', '9000', '40')
Sportcar1.brake()
Sportcar1.acs('100')


# Task2 Создать класс магазина. Конструктор должен инициализировать
# значения: «Название магазина» и «Количество проданных
# товаров». Реализовать методы объекта, которые будут увеличивать
# кол-во проданных товаров, и реализовать вывод значения
# переменной класса, которая будет хранить общее количество
# товаров проданных всеми магазинами.


def tot_sales():
    print(shop.added)


class shop():
    items: int
    added = 0

    def __init__(self, name, sales):
        self.name = name
        self.sales = sales
        shop.added += sales

    def sale(self, items):
        self.items = items
        self.sales = self.items + self.sales
        shop.added += self.items
        print(self.sales)

    def tot_sales(shop):
        print(shop.added)


print('-' * 35)
shop1 = shop('First', 10)
print(shop1.sales)
shop2 = shop('Second', 4)
print(shop2.sales)
print(shop2.sale(10))
# print(shop2.sale(15))
tot_sales()


# Создать класс точки, реализовать конструктор который
# инициализирует 3 координаты (x, y, z).Реалзиовать методы для
# получения и изменения каждой из координат. Перегрузить для этого
# класса методы сложения, вычитания, деления умножения.
# Перегрузить один любой унарный метод.
# Ожидаемый результат: умножаю точку с координатами 1,2,3 на
# другую точку с такими же координатами, получаю результат 1, 4, 9.

class point():
    point: int

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return self.x

    def set_x(self, value):
        self.x = value

    def get_y(self):
        return self.y

    def set_y(self, value):
        self.y = value

    def get_z(self):
        return self.z

    def set_z(self, value):
        self.z = value


    def __add__(self,other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z
        return point(new_x,new_y,new_z)

    def __mul__(self,other):
        new_x = self.x * other.x
        new_y = self.y * other.y
        new_z = self.z * other.z
        return point(new_x, new_y, new_z)


    def __sub__(self,other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_z = self.z - other.z
        return point(new_x, new_y, new_z)

    def __truediv__(self, other):
        new_x = self.x / other.x
        new_y = self.y / other.y
        new_z = self.z / other.z
        return point(new_x, new_y, new_z)

point1 = point(1,2,3)
point2 = point(1,2,3)
point3 = point(3,4,5)
add = point1*point2*point3
print(add.get_x())
print(add.get_y())
print(add.get_z())