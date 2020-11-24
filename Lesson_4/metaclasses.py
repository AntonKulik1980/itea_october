even_numbers = [1, 2, 3, 4]

metaclass = type(type(even_numbers))
print(type(metaclass))


def get_num_of_wheels(self):
    return self.num_of_wheels


Viechle = type('Viechle', (), {'num_of_wheels': 4, 'get_number': lambda self: self.num_of_wheels})

print(Viechle)
# print(Viechle.num_of_wheels)
# print(Viechle().get_num_of_wheels())



class CarMetaclass(type):

    def __new__(mcs, name, base, attrs):
        if not attrs.get('num_of_wheels'):
            raise NotImplementedError('vse ploho')



        car_class = super().__new__(mcs, name, base, attrs)
        print(car_class)
        return car_class

class Car(metaclass  = CarMetaclass):
    num_of_wheels  = 4

    def __init__(self,engine,model):
        self.engine = engine
        self.model = model

    def __call__(self, *args, **kwargs):
        print(f'I am {self.model}')

car = Car('V-8','mersedes')
car()

import time

class Decorator:


    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args,**kwargs)
        end = start - time.time()
        return result, end

@Decorator
def do_noting(seconds):
    time.sleep(seconds)


print(do_noting(2))




