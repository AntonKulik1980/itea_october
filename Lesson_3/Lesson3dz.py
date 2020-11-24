# Создать декоратор, который принимает на вход аргумент «количество
# повторений». Который будет вызывать функцию, определенное кол-во
# раз. Декорируемая функция должна возвращать:
# 1) Количество времени затраченное на каждый вызов;
# 2) Количество времени затраченное в общей сложности на все
# вызовы;
# 3) Имя декорируемой функции;
# 4) Значение последнего результата выполнения.


from functools import wraps
import timeit


def decorartor(number=3):
    for i in range(number):
        def actual_decorartor(func):
            @wraps(func)
            def wrapper(*name):
                tot_time = 0
                for i in range(number):
                    print('-' * number)
                    start_time = timeit.default_timer()
                    result = func(*name)
                    elapsed = timeit.default_timer() - start_time
                    tot_time += elapsed
                    print('-' * number)
                    print('Function "{name}" took {time} seconds to complete for the {times} time.'.format(
                        name=func.__name__, time=elapsed, times=i))
                print(f'Total execution time:{tot_time}')
                return result

            return wrapper

        return actual_decorartor


@decorartor(10)
def target_function(age, name):
    print(f'Hello world, {age},{name}')
    return 'Hello world'


# result = target_function(15, 'Anton')

# Создать классы структур данных:
# 1) Стек
# 2) Очередь.


class Stack:

    def __init__(self):
        self.stack = []

    def add(self, dataval):

        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    def remove(self):
        if len(self.stack) <= 0:
            return "No element in the Stack"
        else:
            return self.stack.pop()

    def peek(self):
        return self.stack[-1]


AStack = Stack()
AStack.add(1)
AStack.add(2)
AStack.add(3)


# print(AStack.peek())

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


AQueue = Queue()

AQueue.enqueue(1)
AQueue.enqueue(2)
AQueue.enqueue(3)
AQueue.enqueue(4)

print(AQueue.size())


# Создать класс комплексного числа и реализовать для него
# арифметические операции (не использовать стандартный тип
# complex).

def mul(c1, c2):
    real = c1.real * c2.real - c1.imag * c2.imag
    imag = c1.imag * c2.real + c1.real * c2.imag
    return Complex(real, imag)


class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        sign = '+' if self.imag >= 0 else ''
        return '{}{}{}i'.format(self.real, sign, self.imag)

    def add(self, c1, c2):
        real = c1.real + c2.real
        imag = c1.imag + c2.imag
        return Complex(real, imag)

    def sub(self, c1, c2):
        real = c1.real - c2.real
        imag = c1.imag - c2.imag
        return Complex(real, imag)

    def abs(self, c):
        return (c.real ** 2 + c.imag ** 2) ** 0.5


AComplex = Complex(1, 2)
print(AComplex.add(Complex(1, 2), Complex(3, 4)))
